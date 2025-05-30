import sys

def uret(str):
    a=''
    b=0
    k = str[2]
    l = str[3]
    a = k.split('=')[1]
    b = l.split('=')[1]
    return a,b

zeynep=sys.argv
x,y=uret(zeynep)