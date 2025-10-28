from django.shortcuts import render ,get_list_or_404
# from django.http import JsonResponse
from students.models import student
from .serializers import StudentSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import   Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework import generics, mixins
from rest_framework import viewsets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from .pangination import CustomPagination
from employees.flters import EmployeeFilter
from rest_framework.filters import SearchFilter



# Create your views here.
@api_view(['GET', 'post'])
def studentsView(request):
   if request.method == 'GET':
       students = student.objects.all()
       serializer = StudentSerializer(students, many=True)
       return Response(serializer.data, status=status.HTTP_200_OK)
   elif request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

@api_view(['GET','PUT','DELETE'])
def studentDetail(request, pk):
    try:
        stud = student.objects.get(pk=pk)       
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = StudentSerializer(stud)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  


# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     def delete(self, request):
#         Employee.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    


# class EmployeeDetail(APIView):
#     def get_object(self, pk):     
#         try:
#             return Employee.objects.get(pk=pk)        
#         except Employee.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#         emp = self.get_object(pk)
#         serializer = EmployeeSerializer(emp)
#         return Response(serializer.data , status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         emp = self.get_object(pk)
#         serializer = EmployeeSerializer(emp, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         emp = self.get_object(pk)
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
""""

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
       
    
    def delete(self, request, *args, **kwargs):
        Employee.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""



"""
#generics
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    
#generics

class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

"""

# class EmployeesViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer_class = EmployeeSerializer
#         serializer = serializer_class(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer_class = EmployeeSerializer
#         serializer = serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         employee = get_list_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         employee = get_list_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk=None):
#         employee = get_list_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeesViewSet(viewsets.ModelViewSet):  
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter
    # filterset_fields = ['designation'] # Fields available for filtering



class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter]
    SearchFilter = ['blog_title']


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'



class BlogCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)