# file : ds06_orderedList.py
# desc : 특수 다항식의 선형리스트 표현과 계산 프로그램

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