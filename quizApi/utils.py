# data for the question and answer
data = {
  "lesson_one_question_one_answer": ["option 1", "option 2", "option 3"],
  "lesson_one_question_two_answer": ["option 5"],
  "lesson_two_question_one_answer": ["option 1"],
  "lesson_two_question_two_answer": ["option 1", "option 4"]
}

# variables to store score and number of questions
score = 0
num_of_questions = 0
average_score = 0

# return correct answer 
def get_correct_answer(lessonId, questionId):
  correct_answer = []
  if lessonId == 1 and questionId == 1:
    correct_answer = data["lesson_one_question_one_answer"]
    
  if lessonId == 1 and questionId == 2:
    correct_answer = data["lesson_one_question_two_answer"]
    
  if lessonId == 2 and questionId == 1:
    correct_answer = data["lesson_two_question_one_answer"]
    
  if lessonId == 2 and questionId == 2:
    correct_answer = data["lesson_two_question_two_answer"]
    
  return correct_answer


# function to check answer
def check_answer(serialized_data, lessonId, questionId):
  global score
  global num_of_questions
  global average_score
  is_correct = False

  submitted_answer = serialized_data["answer"]
  num_of_questions += 1

  correct_answer = get_correct_answer(lessonId, questionId)

  if submitted_answer == correct_answer:
    score += 1
    is_correct = True

  average_score = round(score / num_of_questions, 2)

  return [score, num_of_questions, average_score, is_correct]
   

