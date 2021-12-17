from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.AddView,name='add_lap'),
    path('show/',views.ListView,name='show_lap'),
    path('update/<int:i>/',views.updateView,name='update'),
    path('delete/<int:i>/',views.deleteView,name='delete')
]
