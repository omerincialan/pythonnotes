##
#  This program grades a multiple choice exam in which each question has four
#  possible choices: a, b, c, or d.
#

# Define a string containing the correct answers.
CORRECT_ANSWERS = "adbdcacbdac"

# Obtain the user's answers, and make sure enough answers are provided.
done = False
while not done :
   userAnswers = input("Enter your exam answers: ")
   if len(userAnswers) == len(CORRECT_ANSWERS) :
      done = True     
   else :
      print("Error: an incorrect number of answers given.")    
        
# Check the exam.
numQuestions = len(CORRECT_ANSWERS)
numCorrect = 0
results = ""

for i in range(numQuestions) :
   if userAnswers[i] == CORRECT_ANSWERS[i] :
      numCorrect = numCorrect + 1
      results = results + userAnswers[i]
   else :
      results = results + "X"
      
# Grade the exam.
score = round(numCorrect / numQuestions * 100)

if score == 100 :
   print("Very Good!")
else :
   print("You missed %d questions: %s" % (numQuestions - numCorrect, results))
   
print("Your score is: %d percent" % score)   

