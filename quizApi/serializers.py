from rest_framework import serializers

class QuizSerializer(serializers.Serializer):
  question = serializers.CharField(max_length=255)
  answer = serializers.ListField(allow_empty=None, min_length=1)
  
