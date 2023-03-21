from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages


# Create your views here.
def blogpage(request):
    allposts=Post.objects.all()
    context={"allposts":allposts}
    return render(request, "blog/blogpage.html", context)
    # return render(request, "blog/blogpage.html")
    # return HttpResponse("This is a Blogpage. We will start posting soon so stay tuned")

def blogpost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post)
    context={"post":post, "comments":comments, "user":request.user}
    return render(request, "blog/blogpost.html", context)
    # return HttpResponse('This is BlogPOST: {slug}')


def postComment(request):
    
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        post=Post.objects.get(Sno=postSno)
        
        # parentsno=POST
        comment=BlogComment(comment=comment, user=user, post=post)

        comment.save()
        messages.success(request, "Your comment has been posted successfully")

    return redirect(f"/blog/blogpost/{post.slug}")