#Create new bin python file what will become module(lib)

def opencsv(filename):
#import csv module first when start.
  f = open(filename, 'r')
  reader = csv.reader(f)
  output = []
  for i in reader:
    output.append(i)
  f.close
  return output
#opencsv() 함수에서는 f를 파일 객체로 해 직접 open 하는 방식을 사용

def writecsv(filename, the_list):
  with open(filename, 'w', newline = '') as f:
    a = csv.writer(f, delimiter = ',')
    a.writerows(the_list)
#writecsv() 함수에서는 with 문을 사용해 코드 길이가 조금 더 짧습니다.

###########test############

import usecsv
os.chdir(r'경로')
a = [['국어','영어','수학'],[99,88,77]]
usecsv.writercsv('test.csv', a)
