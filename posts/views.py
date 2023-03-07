from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks

def index(request):
    #If the method is POST
    if request.method == 'POST':
       form = PostForm(request.POST,request.FILES)
       # If the form is valid
       if form.is_valid():
       # Yes, Save
           form.save()
           # Redirect to home
           return HttpResponseRedirect('/')
          
       else:
           # No, Show Error
           return HttpResponseRedirect(form.erros.as_json())
    # Get all post, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    #Show
    return render(request, 'posts.html',
                  {'posts': posts})


def loadPictue(request):
    return render(request,'post/posts.html')


def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    #output = 'POST ID is ' + str(post_id)
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
        
    form = PostForm

    return render(request,'edit.html',{'post':post,'form':form})
   
#jkcjkdcdskjljlkkldn lds
 

        
def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')


            

