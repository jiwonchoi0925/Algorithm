n=int(input())
height=list(map(int,input().split()))
ascent=0
maxValue=[]
for i in range(n-1):
  if height[i]<height[i+1]:
    ascent+=height[i+1]-height[i]
  else:
    maxValue.append(ascent)
    ascent=0
maxValue.append(ascent)
print(max(maxValue))