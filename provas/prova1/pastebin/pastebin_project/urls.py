from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questao<int:i>/', views.question_view),
    path('', include('pastebin.urls')),
]

urlpatterns.extend(
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
