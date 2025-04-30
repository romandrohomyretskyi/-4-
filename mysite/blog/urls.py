from django.urls import path
from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

urlpatterns = [
    path('', HomePageView.as_view()),
    path('articles', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug>', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<year>/<month>/<day>/<slug>', ArticleDetail.as_view(), name='news-detail'),
]
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ← тут вказуємо blog
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
