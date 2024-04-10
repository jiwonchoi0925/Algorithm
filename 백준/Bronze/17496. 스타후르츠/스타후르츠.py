summerDate, growDays, plantAmount, perPrice = map(int,input().split())
totalProfit=((summerDate-1)//growDays)*plantAmount*perPrice
print(totalProfit)