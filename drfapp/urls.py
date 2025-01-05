from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', views.SnippetList.as_view(),name="snippet"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippetdetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
