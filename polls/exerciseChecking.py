import sqlite3 as lite

con = lite.connect('')


class StepChecking:
   
   

   def __init__(self, skill, queNumber, queExpression, stepNumber, stepAnswer,   ):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def checkNotBlank(self):
      return None

    # print "Total Employee %d" % Employee.empCount

   def checkArthimetic(self):
      return None

    #  print "Name : ", self.name,  ", Salary: ", self.salary

   def checkSymbolically(self):
      return None

   def checkNumerically (self):
      return None

   def checkMistake (self):
      return None



input = "dy/dx = 0"
cursor = connection.cursor()
cursor.execute("""SELECT polls_exercise.*, polls_exe_working.*, polls_exe_possible.*
FROM polls_exercise
INNER JOIN  polls_exe_working
ON polls_exercise.[exercise]=polls_exe_working.[exercise_id]
INNER JOIN polls_exe_possible
ON polls_exe_working.[exeWorkingStep]=polls_exe_possible.[exeWorkingStep_id]
WHERE (polls_exercise.[skill_id]="1" AND polls_exercise.[exeQueNum]="5" AND polls_exe_working.[exeWorkstepNo]="3")""")

row = cursor.fetchall()
print row


        