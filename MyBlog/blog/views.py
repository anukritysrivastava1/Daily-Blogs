from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogpage(request):
    allposts=Post.objects.all()
    
    context={"allposts":allposts}
    return render(request, "blog/blogpage.html", context)
    # return render(request, "blog/blogpage.html")
    # return HttpResponse("This is a Blogpage. We will start posting soon so stay tuned")

def blogpost(request):
    return render(request, "blog/blogpost.html")
    # return HttpResponse('This is BlogPOST: {slug}')