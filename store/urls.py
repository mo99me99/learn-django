from django.urls import path
from rest_framework.routers import SimpleRouter,DefaultRouter
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)



# URL configuration
urlpatterns = router.urls

# urlpatterns = [
    # path('',include(router.urls)) #using this approach you can add other specefic aptterns you wnat and still use router.urls
    # path('products/', views.ProductList.as_view()),
    # path('products/<int:pk>/', views.ProductDetail.as_view()),
    # path('collections/', views.CollectionList.as_view()),
    # path("collections/<int:pk>/", views.CollectionDetail.as_view(),name='collection-detail')
# ]