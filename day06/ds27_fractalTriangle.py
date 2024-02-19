# file : ds27_fractalTriangle.py
# desc : 시에르핀스키 삼각형 그리기

from tkinter import *

def drawTriangle(x, y, size):
    if size >= 30:
        drawTriangle(x, y ,size/2) # 왼쪽아래 작은 삼각형
        drawTriangle(x+size/2, y ,size/2) # 오른쪽 아래 작은 삼각형
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은 삼각형
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill = 'skyblue', outline = 'blue')

# 전역변수
wSize = 1000
radius = 400

# 메인코드
window = Tk()
window.title('삼각형 모양의 프랙탈')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
window.mainloop()