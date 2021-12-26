from django.urls import path
from .views import SampleApiView, SampleDetail

urlpatterns = [
    path('', SampleApiView.as_view()),
    path('<int:id>/', SampleDetail.as_view()),
]
