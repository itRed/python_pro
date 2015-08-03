#!/usr/bin/python
# coding:utf-8
# @author: Red
# @version: 1.0
'''
Created on 2015-8-3
读取一行数据，处理一行数据(效率很低)
@author: Red
'''
import MySQLdb

if __name__ == '__main__':
    filepath = 'E://red.txt'
    f = open(filepath, 'r')
    while True:
        line = f.readline()
        if line:
            arr = line.replace('\n', '').split(' ')
            # print arr[0],arr[1]
            conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', charset="utf8")
            curs = conn.cursor()
            conn.select_db('pythondb')
            values = []
            values.append((arr[0], arr[1]))
            curs.executemany("INSERT INTO pythondb.user(USER_NAME,USER_AGE)VALUES(%s,%s)", values)
            conn.commit()
            curs.close()
            conn.close()     
        else :
            break
    print 'finish'
