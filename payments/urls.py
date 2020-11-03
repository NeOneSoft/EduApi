# Django
from django.conf.urls import url

# Views
from payments import views


urlpatterns = [
    url(r'^', views.PaymentView.as_view()),
]