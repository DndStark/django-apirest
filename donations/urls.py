from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from donation import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonView, 'person')
router.register(r'donations', views.DonationView, 'donation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
