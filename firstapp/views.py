import requests
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models.product import Product
from .models.recomend import Recomendation
from .models.review import Review
from .models.rcolab import Rcolabb
from . import mlmodel
from . import mlmlmodel
import csv
# Create your views here.

prodlist=['username','iphone13promax','iphone12promax','iphone11pro','iphoneSE','iphoneX','SamsungGalaxyA52','SamsungGalaxyS20','SamsungGalaxyM32','SamsungGalaxyM12','SamsungGalaxyF22','Oneplus10pro','Oneplus9R','OneplusNord','Oneplus8T','Oneplus7','Redminote11','Redminote10','Redmi9A','Redmi8A','Redmi7A','DellVostro','DellInspiron','HpRyzen','HpEnvy','Applemacbookair','Applemacbookpro','ASUSzenbook','Asusvivobook','Lenevoideapadslim5','Lenevoideapadslim3','Samsungrefrigerator','Haierrefrigerator','Whirpoolrefrigerator','Amazonbasicrefrigerator','LGrefrigerator','BlustarAC','SamsungAC','HaierAC','WhirpoolAC','AmazonbasicAC','HavellsTrimmer','NovaTrimmer','SYSKATrimmer','PhilipsTrimmer','MITrimmer','AppleAirpods','OneplusBuds','NoiseAirbuds','boatairdopes','Jblairbuds','OneplusTv','LGTv','SonyTv','SamsungTv','RedmiTv','SonySoundbar','PanasonicSpeaker','Philipsspeaker','Zebronicssubwoofer','Ahujaspeaker','Boatsmartwatch','Firebolttsmartwatch','Marviksmartwatch','Noisesmartwatch','Genericsmartwatch','Applesmartwatch','Mismartwatch','Fitbitsmartwatch','Amazfitsmartwatch','Oneplussmartwatch']

class Name:
    object = None
    us=""
    def set(self,name):
        self.us = name

    def get(self):
        return self.us


n = Name()

objectslist=[]

def fun(name):
    print(objectslist)
    if name not in objectslist:
        objectslist.append(name)
        for i in objectslist:
            if i == name:
                n.set(i)
                i = Rcolabb()
                n.object = i
    else:
        for i in objectslist:
            if i == name:
                n.set(i)
                i = Rcolabb()
                n.object = i

def home(request):
    return render(request,'home.html')

def e1view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)

    smproducts = mlmlmodel.similar_prod("iphone13promax",5)

    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,iphone13promax=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e1.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e1.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e2view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)

    smproducts = mlmlmodel.similar_prod("SamsungGalaxyA52",5)

    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,SamsungGalaxyA52=i).exists()
        print(bool)
        if bool:
            break

    if bool :
        return render(request,'e2.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e2.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e3view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)

    smproducts = mlmlmodel.similar_prod("Oneplus10pro",5)

    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()

    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Oneplus10pro=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e3.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e3.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e4view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)

    smproducts = mlmlmodel.similar_prod("Redminote11",5)

    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()



    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Redminote11=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e4.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e4.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e5view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("DellVostro",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,DellVostro=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e5.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e5.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e6view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("HpRyzen",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()



    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,HpRyzen=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e6.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e6.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e7view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("Applemacbookair",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()



    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Applemacbookair=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e7.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e7.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e8view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("ASUSzenbook",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,ASUSzenbook=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e8.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e8.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})


def e9view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("Samsungrefrigerator",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()

    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Samsungrefrigerator=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e9.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e9.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e10view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("BlustarAC",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,BlustarAC=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e10.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e10.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e11view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("HavellsTrimmer",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()

    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,HavellsTrimmer=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e11.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e11.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e12view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("AppleAirpods",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,AppleAirpods=i).exists()
        if bool==True:
            break

    if bool :
        return render(request,'e12.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e12.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e13view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("OneplusTv",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,OneplusTv=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e13.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e13.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e14view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("Amazfitsmartwatch",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Amazfitsmartwatch=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e14.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e14.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e15view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("Philipsspeaker",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Philipsspeaker=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e15.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e15.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def e16view(request,id):
    prod_index=id-1

    ids = mlmodel.recommendphoto(prod_index)

    products = Recomendation.get_productpics_by_id(ids)
    smproducts = mlmlmodel.similar_prod("Boatsmartwatch",5)
    p = mlmodel.returnname(prod_index)
    k=p.split()
    t=""
    for i in range(len(k)):
        t+=k[i]
    p = t
    print(t)
    val_username = n.get()


    for i in range(1,6):
        bool  = Rcolabb.objects.filter(username=val_username,Boatsmartwatch=i).exists()
        if bool==True:
            break


    if bool :
        return render(request,'e16.html',{'rids':products,'smproducts':smproducts,'bool':"Your rating is submitted"})
    else:
        return render(request,'e16.html',{'rids':products,'smproducts':smproducts,'bool':"Rate now",'d':[bool]})

def cartview(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart']={}
    ids=(list(request.session.get('cart').keys()))
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request,'cart.html',{'products':products})

def userhomeview(request):
    return render(request,'user.html')

def loginview(request):
    return render(request,'login.html')

def signupview(request):
    return render(request,'signup.html')

def clothview(request):
    return render(request,'clothing.html')

def grocview(request):
    return render(request,'groc.html')

def elecview(request):
    return render(request,'elec.html')


def clothuserview(request):
    return render(request,'clothing2.html')

def grocuserview(request):
    return render(request,'groc2.html')

def elecuserview(request):
    context = Product.objects.all()
    return render(request,'elec2.html',{"context":context})

def contactview(request):
    return render(request,'contact.html')
def aboutview(request):
    return render(request,'about.html')
def helpview(request):
    return render(request,'help.html')
def termsview(request):
    return render(request,'terms.html')

def helpresultview(request):
    return render(request,'helpresult.html')

def contactviewu(request):
    return render(request,'usercontact.html')
def aboutviewu(request):
    return render(request,'userabout.html')
def helpviewu(request):
    return render(request,'userhelp.html')
def termsviewu(request):
    return render(request,'userterms.html')


def registerview(request):
    if request.method=='POST':
        val_email=request.POST['email']
        val_username=request.POST['username']
        val_password1=request.POST['password1']
        val_password2=request.POST['password2']
        if (val_password1==val_password2):
            if User.objects.filter(username=val_username).exists():
                messages.info(request,'Username Taken')
            elif User.objects.filter(email=val_email).exists():
                messages.info(request,'Email Taken')
            else:
                user=User.objects.create_user(username=val_username,password=val_password1,email=val_email)
                user.save();
                messages.info(request,'User  Created')
                return redirect('login')
        else:
            messages.info(request,'User not created')
        return render(request,'signup.html')

    else:
        return render(request,'signup.html')

def loginpageview(request):
    if request.method=='POST':
        val_username=request.POST['username']
        val_password=request.POST['password']

        user=auth.authenticate(username=val_username,password=val_password)

        if user is not None:
            #o.username=val_username
            fun(val_username)

            n.object.username=val_username
            auth.login(request,user)
            request.session['user']=user.username
            return redirect("userhome")
            print(request.session.get('user'))

        else:
            messages.info(request,'Incorrect credentials')
            return redirect('login')

    else:
        return render(request,'signup.html')

def logoutmypageview(request):
    auth.logout(request)
    return redirect('login')

def addtocartview(request):
    pro=request.POST['pro_id']
    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'clothing2.html')


def removefromcartview(request):
    pro=request.POST['pro_id']
    rem=request.POST['minus']

    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            if rem:
                if quantity <= 1 :
                    cart.pop(pro)
                else:
                    cart[pro] = quantity - 1
            else:
                cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'clothing2.html')


def addtocartviewg(request):
    pro=request.POST['pro_id']
    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'groc2.html')


def removefromcartviewg(request):
    pro=request.POST['pro_id']
    rem=request.POST['minus']

    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            if rem:
                if quantity <= 1 :
                    cart.pop(pro)
                else:
                    cart[pro] = quantity - 1
            else:
                cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'groc2.html')


def addtocartviewe(request):
    pro=request.POST['pro_id']
    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'elec2.html')


def removefromcartviewe(request):
    pro=request.POST['pro_id']
    rem=request.POST['minus']

    cart = request.session.get('cart')

    if cart:
        quantity = cart.get(pro)
        if quantity :
            if rem:
                if quantity <= 1 :
                    cart.pop(pro)
                else:
                    cart[pro] = quantity - 1
            else:
                cart[pro] = quantity + 1
        else:
            cart[pro] = 1
    else:
        cart={}
        cart[pro] = 1

    request.session['cart']=cart
    print(request.session['cart'])
    return render(request,'elec2.html')


def ratnowviewe1(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']

        n.object.iphone13promax=val_rating
        n.object.save()

    return  redirect('elec2')

def ratnowviewe2(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']

        n.object.SamsungGalaxyA52=val_rating
        n.object.save()

    return  redirect('elec2')


def ratnowviewe3(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']

        n.object.Oneplus10pro=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe4(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']

        n.object.Redminote11=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe5(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.DellVostro=val_rating
        n.object.save()
    return  redirect('elec2')


def ratnowviewe6(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.HpRyzen=val_rating
        n.object.save()

    return  redirect('elec2')


def ratnowviewe7(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.Applemacbookair=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe8(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.ASUSzenbook=val_rating
        n.object.save()

    return  redirect('elec2')


def ratnowviewe9(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.Samsungrefrigerator=val_rating
        n.object.save()

    return  redirect('elec2')


def ratnowviewe10(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.BlustarAC=val_rating
        n.object.save()


    return  redirect('elec2')

def ratnowviewe11(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.HavellsTrimmer=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe12(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.AppleAirpods=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe13(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.OneplusTv=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe14(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.Amazfitsmartwatch=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe15(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.Philipsspeaker=val_rating
        n.object.save()


    return  redirect('elec2')


def ratnowviewe16(request):
    if request.method=='POST':
        val_rating=request.POST['rating']
        val_username=request.POST['rusername']
        val_prodcutname=request.POST['productname']
        n.object.Boatsmartwatch=val_rating
        n.object.save()

    return  redirect('elec2')

def exportview(request):
    review = Rcolabb.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=d_export.csv'
    writer = csv.writer(response)
    writer.writerow(['username','iphone13promax','iphone12promax','iphone11pro','iphoneSE','iphoneX','SamsungGalaxyA52','SamsungGalaxyS20','SamsungGalaxyM32','SamsungGalaxyM12','SamsungGalaxyF22','Oneplus10pro','Oneplus9R','OneplusNord','Oneplus8T','Oneplus7','Redminote11','Redminote10','Redmi9A','Redmi8A','Redmi7A','DellVostro','DellInspiron','HpRyzen','HpEnvy','Applemacbookair','Applemacbookpro','ASUSzenbook','Asusvivobook','Lenevoideapadslim5','Lenevoideapadslim3','Samsungrefrigerator','Haierrefrigerator','Whirpoolrefrigerator','Amazonbasicrefrigerator','LGrefrigerator','BlustarAC','SamsungAC','HaierAC','WhirpoolAC','AmazonbasicAC','HavellsTrimmer','NovaTrimmer','SYSKATrimmer','PhilipsTrimmer','MITrimmer','AppleAirpods','OneplusBuds','NoiseAirbuds','boatairdopes','Jblairbuds','OneplusTv','LGTv','SonyTv','SamsungTv','RedmiTv','SonySoundbar','PanasonicSpeaker','Philipsspeaker','Zebronicssubwoofer','Ahujaspeaker','Boatsmartwatch','Firebolttsmartwatch','Marviksmartwatch','Noisesmartwatch','Genericsmartwatch','Applesmartwatch','Mismartwatch','Fitbitsmartwatch','Amazfitsmartwatch','Oneplussmartwatch'])

    review_feilds=review.values_list('username','iphone13promax','iphone12promax','iphone11pro','iphoneSE','iphoneX','SamsungGalaxyA52','SamsungGalaxyS20','SamsungGalaxyM32','SamsungGalaxyM12','SamsungGalaxyF22','Oneplus10pro','Oneplus9R','OneplusNord','Oneplus8T','Oneplus7','Redminote11','Redminote10','Redmi9A','Redmi8A','Redmi7A','DellVostro','DellInspiron','HpRyzen','HpEnvy','Applemacbookair','Applemacbookpro','ASUSzenbook','Asusvivobook','Lenevoideapadslim5','Lenevoideapadslim3','Samsungrefrigerator','Haierrefrigerator','Whirpoolrefrigerator','Amazonbasicrefrigerator','LGrefrigerator','BlustarAC','SamsungAC','HaierAC','WhirpoolAC','AmazonbasicAC','HavellsTrimmer','NovaTrimmer','SYSKATrimmer','PhilipsTrimmer','MITrimmer','AppleAirpods','OneplusBuds','NoiseAirbuds','boatairdopes','Jblairbuds','OneplusTv','LGTv','SonyTv','SamsungTv','RedmiTv','SonySoundbar','PanasonicSpeaker','Philipsspeaker','Zebronicssubwoofer','Ahujaspeaker','Boatsmartwatch','Firebolttsmartwatch','Marviksmartwatch','Noisesmartwatch','Genericsmartwatch','Applesmartwatch','Mismartwatch','Fitbitsmartwatch','Amazfitsmartwatch','Oneplussmartwatch')
    for i in review_feilds:
        writer.writerow(i)

    return response

"""
def fun(name):
    print(objectslist)
    if name not in objectslist:
        objectslist.append(name)
        for i in objectslist:
            if i == name:
                n.set(i)
                i = Rcolabb()
                n.object = i
    else:
        for i in objectslist:
            if i == name:
                n.set(i)
                i = Rcolabb()
                n.object = i
"""
