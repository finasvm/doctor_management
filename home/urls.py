from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bookdoctos/',views.bookdoctos,name='bookdoctos'),
    path('doc/',views.doc,name='doc'),
    path('department/',views.department,name='department'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]