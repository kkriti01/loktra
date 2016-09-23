from django.conf.urls import url
from django.contrib import admin

from webscrapper import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.HomeView.as_view(), name="home"),
]
