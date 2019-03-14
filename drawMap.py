from tkinter import *
from loadData import readAllData


class CanvasDemo:
    def __init__(self, roads, nodes):
        self.roads = roads
        self.nodes = nodes
        window = Tk() #创建窗口
        window.title("Canvas Demo") #给窗口命名

        #在窗口画布
        self.canvas = Canvas(window, width=800, height=800, bg = "white")
        self.canvas.pack()

        #创建frame的框架，窗口window为这个框架的父容器
        frame = Frame(window)
        frame.pack()
        # #frame框架作为Button的父容器
        btClear = Button(frame, text = "Clear", command = self.displayClear)

        # #Button在画布上布局
        btClear.grid(row=1, column = 7)
        self.drawMap()
        #创建事件循环直到关闭主窗口
        window.mainloop()

    def drawMap(self):
        startPoint = (100, 700)
        startId = 1
        nodeMap = {startId: startPoint}
        self.displayPoint(startPoint[0], startPoint[1], startId)
        for road in self.roads:
            roadId = road.id
            startId = road.startId
            endId = road.endId
            length = road.length * 10
            isTowWay = road.isTowWay

            endNode = self.getNodeById(endId)
            startPoint = nodeMap.get(startId)
            rot = endNode.roadId.index(roadId)
            if rot == 0:
                endPoint = (startPoint[0], startPoint[1] + length)
            elif rot == 1:
                endPoint = (startPoint[0] - length, startPoint[1])
            elif rot == 2:
                endPoint = (startPoint[0], startPoint[1] - length)
            elif rot == 3:
                endPoint = (startPoint[0] + length, startPoint[1])
            nodeMap[endId] = endPoint
            self.displayPoint(endPoint[0], endPoint[1], endId)
            self.displayLine(endPoint[0], endPoint[1], startPoint[0], startPoint[1], roadId)

    def getNodeById(self, id):
        for x in self.nodes:
            if x.id == id:
                return x

    #fill填充oval的颜色
    def displayPoint(self, x, y, id):
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill = "red", tags = "oval")
        self.canvas.create_text(x-15, y+15, text=str(id), font="time 10 bold ", tags="string")

    #arrow表示line指向，activefill：当鼠标在line上时出现的特定风格，本例中鼠标移动到第二个line上时line变蓝
    def displayLine(self, x1, y1, x2, y2, id):
        # self.canvas.create_line(10,10,190,90,fill = "red",tags = "line")
        self.canvas.create_line(x1,y1,x2,y2,width = 2,arrow = "first", fill = "blue", tags = "line")
        self.canvas.create_text((x1+x2)/2, (y1+y2)/2, text=str(id), font="time 10 bold ", tags="string")

    #delete方法通过tags参数从画布上删除图形
    def displayClear(self):
        self.canvas.delete("rect","oval","arc","polygon","line","string")

cars, nodes, roads = readAllData()
canvas = CanvasDemo(roads, nodes)
# canvas.drawMap()
