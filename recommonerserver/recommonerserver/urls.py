"""recommonerserver URL Configuration"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from recommoner.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'bio', 'organization')


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^recom/', include('recommoner.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
