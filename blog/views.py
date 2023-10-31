
# blog/views.py
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

def write_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BlogForm()

    return render(request, 'blog/write.html', {'form': form})


def view_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})
