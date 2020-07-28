from django.contrib import admin
from django.urls import path
import CBV.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CBV.views.index.as_view(), name='index'),
    path('detail/<pk>', CBV.views.detail.as_view(), name='detail'),
    path('delete/<pk>',CBV.views.delete.as_view(), name='delete'),
    path('update/<pk>',CBV.views.update.as_view(), name='update'),
    path('create/',CBV.views.create.as_view(), name='create'),
    path('result/',CBV.views.result, name='result'),

]
