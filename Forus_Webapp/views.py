from django.shortcuts import render
from . import views
from Forus_Webapp.models import *
from datetime import datetime


# Create your views here.

def index(req):
    return render(req,'index.html')
    
def dash1(req):
    return render(req,'dash1.html')

def dash2(req):
    return render(req,'dash2.html')


def admin2(req):
	return render(req,'admin.html')

def reg(req):
	return render(req,'reg.html')

def reg1(req):
    name=req.POST.get('Uname')
    pwd=req.POST.get('Pwd')
    Email=req.POST.get('Email')
    phone=req.POST.get('PNum')
    x=register1(name=name,email=Email,password=pwd,phno=phone)
    x.save()
    return render(req,"register.html",{'msg':'Registerd sucessfully'})

def login11(req):
    Name=req.POST.get('name')
    pwd=req.POST.get('pwd')

    ulist=register1.objects.all().values()
    uname_list=[]
    for i in ulist:
        
        Password=register1.objects.get(name=Name)
        if(Password.password==pwd):
            x=register1.objects.all()
            req.session['id']=Name
            list1=x.values()
            m = register1.objects.get(name=req.session['id'])
            print(m.name)
            return render(req,'dash2.html',{'list1':list1,'list1':m})
        else:
            return render(req,'register.html',{"error":"inccorect usernmae and password"})

def logout(req):
    return render(req,"admin.html",{'error':"you have logged out"})

def classic(req):
     return render(req,'classicR1.html')

def classichd(req):
     return render(req,'classicHDR1.html')

def classic64(req):
     return render(req,'classic6.4R1.html')

def flora(req):
     return render(req,'flora.html')

def Aberro(req):
     return render(req,'Aberro.html')

def Neo(req):
     return render(req,'Neo.html')

def cbin(req):
     return render(req,'cbin1.html')

def Bin_info(req):
     return render(req,'Bin_info.html')

def cbin2(req):
     return render(req,'cbin2.html')

def dash3(req):
     return render(req,'dash3.html')
     
def dash4(req):
     return render(req,'dash4.html')

def d(req):
     return render(req,'d.html')

def productedit(req):
     return render(req,'addproduct.html')

def edit(req):
     return render(req,'edit.html')


def reg3(req):
    ename=req.POST.get('rname')
    pwd=req.POST.get('password')
    rpwd=req.POST.get('repassword')
    Email=req.POST.get('remail')
    phone=req.POST.get('phone')
    DoB=req.POST.get('location')
    Gender=req.POST.get('gender')
    x=empreg1(name=ename, email=Email, password=pwd, rpassword=rpwd, phno=phone, dob=DoB, gender=Gender)
    x.save()
    return render(req,"reg.html",{'msg':'Registerd sucessfully'})

def login12(req):
    Name=req.POST.get('name')
    pwd=req.POST.get('pwds')
    ulist=empreg1.objects.all().values()
    uname_list=[]
    for i in ulist:
        uname_list.append(i['name'])
    if(Name in uname_list):
        Password=empreg1.objects.get(name=Name)
        if(Password.password==pwd):
             return render(req,'index1.html')
        else:
             return render(req,'admin.html',{'error':'Inccorect username or password'})
        
    else:
         return render(req,'admin.html',{'error':'Inccorect username or password'})
        


def bincard(req):
     erp=req.POST.get('erp')
     mp=req.POST.get('mp')
     st=req.POST.get('st')
     dv=req.POST.get('dv')
     rk=req.POST.get('rk')
     shelf=req.POST.get('shelf')
     binc=req.POST.get('binc')
     Date=req.POST.get('Date')
     pb=req.POST.get('pb')
     des=req.POST.get('des')
     re=req.POST.get('re')
     issue=req.POST.get('issue')
     sb=req.POST.get('sb')
     rdno=req.POST.get('rdno')
     rm=req.POST.get('rm')
     x=stockbin(ERP_NO=erp,MP_NO=mp,store=st,device=dv,rack=rk,shelf=shelf,bin_card=binc,date=Date,pb=pb,desc=des,no_received=re,no_issue=issue,sb=sb,rdno=rdno,remarks=rm,)
     x.save()
     return render(req,"addproduct.html",{'msg':'Added bin sucessfully'})

def viewdata(req):
     display=stockbin.objects.all()
     display1=display.values()
     uname_list=[]
     for i in display1:
        uname_list.append(i['sb'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab=sum(a)
             
     return render(req,'viewdata.html',{'dis':display1,'ab':ab})

def editdata(req,pk):
	data=stockbin.objects.get(id=pk)
	return render(req,'edit.html',{'data':data})


def editform(req):
     binid=req.POST.get('id')
     erp=req.POST.get('erp')
     mp=req.POST.get('mp')
     st=req.POST.get('st')
     dv=req.POST.get('dv')
     rk=req.POST.get('rk')
     shelf=req.POST.get('shelf')
     binc=req.POST.get('binc')
     Date=req.POST.get('Date')
     pb=req.POST.get('pb')
     des=req.POST.get('des')
     re=req.POST.get('re')
     issue=req.POST.get('issue')
     sb=req.POST.get('sb')
     rdno=req.POST.get('rdno')
     rm=req.POST.get('rm')
     x=stockbin.objects.get(id=binid)
     x.ERP_NO=erp
     x.MP_NO=mp
     x.store=st
     x.device=dv
     x.rack=rk
     x.shelf=shelf
     x.bin_card=binc
     x.date=Date
     x.pb=pb
     x.desc=des
     x.no_received=re
     x.no_issue=issue
     x.sb=sb
     x.rdno=rdno
     x.remarks=rm
     x.save()
     display=stockbin.objects.all()
     display1=display.values()
     uname_list=[]
     for i in display1:
        uname_list.append(i['sb'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab=sum(a)
     return render(req,'viewdata.html',{'dis':display1,'ab':ab})   

# def edelete(req,binid):
#      data1=stockbin.objects.get(id=binid)
#      data1.delete()
#      display=stockbin.objects.all()
#      display1=display.values()
#      return render(req,'viewdata.html',{'dis':display1})

def index1(req):
     return render(req,'index1.html')

def ClassicR2(req):
     return render(req,'ClassicR2.html')
def ClassicR3(req):
     return render(req,'ClassicR3.html')
def Classic6_4R2(req):
     return render(req,'Classic6.4R2.html')
def ClassicHDR2(req):
     return render(req,'ClassicHDR2.html')
def Classic6_4R3(req):
     return render(req,'Classic6.4R3.html')
def ClassicHDR3(req):
     return render(req,'ClassicHDR3.html')
def Aberro1(req):
     return render(req,'Aberro1.html')
def Aberro2(req):
     return render(req,'Aberro2.html')
def Flora1(req):
     return render(req,'Flora1.html')
def Flora2(req):
     return render(req,'Flora2.html')
def Neo1(req):
     return render(req,'Neo1.html')
def Neo2(req):
     return render(req,'Neo2.html')


def FG(req):
     y=additem.objects.get(id=1)
     y1=additem.objects.get(id=2)
     y2=additem.objects.get(id=3)
     y3=additem.objects.get(id=4)
     y4=additem.objects.get(id=5)
     y5=additem.objects.get(id=6)
     a=y.total
     g=y.pd
     a1=y1.total
     a2=y2.total
     a3=y3.total
     a4=y4.total
     a5=y5.total
     cd=datetime.now().strftime('%d-%m-%y')


     
     return render(req,'FG.html',{'y':a,'cd':cd,'gg':g,'y1':a1,'y2':a2,'y3':a3,'y4':a4,'y5':a5,'ya':y,'ya1':y1,'ya2':y2,'ya3':y3,'ya4':y4,'ya5':y5})

def addfg(req):
     a=req.POST.get('tid')
     c=req.POST.get('rm1')
     ym=req.POST.get('pbb')
     d=req.POST.get('Iss')
     e=req.POST.get('Rece')
     f=datetime.now().strftime('%d-%m-%y')
     g=req.POST.get('db')
     h=req.POST.get('pd')
     x=additem.objects.get(id=a)
     x.total=g
     i=x.name
     x.cd=f
     x.save()
     y=deviceitem(device_id=a, name=i,Remarks=c,Issued=d,Received=e,Current_Date=f,Previous_Date=h,Previous_Balance=ym,Device_Balance=g)
     y.save()
     return FG(req)

def recedit(req,pk1):
     data=stockbin.objects.get(id=pk1)
     return render(req,'addrec.html',{'data':data})

def recstockaad(req):
     binid=req.POST.get('id')
     erp=req.POST.get('erp')
     pb=req.POST.get('pb')
     re=req.POST.get('re')
     sb=req.POST.get('sb')
     rdno=req.POST.get('rdno')
     rm=req.POST.get('rm')
     x=stockbin.objects.get(id=binid)
     x.ERP_NO=erp
     x.pb=pb
     x.no_received=re
     x.sb=sb
     x.rdno=rdno
     x.remarks=rm
     x.save()
     display=stockbin.objects.all()
     display1=display.values()
     uname_list=[]
     for i in display1:
        uname_list.append(i['no_received'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab1=sum(a)
     return render(req,'recstock.html',{'rec1':display1,'ab1':ab1}) 
     


def recstock(req):
     display=stockbin.objects.all()
     display1=display.values()
     
     uname_list=[]
     for i in display1:
        uname_list.append(i['no_received'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab1=sum(a)
     return render(req,'recstock.html',{'rec1':display1,'ab1':ab1})  


def Issuededit(req,pk2):
	data=stockbin.objects.get(id=pk2)
	return render(req,'addissue.html',{'issue1':data})

def addissue(req):
     binid=req.POST.get('id')
     erp=req.POST.get('erp')
     issue=req.POST.get('no_issue')
     sb=req.POST.get('sb')
     rdno=req.POST.get('rdno')
     rm=req.POST.get('rm')
     x=stockbin.objects.get(id=binid)
     x.ERP_NO=erp
     x.no_issue=issue
     x.sb=sb
     x.rdno=rdno
     x.remarks=rm
     x.save()
     display=stockbin.objects.all()
     display1=display.values()
     uname_list=[]
     for i in display1:
        uname_list.append(i['no_issue'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab2=sum(a)
     return render(req,'Issued.html',{'issue1':display1,'ab2':ab2})
      
     


def Issued(req):
     display=stockbin.objects.all()
     display1=display.values()
     uname_list=[]
     for i in display1:
        uname_list.append(i['no_issue'])
     a=uname_list
     print(a)
     for i in range(0, len(a)):
          a[i] = int(a[i])
     ab2=sum(a)
     return render(req,'Issued.html',{'issue1':display1,'ab2':ab2}) 

# def stk(req):
#      x=store_room.objects.get(id=1)
     
#      print(x.str)
#      return render(req,'index.html')

def adbin(req,pk):
     x=store_room.objects.get(id=pk)
     return render(req,'addproduct.html',{'data':x})

def device_datalist(req):
     display=deviceitem.objects.all()
     display1=display.values()
     aa=additem.objects.get(id=1)
     ab=aa.total
     aa1=additem.objects.get(id=2)
     ab1=aa1.total
     aa2=additem.objects.get(id=3)
     ab2=aa2.total
     aa3=additem.objects.get(id=4)
     ab3=aa3.total
     aa4=additem.objects.get(id=5)
     ab4=aa4.total
     aa6=additem.objects.get(id=6)
     ab6=aa6.total
     return render(req,'device_datalist.html',{'dec':display1,'ab5':ab,'ab1':ab1,'ab2':ab2,'ab3':ab3,'ab4':ab4,'ab6':ab6}) 

def ddelete(req,did):
     data1=deviceitem.objects.get(id=did)
     data1.delete()
     display=deviceitem.objects.all()
     display1=display.values()
     return render(req,'device_datalist.html',{'dec':display1})
     
