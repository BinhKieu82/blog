from django.views import generic
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# class PostList(generic.ListView):
#   queryset = Post.objects.filter(status=1).order_by('-created_on')
#   template_name = 'index.html'
#   paginate_by = 3

def post_list(request):
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})

def post_detail(request, slug):
  template_name = 'post_detail.html'
  post = get_object_or_404(Post, slug=slug)
  comments = post.comments.filter(active=True).order_by('-created_on')
  # page = request.GET.get('page', 1)
  # paginator = Paginator(comments, 5)
  new_comment = None
  # try:
  #   comments_list = paginator.page(page)
  # except PageNotAnInteger:
  #   comments_list = paginator.page(1)
  # except EmptyPage:
  #   comments_list = paginator.page(paginator.num_pages)
  # Comment posted
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
      # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
      # Assign the current post to the comment
      new_comment.post = post
      # Save the comment to the database
      new_comment.save()
      # return redirect('blog:home')
  else:
    comment_form = CommentForm()
  return render(request, template_name, {
    'post': post,
    'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form
    # 'comments_list': comments_list
  })