"""django_ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from crud_ajax.views import CreateCrudUser, CrudView, DeleteCrudUser, UpdateCrudUser, CallsView, CreateCall, DeleteCall, UpdateTrip, call_details

urlpatterns = [
    path('admin/', admin.site.urls),
    

    # Django Ajax CRUD Operations
    # path('', CrudView.as_view(), name='crud_ajax'),
    path('', include('allauth.urls')),
    path('ajax/crud/create/', CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('accounts/profile/', CallsView.as_view(), name='call_log'),
    path('ajax/trip/create/', CreateCall.as_view(), name='trip_ajax_create'),
    path('ajax/trip/delete/', DeleteCall.as_view(), name='trip_ajax_delete'),
    path('ajax/trip/update/', UpdateTrip.as_view(), name='trip_ajax_update'),

    url(r'^call-details/(?P<id>.*)$', call_details, name='call-details'),

    

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
