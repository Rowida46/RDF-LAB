from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=100)
    description=serializers.CharField(max_length=200)
    nomber_of_likes=serializers.IntegerField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)
    
    
    
    
    
    