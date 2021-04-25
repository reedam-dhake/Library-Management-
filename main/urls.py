from django.urls import path, include
from .views import HomeView, AddBookView, EditDetailView, DeleteBookView
from . import views
from django.conf.urls import url


urlpatterns = [
path('', views.bookListView, name='home'),
path('details/<int:pk>', views.book_detail, name = "book-detail"),
path('addBook/', AddBookView.as_view(), name = "add-book"),
path('details/<int:pk>/edit', EditDetailView.as_view(), name="edit-detail"),
path('details/<int:pk>/delete', DeleteBookView.as_view(), name='delete-book'),
path('book/<int:pk>/request_issue/', views.student_request_issue, name='request_issue'),
path('return/<int:pk>', views.return_book, name='return'),
path('extend/<int:pk>', views.extend_date, name='extend'),
path('student/<int:pk>', views.StudentDetail, name='student_detail'),
path('student/', views.StudentList, name='student_list'),
path('comments/<int:pk>/delete', views.comment_Delete, name='delete-comment'),
path('student/<int:pk>/makestaff', views.make_staff, name='make-staff'),
path('student/<int:pk>/unmakestaff', views.unmake_staff, name='unmake-staff'),
url(r'^search_b/', views.search_book, name="search_b"),
url(r'^search_s/', views.search_student, name="search_s"),
path('ratings/', include('star_ratings.urls', namespace='ratings')),
]