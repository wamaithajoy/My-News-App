from django.shortcuts import render
import requests


def home(request):
    return render(request, 'index.html')

def politics(request):
    url=" https://newsapi.org/v2/everything?q=politics&from=2022-10-16&sortBy=popularity&apiKey=cdb1b330651a4d97b4b26c59e1d1c590"
    politics_news=requests.get(url).json()
    a=politics_news['articles']
    desc=[]
    title=[]
    img=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    return render(request,'politics.html',context)

def sports(request):
    url=" https://newsapi.org/v2/everything?q=sports&from=2022-10-16&sortBy=popularity&apiKey=cdb1b330651a4d97b4b26c59e1d1c590"
    sports_news=requests.get(url).json()
    a=sports_news['articles']
    desc=[]
    title=[]
    img=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    return render(request,'sports.html',context) 

def education(request):
    url=" https://newsapi.org/v2/everything?q=education&from=2022-10-16&sortBy=popularity&apiKey=cdb1b330651a4d97b4b26c59e1d1c590"
    education_news=requests.get(url).json()
    a=education_news['articles']
    desc=[]
    title=[]
    img=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    return render(request,'education.html',context)  

def travel(request):
    url=" https://newsapi.org/v2/everything?q=travel&from=2022-10-16&sortBy=popularity&apiKey=cdb1b330651a4d97b4b26c59e1d1c590"
    travel_news=requests.get(url).json()
    a=travel_news['articles']
    desc=[]
    title=[]
    img=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    return render(request,'travel.html',context) 

def health(request):
    url=" https://newsapi.org/v2/everything?q=property&from=2022-10-16&sortBy=popularity&apiKey=cdb1b330651a4d97b4b26c59e1d1c590"
    health_news=requests.get(url).json()
    a=health_news['articles']
    desc=[]
    title=[]
    img=[]

    for i in range(len(a)):
        f=a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist=zip(title,desc,img)
    context={'mylist':mylist}
    return render(request,'health.html',context)           








# Create your views here.
