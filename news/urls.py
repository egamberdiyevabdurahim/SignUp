from django.urls import path

from .views import create, edit, delete, opennews


urlpatterns = [

    path('create/', create, name='create'),
    path('edit/<int:id>', edit, name='edit'),
    path('delete/<int:id>', delete, name='delete'),
    path('opennews/<int:id>', opennews, name='opennews'),

]
