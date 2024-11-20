from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'about_mes', views.AboutMeViewSet)

# Wire up your API using automatic URL routing.
# Additionally, you include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]