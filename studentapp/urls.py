from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_details/', views.add_details, name='add_details'),
    path('student_showpage',views.student_showpage,name='student_showpage'),
    path('product_editpage/<int:pk>',views.product_editpage,name='product_editpage'),
    path('edit_product_details/<int:pk>',views.edit_product_details,name='edit_product_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
   
]