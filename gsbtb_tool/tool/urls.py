from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'opportunities', views.OpportunityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url(r'^.*$', views.index, name='index'),
]
