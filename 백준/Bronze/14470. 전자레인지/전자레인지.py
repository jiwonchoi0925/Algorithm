originTemp=int(input())  #원래 고기의 온도
targetTemp=int(input()) #목표 온도
icedOneDegree=int(input()) #얼어있는 고기 1도 데우는데 걸린 시간
defrostTime=int(input()) #얼어있는 고기 해동하는데 걸린 시간
nonIcedOneDegree=int(input()) #얼지 않은 고기를 1도 데우는데 걸린 시간
totalTime=0 #고기를 목표온도로 데우는데 걸리는 시간

if originTemp < 0 :
  totalTime=(-originTemp*icedOneDegree)+defrostTime+(targetTemp*nonIcedOneDegree)
else:
  totalTime=(targetTemp-originTemp)*nonIcedOneDegree

print(totalTime)