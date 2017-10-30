from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import HelloAPIView, HelloViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    url(r'^hello-view/$', HelloAPIView.as_view()),
    url(r'', include(router.urls))
]
