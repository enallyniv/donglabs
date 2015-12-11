from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# For the main view just shit out the first page because what else would you show?

def post_list_main(request):

    return post_list(request, 1)

# Try a paginated post list

def post_list(request, pagenumber):
    all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') # Select everything...
    paginator = Paginator(all_posts, 3) # Show that many per page

    try:
        posts = paginator.page(pagenumber)
    except PageNotAnInteger:
        # if the page isn't an integer, just show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # show the last page if we go out of the limits
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 'blog/base_blog.html', {'posts': posts, 'paginator': paginator })


# Post page

def submit_post(request):
    return render(request, 'blog/base_post.html', {})


# About page
        
def about(request):
    return render(request, 'blog/base_about.html', {})
