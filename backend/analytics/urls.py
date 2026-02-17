from rest_framework.routers import DefaultRouter

from .views import MetricSnapshotViewSet

router = DefaultRouter()
router.register("metrics", MetricSnapshotViewSet)

urlpatterns = router.urls
