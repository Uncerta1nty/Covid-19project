def max_value(list1,key):
  big=''
  for i in list1:
    if(i[key]>big):
      big=i[key]
  return big



def init_dictionary(list1,key):
  new={}
  v=''
  for i in list1:
    if(key in i):
      v=i[key]
      new[v]=0
  return new
      
def sum_matches(lod,k,v,tgt):
  val=0
  for i in lod:
    if(i[k]==v):
      val+=int(i[tgt])
  return val

def copy_matching(lod,k,v):
  val=[]
  for i in lod:
    if(k in i and i[k]==v):
      val.append(i)
  return val