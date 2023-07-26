import sys
import datetime


def help():
    data = "abcd"
    sys.stdout.buffer.write(data.encode('utf8'))


def list(task):
    file = open('todo.txt','a')
    file.write(task)
    file.close("/n")
    print("Task added")

def ls():
    file = open('todo.txt',"r")
    file.read()
