from django.urls import path
from .import views
app_name = 'blog'

urlpatterns = [
    #path('',views.post_list,name = 'post_list'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:Post>/',views.post_details,name = 'post_detal')
]
