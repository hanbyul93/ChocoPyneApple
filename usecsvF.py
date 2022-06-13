import csv, re
def opencsv(filename):
  f = open(filename, 'r')
  reader - csv.reader(f)
  output = []
  for i in reader:
    output.append(i)
  return output

def writecsv(filename, the_list):
  with open(filename, 'w', newline = '') as f:
    a = csv.writer(f, delimiter = ',')
    a.writerows(the_list)
    
 # usecsv.py switch() 함수를 추가합니다.
def switch(listName):
  for i in listName:
    for j in i:
      try:
        i[i.index(j)] = float(re.sub(',', '', j))
      except:
        pass
   return listName
