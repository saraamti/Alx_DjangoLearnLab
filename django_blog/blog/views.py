from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  
from django.contrib.auth.forms import AuthenticationForm  
from django.urls import reverse_lazy  
from django.contrib.auth.decorators import login_required  
from .forms import PostForm, UserRegisterForm, CommentForm  
from .models import Post, Comment  

class PostListView(ListView):  
    model = Post  
    template_name = 'blog/post_list.html'  

class PostDetailView(DetailView):  
    model = Post  
    template_name = 'blog/post_detail.html'  

class PostCreateView(CreateView):  
    model = Post  
    form_class = PostForm  
    template_name = 'blog/post_form.html'  
    success_url = reverse_lazy('post-list')  

class PostUpdateView(UpdateView):  
    model = Post  
    form_class = PostForm  
    template_name = 'blog/post_form.html'  
    success_url = reverse_lazy('post-list')  

class PostDeleteView(DeleteView):  
    model = Post  
    template_name = 'blog/post_confirm_delete.html'  
    success_url = reverse_lazy('post-list')  

def register(request):  
    if request.method == 'POST':  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():  
            form.save()  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=password)  
            login(request, user)  
            return redirect('post-list')  
    else:  
        form = UserRegisterForm()  
    return render(request, 'blog/register.html', {'form': form})  
