def solution(x, y):
    numberAtPositionx1 = findPositionx1(x)
    if (y == 1):
        return str(int(numberAtPositionx1))
    else:
        coefficentOfN = findCoefficentOfN(x)
        constant = findConstant(numberAtPositionx1, coefficentOfN)
        numberAtPositionxy = findxy(y, coefficentOfN, constant)
        return str(int(numberAtPositionxy))

def findPositionx1(x):
    return (x ** 2 + x)/2

def findCoefficentOfN(x):
    return x - 1.5

def findConstant(numberAtPositionx1, coefficentOfN):
    return numberAtPositionx1 - coefficentOfN - 0.5

def findxy(y, coefficentOfN, constant):
    return (0.5*y**2 + coefficentOfN*y + constant)

print(solution(3,2))
print(solution(5,10))
print(solution(6,3))
print(solution(3,7))