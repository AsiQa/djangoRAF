from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'products'

urlpatterns = [

    #url(r'^admin/', admin.site.urls),
    #path('about/', views.about),
    #path('', views.homepage),

    url(r'^$', views.product_list, name="list"),
    url(r'^add/$', views.product_add, name="add"),
    #url(r'^(?P<slug>[\w-]+)/$', views.product_detail),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.product_detail),
    path('<slug:slug>/', views.product_detail, name="detail"),
]
