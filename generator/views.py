from django.shortcuts import render
from django.http import HttpResponse
import random
import pandas as pd
import numpy as np
book1 = pd.read_excel(r"C:\\Users\\varun\\Book1.xlsx")

book2 = pd.read_excel(r"C:\\Users\\varun\\Book2.xlsx")
# Create your views here.

def home(request):
     return render(request,'generator/home.html',{'password':'wesgrd3465654'})
def generatepassword(request):
     return render(request,'generator/random_password_homepage.html')
     
def pizza(request):
     return HttpResponse("<h1>I love Pizza</h1>")
def about(request):
     return render(request,'generator/about.html')
def fetchdetails(request):
    j = int(request.GET.get('id'))
    for i in range(0,4):
        try:
            if j == book1['ID'][i]:
                np.append(book1.iloc[i],book2.iloc[i][1:])
                return render(request,'generator/employee_details.html',{'employeedetails': np.append(book1.iloc[i],book2.iloc[i][1:]) })
            else:
                return render(request,'generator/errorpage.html',{'errorpage': "Can't find the employee Id asked for, please enter correctly" })
        except:
            return render(request,'generator/errorpage.html',{'errorpage': "Can't find the employee Id asked for, please enter correctly" })
               
            
def password(request):
    charecters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specials'):
        charecters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        charecters.extend(list('12355675686789'))
    if request.GET.get('lowercase'):
        charecters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    length = int(request.GET.get('length'))
    #id_value = book1['ID'][0]
    thepassword = ""
    #id_value=id_value+identity.append(book1['ID'][0])
    for i in range(0,length):
        thepassword+=random.choice(charecters)
    return render(request,'generator/password.html',{'password': thepassword })
    
   