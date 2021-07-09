from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blogs'
urlpatterns = [
    path('', views.BlogsView.as_view(), name='all'),
    path('blog/<str:slug>', views.BlogView.as_view(), name='blog'),
    path('edit', views.EditView.as_view(), name='edit'),
    path('blog/create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog_delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('authors/', views.AuthorView.as_view(), name='author_list'),
]

# path('', views.MainView.as_view(), name='all'),
# path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
# path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
# path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
# path('lookup/', views.MakeView.as_view(), name='make_list'),
# path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
# path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
# path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
