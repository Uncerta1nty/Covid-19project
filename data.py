import csv
import json
import urllib.request


def json_loader(x):
  z=urllib.request.urlopen(x)
  xstr=z.read().decode()
  y= json.loads(xstr)
  return y



def make_values_numeric(x,y):
  for i in x:
    y[i]=float(y[i])
  return y



def save_data(x,y,z):
  a=[]
  with open(z,'w') as f:
    file = csv.writer(f)
    file.writerow(x)
    for k in y:   
      for j in x:
        a.append(str(k[j]))
      file.writerow(a)
      a=[]

def read_values(x):
  y=[]
  z=[]
  with open(x) as f:
    file = csv.reader(f)
    for i in file:
      for j in (range(len(i))):
        z.append(i[j])
      y.append(z)
      z=[]
  return y



def dic_list_gen(x,y):
  z={}
  t=[]
  for j in range(len(y)):
    for i in range(len(x)):
      z[x[i]]=y[j][i]
    t.append(z)
    z={}
  return t




def load_data(x):
  z = []
  with open(x, "r", newline="") as f:
    rr = csv.DictReader(f)
    for row in rr:
      z.append(row)
  return z


def dic_list_gen(x,y):
  z={}
  t=[]
  for j in range(len(y)):
    for i in range(len(x)):
      z[x[i]]=y[j][i]
    t.append(z)
    z={}
  return t


def read_values(x):
  y=[]
  z=[]
  with open(x) as f:
    file = csv.reader(f)
    next(file)
    for i in file:
      for j in (range(len(i))):
        z.append(i[j])
      y.append(z)
      z=[]
  return y






def make_lists(x,y):
  z=[]
  a=[]
  for j in y:
    for i in x:
      a.append(j.get(i))
    z.append(a)
    a=[]
  return z



def write_values(x,y):

      
  with open(x,'a') as f:
    file = csv.writer(f)

    for i in y:
      file.writerow(i)