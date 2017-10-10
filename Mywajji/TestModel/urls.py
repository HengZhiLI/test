from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^(\d+)$', views.aaa),
    url(r'^TestGet1/$', views.TestGet1),
    url(r'^TestGet2/$', views.TestGet2),
    url(r'^TestGet3/$', views.TestGet3),
    url(r'^TestPost1/$', views.TestPost1),
    url(r'^TestPost2/$', views.TestPost2),

]

