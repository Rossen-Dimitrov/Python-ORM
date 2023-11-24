from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('create-category/', views.create_category, name='category create page'),
    path('dashboard/', views.dashboard, name='dashboard page'),
    path('create/', views.fruit_create, name='fruit create page'),
    path('<int:fruit_pk>/', include([
        path('edit/', views.edit_details, name='fruit edit page'),
        path('details/', views.fruit_details, name='fruit details page'),
        path('delete/', views.delete_details, name='fruit delete page'),
    ])),

]
