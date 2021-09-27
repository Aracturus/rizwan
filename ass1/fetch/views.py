from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render(request,'home.html',{'response':response})
