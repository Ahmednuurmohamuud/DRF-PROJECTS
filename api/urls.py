from django.urls import path ,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeesViewSet, basename='employees')

urlpatterns = [
    path('students/', views.studentsView),  # GET all students or POST a new student
    path('students/<int:pk>/', views.studentDetail),  # GET, PUT, DELETE a specific student by ID

    # path('employees/', views.Employees.as_view()),  # GET all employees or POST a new employee
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),  # GET, PUT, DELETE a specific employee by ID
    path('', include(router.urls)),  # Include the router URLs for EmployeeViewSet


    path('blogs/', views.BlogListView.as_view()),  # GET all blogs or POST a new blog
    path('comments/', views.CommentListView.as_view()),  # GET all comments or POST a new comment

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),  # GET, PUT, DELETE a specific blog by ID
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),  #
]
