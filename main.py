import bottle
import json
import data
import processing


import os.path


@bottle.post('/linepost')
def receive_chat():
  content = bottle.request.body.read().decode()


  list1= data.read_values("saved_data.csv")
  header=["date",'location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
  dic=data.dic_list_gen(header,list1)
  x=processing.copy_matching(dic,'location',content)

  y = json.dumps(x)

  return y






@bottle.route("/")
def default():
  return bottle.static_file("simple.html",root=".")

@bottle.route("/javacode.js")
def hi():
  print("test12")
  return bottle.static_file("javacode.js",root=".")

@bottle.route("/barpath")
def bar():
  print("test2")
  list1= data.read_values("saved_data.csv")
  header=["date",'location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
  dic=data.dic_list_gen(header,list1)
  maxdate = processing.max_value(dic,'date')
  x=processing.copy_matching(dic,'date',maxdate)
  y=data.make_lists(['location','series_complete_pop_pct'],x)

  return json.dumps(y)



@bottle.route("/piepath")
def pie():
  list1= data.read_values("saved_data.csv")
  header=["date",'location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
  dic=data.dic_list_gen(header,list1)
  maxdate = processing.max_value(dic,'date')
  x=processing.copy_matching(dic,'date',maxdate)

  jan=processing.sum_matches(x,'date',maxdate,'administered_janssen')
  mod=processing.sum_matches(x,'date',maxdate,'administered_moderna')
  pf=processing.sum_matches(x,'date',maxdate,'administered_pfizer')
  un=processing.sum_matches(x,'date',maxdate,'administered_unk_manuf')

  return json.dumps([jan,mod,pf,un])






def load_data( ):
   csv_file = 'saved_data.csv'
   if not os.path.isfile(csv_file):
     url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
     info = data.json_loader(url)
     heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
     data.save_data(heads, info, 'saved_data.csv')

load_data()

bottle.run(host="0.0.0.0", port=8080)