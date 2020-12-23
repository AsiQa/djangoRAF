from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    #url(r'^admin/', admin.site.urls),
    #path('about/', views.about),
    #path('', views.homepage),

    url(r'^products/', include('products.urls')),

    url(r'^about/$', views.about),
    url(r'^$', product_views.product_list),

]

urlpatterns += staticfiles_urlpatterns()
