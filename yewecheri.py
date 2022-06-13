### 숫자만 골라 실수형으로 ##

>>> i = [i = ['123!!', '151,767', '11,093', '27,394', '', '!!!$%']
### i에 특수 문자와 빈 문자열로 된 원소를 추가합니다.
  for j in i:
try:
		i[i.index(j)] = float(re.sub(',', '', j)) # 모든 j를 실수형으로 바꿔봅니다.
except:                                       # 오류가 발생하면
  pass                                        # pass를 실행해 넘어갑니다.
  
>>> i 


서울시 poplist

>>> import os,re
>>> import usecsv
>>> os.chdir(r'C:----')
>>> total = usecsv.opencsv('popSeoul.csv')

>>> for i in total [:5]:
    print(i)
    
    
# 예외 처리로 숫자만 골라서 숫자형으로 바꾸기
 
>>> total
	 
	 .........
	 
>>> i = total[1]    #먼저 리스트 하나만 가져와 i에 저장해 실험해 봅니다.
>>>for j in i:
	 try:
	 	i[i.index(j)] = float(re.sub(',', '', j))
	 except:
	 	pass
>>> i 
	 #결과값    # 숫자만 실수형으로 잘 바뀌는지 확인
>>> for i in total:  # total 객체의 모든 리스트를 가져와 앞에서 만든 명령을 적용합니다.
	 for j in i:
	 	try:
	 		i[i.index(j)] = float(re.sub(',', '', j))
	 except:
	 	pass
>>> total
	 #결과값     # 모든 숫자가 실수형으로 잘 바뀐것을 확인 
	 
