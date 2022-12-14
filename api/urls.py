from rest_framework.routers import DefaultRouter
from api.views import UserViewSet


app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)

urlpatterns = router.urls