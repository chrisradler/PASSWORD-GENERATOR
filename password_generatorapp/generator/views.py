from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    #this is to link the home webpage to our template. home.html
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
#creating a character list
    characters = list('abcdefghijklmnopqrstuvwvyz')
#checking to see if the user wants uppercase letters, numbers or special characters. we extended the list accordingly
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('@#^*#$^&%*#@&()#@'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

#this line below is grabbing the length dropdown for home.html. The neame of the dropdown is length
    length = int(request.GET.get('length'))
# an open list for the new generated password
    thepassword = ''
#for loop to generate a random password from the characters list above
    for x in range(length):
        thepassword += random.choice(characters)
#this is to link the password webpage to our template. password.html
    return render(request, 'generator/password.html', {'password':thepassword})

