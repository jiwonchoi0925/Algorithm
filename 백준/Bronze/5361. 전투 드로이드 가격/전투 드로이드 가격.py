for i in range(int(input())):
    try:
        partA, partB, partC, partD, partE = map(int, input().split())
        totalCost = (partA * 350.34) + (partB * 230.90) + (partC * 190.55) + (partD * 125.30) + (partE * 180.90)
        print('$' + format(totalCost, '.2f'))
    except ValueError:
        print("입력 값이 잘못되었습니다. 5개의 숫자를 입력해주세요.")
        print('$' + format(totalCost, '.2f'))