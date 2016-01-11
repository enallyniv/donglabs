from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SubmitForm

"""
 For the main view we will just shit out the first page of the post list.
"""

def post_list_main(request):
    return post_list(request, 1)

"""
 Main page post list.
"""

def post_list(request, pagenumber):
    all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # Select everything...
    paginator = Paginator(all_posts, 5) # Show that many per page

    try:
        posts = paginator.page(pagenumber)
    except PageNotAnInteger:
        # if the page isn't an integer, just show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # show the last page if we go out of the limits
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/base_blog.html', {'posts': posts, 'paginator': paginator })

"""
 Single-post view, for viewing single posts!
"""

def view_single(request, postnumber):
    singlepost = get_object_or_404(Post, pk=postnumber)
    return render(request, 'blog/base_blog_single.html', {'singlepost': singlepost, })
 
"""
 Post page for posting things!
"""

def submit_post(request):
    if request.method == "POST":
        form = SubmitForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = SubmitForm()

    return render(request, 'blog/base_submit.html', {'form': form})

"""
 About page, which does precisely nothing interesting
"""
        
def about(request):
    return render(request, 'blog/base_about.html', {})
