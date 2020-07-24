from django.urls import path
from .views import index,cadastro,upload_file_view


urlpatterns = [
    # path('',index, name='index'),
    path('cadastro/',cadastro,name='cadastro'),
    path('',upload_file_view, name='upload-view'),

]