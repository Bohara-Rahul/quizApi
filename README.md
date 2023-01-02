# Quiz Api

## A Django Rest Framework powered app

## A Simple django-rest-framework powered api developed for the simple quiz system. 

### This API receives the question and answer from the client in json format and, it sends back the response in json format with score,  

## URL Endpoints

### http://localhost:8000/quiz/lesson/1/question/1

{
  "question": "question1",
  "answer": ["option 1", "option 2", "option 3"]
}

### It is a correct answer and increases score by 1

### http://localhost:8000/quiz/lesson/1/question/2

{
  "question": "question2",
  "answer": ["option 5"]
}

### It is a correct answer and increases score by 1

### http://localhost:8000/quiz/lesson/2/question/1

{
  "question": "question1",
  "answer": ["option 2"]
}

### It is a wrong answer and does not affect score

### http://localhost:8000/quiz/lesson/2/question/2

{
 "question": "question2",
 "answer": ["option 6"]
}

### It is a wrong answer and does not affect score



