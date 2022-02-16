// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received                                                              
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}



// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received                                                              
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}


function getData(){

  ajaxGetRequest("/barpath", showBar);
  ajaxGetRequest("/piepath",showPie)
}


function getLocData(){
  let myDiv= document.getElementById("locText");

  ajaxPostRequest("/linepost",myDiv["value"],showLine)
}


function showBar(response) {
    // Data is always sent in JSON, so we must first convert it                                                                                                                 
    let data = JSON.parse(response)
    let xvalues = []
    for (let i of data){
      xvalues.push(i[0])
    }
    let yvalues = []
    for (let i of data){
      yvalues.push(i[1])
    }
    
    // Now write the code that uses data to create the scatter plot
  z = [
  {
    x: xvalues,
    y: yvalues,
    type: 'bar'
  }
];

var layout = {
  title: 'fully vaccinated By location',
  font:{
    family: 'Raleway, sans-serif'
  },
  showlegend: false,
  xaxis: {
    title: 'Location',

  },
  yaxis: {
    title: '% fully vaccinated',

  },

};




Plotly.newPlot('myDivbar', z,layout);



}


function showPie(response) {
    // Data is always sent in JSON, so we must first convert it                                                                                                                 
    let data = JSON.parse(response)
    let vals =[]
    let names = ['Janssen', 'Moderna', 'Pfizer', 'Other']




  var z = [{
  type: "pie",
  values: data,
 
  labels: names,
  textinfo: "label+percent",
  insidetextorientation: "radial"
}]

var layout = [{
  height: 700,
  width: 700
}]

Plotly.newPlot('myDivpie', z, layout)

}

function showLine(response) {
    // Data is always sent in JSON, so we must first convert it                                                                                                                 
    let data = JSON.parse(response)
    let xdata=[]
    let ydata=[]
    let state = data[0]['location']
    for (i of data){
      xdata.unshift(i['date'])
    }
    for (i of data){
      ydata.unshift(i['series_complete_pop_pct' ])
    }
var trace2 = {
  x: xdata,
  y: ydata,
  mode: 'lines',
  name: 'Lines'
};



var z = [trace2];

var layout = {
  title: '% of '+ state+' Vaccinated by Date   ',
  xaxis: {
    title: 'Date'
  },
  yaxis: {
    title: '% fully vaccinated'
  }
};

Plotly.newPlot('myDivline', z, layout);

}
