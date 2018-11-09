#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
9*9大小的数独求解
'''

import copy

q1 = [
    [0, 4, 0, 0, 8, 7, 0, 0, 3],
    [1, 0, 0, 0, 6, 4, 8, 0, 0],
    [0, 8, 9, 0, 0, 5, 0, 0, 0],
    [8, 6, 5, 2, 0, 3, 0, 0, 0],
    [4, 0, 0, 0, 9, 1, 0, 0, 0],
    [0, 1, 2, 0, 5, 0, 3, 7, 6],
    [6, 7, 8, 0, 3, 2, 9, 0, 4],
    [0, 0, 1, 7, 4, 9, 0, 5, 0],
    [5, 0, 0, 8, 1, 6, 7, 3, 2]
]

q2 = [
    [0, 8, 0, 0, 0, 0, 4, 0, 0],
    [7, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [1, 0, 5, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 1, 5],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 9, 0, 0, 4, 8, 0, 0, 0]
]

q3 = [
    [0, 9, 0, 0, 0, 4, 7, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 7, 4, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 5, 0, 0, 8, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 4, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 1, 0, 0, 0]
]

class sudoku():
    
    q, p = [], []
    
    def __init__(self, q):
        self.q = copy.deepcopy(q)
        self.p = [[list(range(1, 10)) for i in range(9)] for j in range(9)]
    
    def update_p(self, i, j, n):
        if n<1 or n>9:
            print("数字超范围：{}".format(n))
            return False
        self.p[i][j] = [n]
        for x in range(9):
            # 处理同一行
            if x!=j:
                if n in self.p[i][x]:
                    self.p[i][x].remove(n)
            # 处理同一列
            if x!=i:
                if n in self.p[x][j]:
                    self.p[x][j].remove(n)
        # 处理同一九宫格
        for x in range(int(i/3)*3, int(i/3)*3+3):
            for y in range(int(j/3)*3, int(j/3)*3+3):
                if x!=i and y!=j and n in self.p[x][y]:
                    self.p[x][y].remove(n)
        for x in range(9):
            for y in range(9):
                if len(self.p[x][y])<1:
                    return False
        return True

    def check_p_col(self, i, j, n):
        for x in range(9):
            if x!=i and n in self.p[x][j]:
                return False
        return True

    def check_p_row(self, i, j, n):
        for y in range(9):
            if y!=j and n in self.p[i][y]:
                return False
        return True

    def check_p_patch(self, i, j, n):
        for x in range(int(i/3)*3, int(i/3)*3+3):
            for y in range(int(j/3)*3, int(j/3)*3+3):
                if (x!=i or y!=j) and n in self.p[x][y]:
                    return False
        return True

    def check_p(self, i, j, n):
        if self.check_p_col(i, j, n) or self.check_p_row(i, j, n) or self.check_p_patch(i, j, n):
            return True
        return False

    def is_solved(self):
        for i in range(9):
            for j in range(9):
                if self.q[i][j] == 0:
                    return False
                else:
                    if len(self.p[i][j]) != 1:
                        return False
                    elif self.q[i][j]!=self.p[i][j][0]:
                        return False
        return True

    def update_q(self):
        for i in range(9):
            for j in range(9):
                if len(self.p[i][j])==1:
                    if self.q[i][j]==0:
                        self.q[i][j] = self.p[i][j][0]
                    elif self.q[i][j]!=self.p[i][j][0]:
                        return False
                elif len(self.p[i][j]) > 1:
                    for p_data in self.p[i][j]:
                        if self.check_p(i, j, p_data):
                            self.q[i][j] = p_data
                            break
        return True

    def print_p(self):
        for i in range(9):
            print(self.p[i])

    def print_q(self):
        for i in range(9):
            print(self.q[i])

    def count_q(self):
        c = 0
        for i in range(9):
            for j in range(9):
                if self.q[i][j]>0:
                    c += 1
        return c

    def choose_p(self):
        for x in range(9):
            for y in range(9):
                if len(self.p[x][y])>1:
                    return x, y
        return 9, 9

    def solve(self):
        while not self.is_solved():
            for i in range(9):
                for j in range(9):
                    if self.q[i][j]>0:
                        if not self.update_p(i, j, self.q[i][j]):
                            return False
            c_before = self.count_q()
            if not self.update_q():
                return False
            c_after = self.count_q()
            if c_after == c_before:
                break
        while not self.is_solved():
            i, j = self.choose_p()
            if i==9:
                break
            for p_data in self.p[i][j]:
                sudo_tmp = sudoku(self.q)
                sudo_tmp.q[i][j] = p_data
                if sudo_tmp.solve():
                    self.q = sudo_tmp.q
                    self.p = sudo_tmp.p
                    return True
            return False
        return True

def main(q):
    s = sudoku(q)
    if s.solve():
        print("解决")
    else:
        print("未能解决")
    s.print_p()
    s.print_q()

if __name__ == '__main__':
    main(q1)
    main(q2)
    main(q3)