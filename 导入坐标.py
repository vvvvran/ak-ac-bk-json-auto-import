# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:56:37 2023

@author: 24562
"""
import os
import shutil
cwd=os.getcwd()
print(cwd)
try:
    shutil.rmtree('teleports')
except:
    print("teleports文件夹不存在")
os.mkdir('teleports')
cou=1
filelst=[]
for file_name in os.listdir(os.path.join(cwd,'坐标')):
    print(cou,end='.')
    print(file_name)
    filelst.append(file_name)
    cou+=1
print("输入坐标编号，可多选，如 1 3 4 12，回车确认,如果风神瞳和岩神瞳里面都有1.json，两个会因为名字冲突只导入一个，其他坐标也是")
str=input()
for i in str.split(' '):
    for files in os.listdir(os.path.join(cwd+'\\坐标',filelst[int(i)-1])):
        shutil.copy(os.path.join(os.path.join(cwd+'\\坐标',filelst[int(i)-1]),files), os.path.join(cwd,'teleports')) 