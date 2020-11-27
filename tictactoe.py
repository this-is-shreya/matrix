# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:40:51 2020

@author: shreya
"""
import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1='x'
p2='0'
def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input("enter row position"))
        col=int(input("enter col position"))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print("please enter a valid input")
    board[row-1][col-1]=symbol
    
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
    return False
def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,"won")
            return True
    return False
    
def check_diagonals(symbol):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==symbol:
        print(symbol,"has won")
        return True
    if board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[0][2]==symbol:
        print(symbol,"has won")
        return True
    return False
def won(symbol):
    return check_col(symbol) or check_rows(symbol) or check_diagonals(symbol)
    print(numpy.matrix(board))
def play():
    for turn in range(9):
        if turn%2==0:
            print("x turn")
            place(p1)
            if won(p1):
                break
        else:
            print("0 turn")
            place(p2)
            if won(p2):
                break
    if not(won(p1)) and not(won(p2)):
            print("its a draw")
play() 