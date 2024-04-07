import math

vacationDate=int(input())

totalKorean=int(input())
totalMath=int(input())
maxKorean=int(input())
maxMath=int(input())
mathDate=math.ceil(totalMath/maxMath)
koreanDate=math.ceil(totalKorean/maxKorean)
print(vacationDate - max(mathDate,koreanDate))