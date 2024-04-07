classNumber=int(input()) #반 개수

for i in range(classNumber):
  scoreInfo=list(map(int,input().split()))
  del scoreInfo[0]
  scoreInfo.sort()
  largestGap=0
  for j in range(0,len(scoreInfo)-1):
    if scoreInfo[j+1] - scoreInfo[j] > largestGap:
      largestGap=scoreInfo[j+1] - scoreInfo[j]
  maxValue=max(scoreInfo) #최대값
  minValue=min(scoreInfo) #최소값

  print('Class',i+1)
  print("Max %d, Min %d, Largest gap %d" %(maxValue,minValue,largestGap))
