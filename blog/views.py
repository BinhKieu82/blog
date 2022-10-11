from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CommentForm, PostForm, UpdatePostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# class PostList(generic.ListView):
#   queryset = Post.objects.filter(status=1).order_by('-created_on')
#   template_name = 'index.html'
#   paginate_by = 3

# class CreateArticle(generic.CreateView):
#   model = Post
#   form_class = PostForm
#   template_name = 'article_create.html'

def about(request):
  return render(request, 'about.html', {})

def policy(request):
  return render(request, 'policy.html', {})

def contact(request):
  return render(request, 'contact.html', {})

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
  return render(request, 'index.html', {'page': page, 'post_list': post_list})

def post_detail(request, slug):
  template_name = 'post_detail.html'
  post = get_object_or_404(Post, slug=slug)
  comments = post.comments.filter(active=True).order_by('-created_on')  
  new_comment = None
  
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
      messages.success(request, 'Your comment is awaiting moderation - thank you!')
  else:
    comment_form = CommentForm()  
  return render(request, template_name, {
    'post': post,
    'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form
  })

# @login_required(login_url="/accounts/login/") #if user login
def article_create(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES) #validate textfields & media field
    if form.is_valid():
      #save article to db
      instance = form.save(commit=False) #dont commit, will saved soon
      instance.author = request.user
      instance.save() #save with author
      return redirect('blog:home')
  else:
    form = PostForm()
  return render(request, 'article_create.html', {'form': form})

# def article_update(request, slug):  
#   post = get_object_or_404(Post, slug=slug)
#   if request.method == 'POST':
#     form = UpdatePostForm(request.POST, request.FILES) #validate textfields & media field
#     if form.is_valid():
#       #save article to db
#       instance = form.save(commit=True) #dont commit, will saved soon
#       # instance.author = request.user
#       instance.save() #save with author
#       return redirect('blog:home')
#   else:
#     form = UpdatePostForm()
#   return render(request, 'post_update.html', {'form': form, 'post': post})

class UpdateArticle(generic.UpdateView):
  model = Post
  template_name = 'post_update.html'
  fields = ['title', 'slug', 'content']
  
class DeleteArticle(generic.DeleteView):
  model = Post
  template_name = 'post_delete.html'
  success_url = reverse_lazy('blog:home')
  