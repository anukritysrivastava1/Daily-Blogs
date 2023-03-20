from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
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


def signup(request):
    if request.method == "POST":
        #parameters
        username=request.POST["username"]
        inputfname=request.POST["inputfname"]
        inputlname=request.POST["inputlname"]
        inputemail=request.POST["inputemail"]
        inputPassword1=request.POST["inputPassword1"]
        inputPassword2=request.POST["inputPassword2"]

        # Errors Messages

        # if len(username)<3:
        #     messages.error(request, "Your username should be more than 3 characters.")
        # if not username.isalnum():
        #     messages.error(request, "Your username should only contains alphabet and numbers.")

        if inputPassword1 != inputPassword2:
            messages.error(request, "Password do not match, Please your password and try again.")
            return redirect('home')
        

        # Creating user
        myuser=User.objects.create_user(username, inputemail, inputPassword1)
        myuser.first_name= inputfname
        myuser.last_name= inputlname
        myuser.save()
        messages.success(request, "Your account has been created successfully.")
        return redirect('home')
        
    else:
        return HttpResponse("ERROR - Please try again.")

def bloglogin(request):
    if request.method == "POST":
        #parameter for the post
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
    
        user=authenticate(username=loginusername, password=loginpassword)
        if user is None:
            messages.error(request, "Invalid credential, Please check and try again")
            return redirect("home")
    
        else:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
    return HttpResponse("404 - Page Not Found")



def bloglogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect("home")