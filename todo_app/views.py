from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer, BucketSerializer      
from .models import Todo, Bucket                  

class TodoView(viewsets.ModelViewSet):       
  serializer_class = TodoSerializer          
  queryset = Todo.objects.all()  

class BucketView(viewsets.ModelViewSet):       
  serializer_class = BucketSerializer          
  queryset = Bucket.objects.all()  