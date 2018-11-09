#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
9*9大小的数独求解
'''

q0 = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

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

p = [[list(range(1, 10)) for i in range(9)] for j in range(9)]

def update_p(i, j, n):
    global p
    if n<1 or n>9:
        return False
    p[i][j] = [n]
    for x in range(9):
        # 处理同一行
        if x!=j:
            try:
                p[i][x].remove(n)
                if len(p[i][x])==1:
                    update_p(i, x, p[i][x][0])
            except ValueError:
                pass
        # 处理同一列
        if x!=i:
            try:
                p[x][j].remove(n)
                if len(p[x][j])==1:
                    update_p(x, j, p[x][j][0])
            except ValueError:
                pass
    # 处理同一九宫格
    if i<3:
        if j<3:
            for x in range(3):
                for y in range(3):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        elif j>5:
            for x in range(3):
                for y in range(6, 9):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        else:
            for x in range(3):
                for y in range(3, 6):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
    elif i>5:
        if j<3:
            for x in range(6, 9):
                for y in range(3):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        elif j>5:
            for x in range(6, 9):
                for y in range(6, 9):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        else:
            for x in range(6, 9):
                for y in range(3, 6):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
    else:
        if j<3:
            for x in range(3, 6):
                for y in range(3):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        elif j>5:
            for x in range(3, 6):
                for y in range(6, 9):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass
        else:
            for x in range(3, 6):
                for y in range(3, 6):
                    if x!=i and y!=j:
                        try:
                            p[x][y].remove(n)
                            if len(p[x][y])==1:
                                update_p(x, y, p[x][y][0])
                        except ValueError:
                            pass

def check_p(i, j, n):
    for x in range(9):
        if x!=i and n in p[x][j]:
            return False
    for y in range(9):
        if y!=j and n in p[i][y]:
            return False
    if i<3:
        if j<3:
            for x in range(3):
                for y in range(3):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        elif j>5:
            for x in range(3):
                for y in range(6, 9):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        else:
            for x in range(3):
                for y in range(3, 6):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
    elif i>5:
        if j<3:
            for x in range(6, 9):
                for y in range(3):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        elif j>5:
            for x in range(6, 9):
                for y in range(6, 9):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        else:
            for x in range(6, 9):
                for y in range(3, 6):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
    else:
        if j<3:
            for x in range(3, 6):
                for y in range(3):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        elif j>5:
            for x in range(3, 6):
                for y in range(6, 9):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
        else:
            for x in range(3, 6):
                for y in range(3, 6):
                    if x!=i and y!=j and n in p[x][y]:
                        return False
    return True

def check_q(q):
    for i in range(9):
        for j in range(9):
            if q[i][j] == 0:
                return False
    return True

def update_q(q):
    for i in range(9):
        for j in range(9):
            if len(p[i][j])==1 and q[i][j]==0:
                q[i][j] = p[i][j][0]
            elif len(p[i][j]) > 1:
                for p_data in p[i][j]:
                    if check_p(i, j, p_data):
                        q[i][j] = p_data
                        print(i, j, p_data)
                        break

def print_p():
    global p
    for i in range(9):
        print(p[i])

def print_q(q):
    for i in range(9):

def count_q(q):
    c = 0
    for i in range(9):
        for j in range(9):
            if q[i][j]>0:
                c +=liu@1990

    return c

def main(q):
    global p
    while not check_q(q):
        for i in range(9):
            for j in range(9):
                if q[i][j]>0 and len(p[i][j])>1:
                    update_p(i, j, q[i][j])
        c_before = count_q(q)
        update_q(q)
        c_after = count_q(q)
        if c_after == c_before:
            break
        print(count_q(q))
    print_p()
    print_q(q)

if __name__ == '__main__':
    main(q2)