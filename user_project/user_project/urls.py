from django.contrib import admin
from django.urls import path, include
from rest_framework import routers 
from django.views.generic import TemplateView
import os
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.views.user_viewset import UserViewSet
from users.views.post_viewset import PostViewSet
from users.views.comment_viewset import CommentViewSet
from users.views.album_viewset import AlbumViewSet
from users.views.photo_viewset import PhotoViewSet
from users.views.todo_viewset import TodoViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'todos', TodoViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="User Project API",
      default_version='v1',
      description="API documentation for User Project",
      contact=openapi.Contact(email="youremail@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Swagger / ReDoc yolları
    path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Vue frontend ana sayfası
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('<path:path>', TemplateView.as_view(template_name='index.html')),  # Tüm diğer pathleri index.html’e yönlendir
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))
