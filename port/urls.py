
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
import amine.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home,name='home'),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
