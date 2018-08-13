from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from webapp import views
from webapp.views import MovieViewSet

router = routers.SimpleRouter()
router.register(r'', MovieViewSet, base_name='webapp')

urlpatterns = router.urls
# urlpatterns = [
#     path('', views.index, name='index'),
# ]