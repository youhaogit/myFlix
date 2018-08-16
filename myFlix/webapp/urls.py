from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from webapp import views
from webapp.views import MoviesViewSet

router = routers.SimpleRouter()
router.register(r'webapp', MoviesViewSet, base_name='webapp')

urlpatterns = router.urls

urlpatterns += [
    path('', views.index, name='index'),
]

