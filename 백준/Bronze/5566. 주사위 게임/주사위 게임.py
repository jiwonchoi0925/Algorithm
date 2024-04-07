N,M=map(int,input().split())
boardLength=[] #보드판 길이
dice=[] # 주사위 던진 횟수
currentPosition=0  #현재 위치
distance=0 #남은 칸 수 

for a in range(0,N):
  boardLength.append(int(input()))  #배열에 길이 넣기

for b in range(0,M):
  dice.append(int(input()))

for c in range(1,1+M):
  currentPosition +=dice[c-1]
  if currentPosition+1 >= N:
    print(c)
    break
  distance=boardLength[currentPosition]
  currentPosition +=distance
  if currentPosition+1 >= N:
    print(c)
    break