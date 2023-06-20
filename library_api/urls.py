from django.urls import path
from library_api import views


# URL patterns for the library_api views
urlpatterns = [
    # URL pattern for the BookList view
    path("library_api/", views.BookList.as_view()),
    # URL pattern for the BookDetail view with a dynamic integer parameter pk
    path("library_api/<int:pk>/", views.BookDetail.as_view()),
    # URL pattern for the UserTracker view
    path("tracker/", views.UserTracker.as_view()),
]
