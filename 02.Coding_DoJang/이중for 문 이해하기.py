temp=[0,0,0,0,0,0,0,0,0,0] # 리스트 생성
for num in range(1,1001): #0~1000
  for tp in (str(num)): # 각 숫자를 배열로 취급하기 위해 string화 시킴
    temp[int(tp)]+=1 # 넣을땐 다시 int로 해서 temp에 넣음

for i in range(10): # 출력
  print(i,":",temp[i],"개")