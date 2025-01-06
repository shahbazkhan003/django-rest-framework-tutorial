from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     # path('snippets/', views.snippet_list),
#     # path('snippets/<int:pk>/', views.snippet_detail),
#     path('snippets/', views.SnippetList.as_view(),name="snippet"),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippetdetail'),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
# ]

urlpatterns = format_suffix_patterns(urlpatterns) 
