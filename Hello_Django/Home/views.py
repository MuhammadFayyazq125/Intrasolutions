from django.shortcuts import render,HttpResponse
import pyrebase as pb

config = {
    "apiKey": "AIzaSyCR-9QE5bfx3Rn5NbQAlS_B-lLhALRKKBk",
    "authDomain": "djangofirebase-8656c.firebaseapp.com",
    "databaseURL": "https://djangofirebase-8656c-default-rtdb.firebaseio.com",

    "projectId": "djangofirebase-8656c",
    "storageBucket": "djangofirebase-8656c.appspot.com",
    "messagingSenderId": "484178472360",
    "appId": "1:484178472360:web:87747b6fb8b939bc83c19d"
}
firebase = pb.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def index(request):
    Uname = database.child("Data").child('Name').get().val()
    email = database.child("Data").child('email').get().val()
    password = database.child("Data").child('password').get().val()

    # return HttpResponse('This is Homepage')
    return render(request, 'index.html', {
        "Uname":Uname,
        'email':email,
        'password':password,
    })

def about(request):
    return HttpResponse('This is about page')

def Services(request):
    return HttpResponse('This is Services page')

def contact_us(request):
    return HttpResponse('This is contact us page')