# -*- encoding: utf-8 -*-
'''
@File    :   divide.py
@Time    :   2021/03/24 11:00:19
@Author  :   mike.wu 
@Contact :   xcwu@whu.edu.cn
'''
#划分训练集和测试集小工具
import os, random, shutil

def moveFile(fileDir, tarDir):
    pathDir = os.listdir(fileDir)    
    filenumber=len(pathDir)
    rate=0.2   #划分比例
    picknumber=int(filenumber*rate) 
    sample = random.sample(pathDir, picknumber) 
    print (sample)
    for name in sample:
        shutil.move(fileDir+'/'+name, tarDir+'/'+name)
    return

if __name__ == '__main__':
	fileDir = "./php"    #源文件目录
	tarDir = './t1'      #移动到新的文件夹路径
	moveFile(fileDir, tarDir)
