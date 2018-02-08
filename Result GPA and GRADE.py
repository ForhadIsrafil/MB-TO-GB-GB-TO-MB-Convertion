
def b():
    
    b= int(input("enter ur bangla numbr"))

    if b>=80:
        bb=5
        return bb
    #print("u got a+ in bangla")
    elif b>=70:
        bb=4
        return bb
    #print("u got a in bangla")
    elif b>=60:
        bb=3
        return bb
        #print("u got b in bangla")
    elif b>=50:
        bb=2
        return bb
    #print("u got c in bangla")
    elif b>=40:
        bb=1
        return bb
    #print("u got d in bangla")
    else :
        bb=0
        return bb
   #print("u r fail bangla")


def e():
    e=int(input("enter ur english numbr"))

    if e>=80:
        ee=5
        return ee
    #print("u got a+ in bangla")
    elif e>=70:
        ee=4
        return ee
    #print("u got a in bangla")
    elif e>=60:
        ee=3
        return ee
    #print("u got b in bangla")
    elif e>=50:
        ee=2
        return ee
    #print("u got c in bangla")
    elif e>=40:
        ee=1
        return ee
    #print("u got d in bangla")
    else :
        ee=0
        return ee
   #print("u r fail bangla")
def m():
    m=int(input("enter ur math numbr"))

    if m>=80:
        mm=5
        return mm
    #print("u got a+ in bangla")
    elif m>=70:
        mm=4
        return mm
    #print("u got a in bangla")
    elif m>=60:
        mm=3
        return mm
    #print("u got b in bangla")
    elif m>=50:
        mm=2
        return mm
    #print("u got c in bangla")
    elif m>=40:
        mm=1
        return mm
    #print("u got d in bangla")
    else :
        mm=0
        return mm
   #print("u r fail bangla")

def p():
    p=int(input("enter ur physics numbr"))

    if p>=80:
        pp=5
        return pp
    #print("u got a+ in bangla")
    elif p>=70:
        pp=4
        return pp
    #print("u got a in bangla")
    elif p>=60:
        pp=3
        return pp
    #print("u got b in bangla")
    elif p>=50:
        pp=2
        return pp
    #print("u got c in bangla")
    elif p>=40:
        pp=1
        return pp
    #print("u got d in bangla")
    else :
        pp=0
        return pp
   #print("u r fail bangla")
def c():
    c=int(input("enter ur chemistry numbr"))

    if c>=80:
        cc=5
        return cc
    #print("u got a+ in bangla")
    elif c>=70:
        cc=4
        return cc
    #print("u got a in bangla")
    elif c>=60:
        cc=3
        return cc
    #print("u got b in bangla")
    elif c>=50:
        cc=2
        return cc
    #print("u got c in bangla")
    elif c>=40:
        cc=1
        return cc
    #print("u got d in bangla")
    else :
        cc=0
        return cc
   #print("u r fail bangla")

def z():
    z=int(input("enter ur biology numbr"))

    if z>=80:
        zz=5
        return zz
    #print("u got a+ in bangla")
    elif z>=70:
        zz=4
        return zz
    #print("u got a in bangla")
    elif z>=60:
        zz=3
        return zz
    #print("u got b in bangla")
    elif z>=50:
        zz=2
        return zz
    #print("u got c in bangla")
    elif z>=40:
        zz=1
        return zz
    #print("u got d in bangla")
    else :
        zz=0
        return zz
   #print("u r fail bangla")

def h():
    h=int(input("enter ur h.math numbr"))

    if h>=80:
        hh=5
        return hh
    #print("u got a+ in bangla")
    elif h>=70:
        hh=4
        return hh
    #print("u got a in bangla")
    elif h>=60:
        hh=3
        return hh
    #print("u got b in bangla")
    elif h>=50:
        hh=2
        return hh
        #print("u got c in bangla")
    elif h>=40:
        hh=1
        return hh
    #print("u got d in bangla")
    else :
        hh=0
        return hh
   #print("u r fail bangla")

result =format((b()+e()+m()+p()+c()+z()+h())/7, '.2f')
print("result",result)
