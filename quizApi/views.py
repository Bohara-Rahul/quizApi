from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import QuizSerializer

from .utils import check_answer

# Create your views here.

@api_view(['POST'])
def post_quizzes(request, lessonId, questionId):
  
  if request.method == "POST":
    serializer = QuizSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serialized_data = serializer.validated_data
    [score, num_of_questions, average_score, is_correct] = check_answer(serialized_data, lessonId, questionId)
    return Response({
      "score":score, 
      "num_of_questions": num_of_questions,
      "average_score": average_score,
      "is_correct": is_correct
    })
    
    
