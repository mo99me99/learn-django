from django.urls import path
from . import views


# URL configuration
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('collections/', views.collection_list),
    path("collections/<int:pk>/", views.collection_detail,name='collection-detail')
]