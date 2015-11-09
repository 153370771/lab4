from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from models import book,author
import MySQLdb
from django import forms

# Create your views here.
def index(request):
    return render_to_response('index.html')
    
def sear(request):
    return render_to_response('sear.html')

def showall(request):
    book_lst = book.objects.all()
    if book_lst[0].ISBN>0:
        return render_to_response('showall.html',{'book_lst':book_lst})
    else:
        return render_to_response('index.html')

def search(request):
    if request.POST:
		author_lst = author.objects.filter(name__contains = request.POST['authorname'])[0]
		print author_lst.authorid
		book_lst = book.objects.filter(authorid__contains = author_lst.authorid)
		return render_to_response('search.html',{'book_lst': book_lst})
    else:
		return render_to_response('sear.html')
    
def images(request):
    return HttpResponse(open('images/'+request.GET['id'],'rb'),mimetype='image/jpeg')

def add(request):
    return render_to_response('add.html')

def addbook(request):
    if request.POST:
        post=request.POST
        authorid=post['authorid']
        multiple_book = book(ISBN = post['ISBN'],title = post['title'],authorid = authorid, publisher=post['publisher'],publishdate=post['publishdate'],
                             price=post['price'])
        multiple_book.save()
        try:
            author_lst = author.objects.filter(authorid__contains = authorid)
            if author_lst:
                return render_to_response('index.html')
            else:
                return render_to_response('authoradd.html',{'authorid':authorid})
        except:
            return render_to_response('authoradd.html',{'authorid':authorid})
    else:
        return render_to_response('add.html')

def delete(request):
    if 'id' in request.GET:
        n_book_lst = book.objects.filter(title = request.GET['id'])
        n_book_lst.delete()
    book_lst = book.objects.all()
    return render_to_response('showall.html',{'book':book_lst})

def update(request):
    if 'id' in request.GET:
        book_lst = book.objects.get(title = request.GET['id'])
    if request.POST:
        post = request.POST
        authorid = post['authorid']
        book_lst=book.objects.filter(authorid=authorid)
        ISBN=book_lst[0].ISBN
        title=book_lst[0].title
        book_lst = book(ISBN,title,authorid, publisher=post['publisher'],publishdate=post['publishdate'],price=request.POST['price'])
        book_lst.save()
        book_lst=book.objects.all()
        try:
           author_lst = author.objects.filter(authorid__contains = authorid) 
           if author_lst:
               return render_to_response('index.html')
           else:
               return render_to_response('authoradd.html',{'authorid':authorid})
        except:
            return render_to_response('authoradd.html',{'authorid':authorid})
    return render_to_response('update.html',{'book':book_lst})
def authoradd(request):
    if request.POST:
        author_lst=author(authorid=request.POST['authorid'],name=request.POST['name'],age=request.POST['age'],country=request.POST['country'])
        author_lst.save()
        
        return render_to_response('authoradd.html')
    else:
        return render_to_response('index.html')
    
def showdata(request):
    if 'id' in request.GET:
        book_lst = book.objects.get(title = request.GET['id'])
        author_lst = author.objects.get(authorid = book_lst.authorid)
        return render_to_response('showdata.html',{'book':book_lst,'author':author_lst})

