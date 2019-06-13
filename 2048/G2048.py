import os
import random
import numpy as np
import itertools as it

class G2048(object):
    HighScore = 0 #本次启动游戏的最高分
    TopScore = {} #历史排名前十

    def __init__(self):
        self.gamebroad = np.mat(np.zeros((4,4)))
        self.score = 0
        self.__randpoint()
        self.__randpoint()
        self.__getScore()
    
    def restart(self):
        self.gamebroad = np.mat(np.zeros((4,4)))
        self.score = 0
        self.__randpoint()
        self.__randpoint()
    
    def __isSame(self, x, y):
        pass

    def plusLine(self):
        pass
    
    def up(self):
        pass
    
    def down(self):
        pass
    
    def left(self):
        pass
    
    def right(self):
        pass
    
    def __randpoint(self):
        n = self.gamebroad[self.gamebroad == 0].size
        ser = random.randint(1, n)
        scala = 0
        for i in range(4):
            for j in range(4):
                if self.gamebroad == 0 :
                    scala = scala + 1
                    if scala == ser :
                        self.gamebroad[i,j] = 2 if random.random() < 0.9 else 4
                        break

    def isOver(self):
        pass
    
    def __getScore(self):
        if os.path.exists('data.gdata') :
            with open('data.gdata', mode = 'r', encoding = 'utf-8') as filed :
                data = filed.read()
                if data[0] == '\ufeff' :
                    data = data[1:]
                data = list(map(lambda x : x.split('%c43c56;'), data.split('\n')))
            G2048.TopScore =  dict(zip(
                list(map(lambda x : data[x][0] , range(10))),
                list(map(lambda x : {data[x][1]:data[x][2]} , range(10)))
            ))
    
    @classmethod
    def putTopScore():
        if G2048.TopScore == {} :
            print()