import base64
import urllib.parse
import html

def bs64(mode,s):
    if mode == 'in':
        try:
            a=str(base64.b64encode(s.encode("utf-8")), "utf-8")
            print (a)
        except:
            print("input error")
    elif mode == 'un':
        try:
            s=s+'=='
            a=str(base64.b64decode(s),"utf-8")
            print (a)
        except:
            print("input error")

def asc(mode,s):
    if mode == 'in':
        try:
            print (ord(s))
        except:
            print("input error")
    elif mode == 'un':
        try:
            print (chr(int(s)))
        except:
            print("input error")

def unicode(mode,s):
    if mode == 'in':
        try:
            a = s.encode('unicode-escape')
            print (a)
        except:
            print("input error")
    elif mode == 'un':
        try:
            a = s.encode('utf-8').decode('unicode-escape')
            print (a)
        except:
            print("input error")

def url(mode,s):
    if mode=='in':
        try:
            a=urllib.parse.quote(s)
            print (a)
        except:
            print("input error")
    elif mode=='un':
        try:
            a=urllib.parse.unquote(s)
            print (a)
        except:
            print("input error")

def ht(mode,s):
    if mode=='in':
        try:
            a=html.escape(s)
            print(a)
        except:
            print("input error")
    elif mode=='un':
        try:
            a=html.unescape(s)
            print(a)
        except:
            print("input error")
def inp():
    mode = input("input in or  un ,in is encode，un is decode：<")
    s = input("input the strings you want to decode or encode:<")
    return mode,s

def main():
    bm = input("please choose  1:base64,2:ascii,3:unicode,4:url,5:html,6:exit:")
    try:
        bm=int(bm)
    except:
        print("choose error")
        main()
    if bm == 1:
        mode,s=inp()
        bs64(mode,s)
    elif bm==2:
        mode, s = inp()
        asc(mode,s)
    elif bm==3:
        mode, s = inp()
        unicode(mode,s)
    elif bm==4:
        mode, s = inp()
        url(mode,s)
    elif bm==5:
        mode, s = inp()
        ht(mode,s)
    else:
        exit()

if __name__ == "__main__":
    while True:
        main()
