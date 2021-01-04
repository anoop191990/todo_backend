from rest_framework import serializers
from .models import Todo, Bucket

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'bucket', 'title', 'description', 'is_done')

class BucketSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bucket
    fields = ('id', 'name')