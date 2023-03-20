from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post


# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is the Home Page")

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<10 or len(content)<10:
            messages.error(request, "Please fill the form properly.")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your response have been submitted.")
    # print(name, email, phone, content)
    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts=Post.objects.none()
    else:
        if Post.objects.filter(title__icontains=query):
            allposts=Post.objects.filter(title__icontains=query)
        elif Post.objects.filter(author__icontains=query):
            allposts=Post.objects.filter(author__icontains=query)
        else:
            allposts=Post.objects.filter(content__icontains=query)

    if allposts.count()==0:
        messages.warning(request,"No search result found. Please refine your query.")
    
    context={"allposts":allposts,
             "query": query}
    return render(request, "home/search.html", context)