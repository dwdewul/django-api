from django.conf.urls import url
from .views import HelloAPIView

urlpatterns = [
    url(r'^hello-view/$', HelloAPIView.as_view()),
]
