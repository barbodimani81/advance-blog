from django.urls import path
from django.views.generic.base import RedirectView

from .views import SampleView, RedirectToGoogle, PostListView, PostDetailView, PostCreateView, PostEditView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('cbv/', SampleView.as_view(), name='cbv'),
    path('google/', RedirectToGoogle.as_view(), name='google'),
    path('posts/', PostListView.as_view(), name='post_detail.html-list-view'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail.html-detail-view'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
