
from rest_framework import serializers
from .models import Todo




class TodoSerializer(serializers.ModelSerializer):
    
    author = serializers.CharField(source='author.email', read_only=True)
    class Meta:
        model = Todo
        fields = [ 'pk','note', 'title', 'created_at', 'author', 'time_passed', 'checked']

