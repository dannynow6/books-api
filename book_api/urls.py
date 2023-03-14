from book_api.views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter
from book_api import views

router = DefaultRouter()
router.register(r"books", views.BookViewSet, basename="book")
router.register(r"authors", views.AuthorViewSet, basename="author")
urlpatterns = router.urls
