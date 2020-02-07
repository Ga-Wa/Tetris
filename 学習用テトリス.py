import tkinter as tk
import math

class Model():

    width = 7 #横軸の盤面の数
    height = 15 #縦軸の盤面の数

    def __init__(self):
        self.data=[[0]*Model.width for i in range(Model.height)] #0の用を入れた二次元配列の作成
        self.NumberX=math.floor(Model.width/2) #横軸
        self.NumberY=0 #縦軸

    def map_all(self,list): #横が揃っているかか判定する。揃っていたらTrueを返す
        judge=[]
        if list:
            for 1 in list[1:]:
                judge.append(list[0] == 1)
            return all(judge)
        else:
            return False

    def leftModel(self): #左矢印キーが押されたら
        if self.NumberX > 0: #左端かどうか
            self.NumberX = self.NumberX-1

    def rightModel(self): #右矢印キーが押されたら
        if self.NumberX < Model.width-1: #右端かどうか
            self.NumberX = self.NumberX+1

    def downModel(self): #下矢印キーが押されたら
        if self.NumberY < Model.height-1 and self.data[self.NumberY+1][self.NumberX] != 2: #盤面の一番下かつ下ブロックが2でないなら真
            self.NumberY = self.NumberY+1
    
    def update(self):
        for i in range(Model.height): #盤面をすべて0にする
            for j in range(Model.width):
                if self.data[i][j] == 1:
                    self.data[i][j] = 0

        if self.NumberY > 0: #ブロック2つ分を1にする
            self.data[self.NumberY-1][self.NumberX] = 1
            self.data[self.NumberY][self.NumberX] = 2

        if self.NumberY == Model.height-1 or self.data[self.NumberY+1][self.NumberX] == 2:  #判定(一番下または下ブロックが2)
            self.data[self.NumberY-1][self.NumberX] = 2
            self.data[self.NumberY][self.NumberX] = 2

            for i in range(Model.height):
                if self.map_all(self.data[i]):  #横が揃っているかどうか判定
                    for j in range(Model.width):
                        self.data[i][j] = 0
            
            self.NumberX = math.floor(Model.width/2)
            self.NumberY = 0

        self.NumberY = (self.numberY+1)%Model.height

class View():

    def __init__(self,master,model,controller):
        self.master = master
        self.model = model
        self.controller = controller

        