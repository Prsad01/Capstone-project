from django.urls import path,include
from .views import index , UserView,MenuView, BookingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('users',UserView,basename='user')
router.register('booking/tables',BookingView, basename='tables')
router.register('menu-item',MenuView, basename='menu')

urlpatterns = [

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]+router.urls
