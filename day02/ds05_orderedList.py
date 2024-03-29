# file : ds05_orderedList.py
# desc : 다항식 선형리스트 표현과 계산 프로그램

def printPoly(p_x):
    term = len(p_x) - 1 # 최고차항 숫자 = 배열 길이 -1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1
    return polyStr

def calcPoly (xVal, p_x):
    retValue = 0
    term = len(p_x) - 1 # 최고차항 숫자 = 배열 길이 -1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1
    return retValue

## 전역 변수 선언    
px = [7, -4, 0, 5]  # = 7x^3 - 4x^2 + 0x^1 + 5x^0

## 메인 코드
if __name__ == '__main__':

    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('X 값 --> '))

    pxValue = calcPoly(xValue, px)
    print(pxValue)


## 특수 다항식의 선형리스트 표현과 계산 프로그램
## 함수 선언
def printPoly(t_x, p_x):
    polyStr = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i] # 항 차수
        coef = p_x[i] # 계수

        if (coef >= 0):
            polyStr += "+"
        polyStr += str(coef) + "x^" + str(term) + " "
    return polyStr

def calcPoly (xVal, t_x, p_x):
    retValue = 0

    for i in range(len(px)):
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xVal ** term
    return retValue

## 전역 변수 선언    
tx = [300, 20, 0]
px = [7, -4, 5]

## 메인 코드
if __name__ == '__main__':

    pStr = printPoly(tx, px)
    print(pStr)

    xValue = int(input('X 값 --> '))

    pxValue = calcPoly(xValue, tx, px)
    print(pxValue)