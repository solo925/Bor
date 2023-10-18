from django.shortcuts import render,get_object_or_404
from . models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,\
    PageNotAnInteger
    
class PostListView(ListView):
    queryset=Post.published.all()
    context_object_name='posts'
    paginate_by= 3
    template_name='post/list.html'

def post_list(requests):
    posts = Post.published.all()
    paginator=Paginator(object_list,3)#3 posts in each page
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAninteger:
        #if page is not an integer deliver the first page
        posts=paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of result
        posta=paginator.page(paginator.num_pages)
        
    return render(requests,'post/list.html',{'posts':posts})

def post_details(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status ='published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    return render(request,'post/list.html',{'post':post})
    
    
