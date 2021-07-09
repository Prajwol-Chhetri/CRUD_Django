from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blogs.models import Author, Blog


# Create your views here.
class BlogsView(View):
    def get(self, request):
        ac = Author.objects.all().count()
        bl = Blog.objects.all()
        ctx = {'author_count': ac, 'blogs_list': bl}
        return render(request, 'blogs/blogs.html', ctx)


class EditView(LoginRequiredMixin, View):
    def get(self, request):
        ac = Author.objects.all().count()
        bl = Blog.objects.all()
        ctx = {'author_count': ac, 'blogs_list': bl}
        return render(request, 'blogs/edit_blog_list.html', ctx)


class BlogView(View):
    def get(self, request,  *args, **kwargs):
        slug = kwargs['slug']
        b = Blog.objects.filter(slug=slug).first()
        ctx = {'blog': b}
        return render(request, 'blogs/blog.html', ctx)


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = '__all__'
    success_url = reverse_lazy('blogs:all')


class AuthorView(LoginRequiredMixin, View):
    def get(self, request):
        al = Author.objects.all()
        ctx = {'author_list': al}
        return render(request, 'blogs/author_list.html', ctx)