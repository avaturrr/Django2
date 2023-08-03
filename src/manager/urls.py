from django.urls import path

from manager.views import BookView, AddLike

urlpatterns = [
    path("", BookView.as_view()),
    path("add_like/<int:book_id>", AddLike.as_view(), name="add_like")
]
