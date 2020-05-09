from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name="hello-viewset")
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
  path('',include(router.urls)),
  path('login/', views.UserLoginView.as_view()),
  path('hello-view',views.HelloApiView.as_view())
  # noneed to metion the basename as the UserProfileViewSet already knows of the basename with the 
  # help of the queryset in the Viewset for the UserProfileViewSet
]

