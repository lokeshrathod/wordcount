from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['text']
    Word_count = fulltext.split()
    Word_dict = {}
    for word in Word_count:
        if word in Word_dict:
            Word_dict[word] += 1
        else:
            Word_dict[word] = 1
    return render(request,'count.html',{'fulltext':fulltext,'wordcount':len(Word_count),"Word_dict":Word_dict})