from django.conf.urls import url
from . import views

app_name = "calculator"

urlpatterns = [
    url(r'^$',views.CalcView.as_view(),name='calc'),
]
