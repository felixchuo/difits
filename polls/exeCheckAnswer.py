import string
import sqlite3 as lite
from sympy.abc import x,y
from sympy import *  #for mathematical calculation
import re

con = lite.connect('db.sqlite3', check_same_thread=False)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
              ]


'''initiate a class that accept 4 parameters consisting of user input and 3 dictionary from database'''
class StepChecking:
    def __init__(self, input, skill_id, exeQueNum, stepCount, StepNo):
        self.input = input
        self.skill_id = skill_id
        self.exeQueNum = exeQueNum
        self.StepNo = StepNo
        self.stepCount = stepCount
        
        
      
    def getStepAnswer(self):
        print "skill id", self.skill_id
        print "step Count", self.stepCount
        print "exeQueNum", self.exeQueNum
        '''connect to the database to retrive the stepAnswer, hint, feedback using the skill id, question number and work step number '''
        cur1 = con.cursor()
        cur1.execute('''SELECT polls_exe_working.[exeStepAnswer], polls_exe_working.[exeStepHint], polls_exe_working.[exeHintVisualAid], polls_exe_working.[exeGeneralFeedback], polls_exe_working.[exeCongratulatory]
        FROM polls_exercise
        INNER JOIN  polls_exe_working
        ON polls_exercise.[exercise]=polls_exe_working.[exercise_id]
        WHERE polls_exe_working.[exeWorkStepNo]= %s AND polls_exercise.[exeQueNum]= %s AND polls_exercise.[skill_id]= %s'''%(self.stepCount, self.exeQueNum, self.skill_id))
        StepAnswer = dictfetchall(cur1)
        print "StepAnswer", StepAnswer
        return StepAnswer
        

        #for item in row:
        #  print item
    def getPossibleMistake(self):

        '''connect to the database to retrive the possible mistake, mistake feedback and hint based on skill_id, QueNum and work step number '''
        cur2 = con.cursor()
        cur2.execute('''SELECT polls_exe_possible.[exePossibleMistake], polls_exe_possible.[exeMistakeFeedback], polls_exe_possible.[exeFeedbackVisualAid]
        FROM polls_exercise
        INNER JOIN  polls_exe_working
        ON polls_exercise.[exercise]=polls_exe_working.[exercise_id]
        INNER JOIN polls_exe_possible
        ON polls_exe_working.[exeWorkingStep]=polls_exe_possible.[exeWorkingStep_id]
        WHERE polls_exercise.[skill_id]=%s AND polls_exercise.[exeQueNum]= %s AND polls_exe_working.[exeWorkstepNo]=%s'''% (self.skill_id, self.exeQueNum, self.stepCount))
        PossibleMistake = dictfetchall(cur2)
        return PossibleMistake
          # print self.input, self.StepAnswer, self.PossibleMistake

    '''The function to clear all the whitespace from the answers derive from the database'''
    def preprocessStepAnswer(self, StepAnswer):
        print "into pre process"
        stepAnswer = StepAnswer.lower()
        stepAnswer = stepAnswer.replace(' ','')
        stepAnswer = stepAnswer.replace(',', '')
        lhs_stepAnswer = stepAnswer.split("=")[0]
        print lhs_stepAnswer
        lhs_stepAnswer = lhs_stepAnswer.replace('(', '')
        lhs_stepAnswer = lhs_stepAnswer.replace(')','')
        rhs_stepAnswer = stepAnswer.split("=")[1]
        print rhs_stepAnswer
        '''insert * between digit and variable x '''
        rhs_stepAnswer = re.sub(r'(\d+)([u - x])', r'\1*\2',rhs_stepAnswer)
        '''insert * between digit and open parentheses '''  
        rhs_stepAnswer = re.sub(r'(\w)(\()', r'\1*\2',rhs_stepAnswer)
        '''insert * between closing parentheses and digit '''         
        rhs_stepAnswer = re.sub(r'(\))(\w)', r'\1*\2',rhs_stepAnswer)
        '''insert * between closing parentheses and open parentheses '''         
        rhs_stepAnswer = re.sub(r'(\))(\()', r'\1*\2',rhs_stepAnswer)
        '''insert * between variable x and digit '''        
        rhs_stepAnswer = re.sub(r'([u - x])(\d+)', r'\1*\2',rhs_stepAnswer)
        '''insert * between digits and square roots '''
        rhs_stepAnswer = re.sub(r'(\d+)([sqrt])', r'\1*\2', rhs_stepAnswer)
        StepAnswer = lhs_stepAnswer+"="+rhs_stepAnswer
        print "StepAnswer", StepAnswer
        return StepAnswer


    '''The function to get the hint from the database.'''
    def getWorkStepHint(self):
        obStepAnswer = self.getStepAnswer()
        for item in obStepAnswer:
            StepHint = item["exeStepHint"]
        print StepHint
        return StepHint
    # def preprocessPossibleMistake(self):
    #     for item in self.PossibleMistake:
    #         possibleMistake = str(item["exePossibleMistake"])
    #         rawPossibleMistake = possibleMistake.translate(None, string.whitespace)
    #         print rawPossibleMistake
    #     return rawPossibleMistake

    # def checkArthimetic(self):
    #   return None

    #  print "Name : ", self.name,  ", Salary: ", self.salary
      #


    '''The function to get the right hand side of the mathematical expression before the equal symbol.'''
    def getRHSExpression(self, x):
        rhs = x.split("=")[1]
        rhs = rhs.lower()
        print rhs
        return rhs

    '''The function to get the left hand side of the mathematical expression after the equal symbol.'''
    def getLHSExpression(self, x):
        print "getLHSExpression"
        print type(x)
        lhs=x.split("=")[0]
        lhs = lhs.lower()
        print lhs
        return lhs
    

        #return None
    def checkPossibleMistake (self, input):
        PossibleMistake = self.getPossibleMistake()
        for item in PossibleMistake:
            '''loop the dictionary to reach the possible mistake from the database'''
            possibleMistake = str(item["exePossibleMistake"])
            '''take away the whitespace'''
            # possibleMistake = possibleMistake.translate(None, string.whitespace)
            possibleMistake = possibleMistake.replace(' ','')
            possibleMistake = possibleMistake.replace (',', '')
            '''lower case for possible mistake'''
            possibleMistake = possibleMistake.lower()
            '''get the right hand side of possible mistake expression.'''
            possibleFeedback =  str(item["exeMistakeFeedback"])
            possibleHint = str(item['exeFeedbackVisualAid'])
            print "possible mistake", possibleMistake
    #        print "7",possibleMistake
            if self.compareRHSExpression(input, possibleMistake)  == True:
    #            print "8"
                return True, possibleFeedback, possibleHint
            else:
                print "9"
                return False, "Check Possible Mistake", None

    def compareLHSExpression(self, x, y):
        print 'check left hand side'
        first = self.getLHSExpression(x)
        first = first
        print "type for input", type(first)
        second = self.getLHSExpression(y)
        print 'input:',first
        print 'step answer:',second
        if first == second:
            print "LHS Expression match"
            return True
        else:
            return False

    def compareRHSExpression(self, k, l):
        print 'check RHS as string'
        RHSString1 = self.getRHSExpression(k)
        RHSString2 = self.getRHSExpression(l)
        print 'input answer RHS:', RHSString1
        print 'step answer RHS:', RHSString2
        '''Compare RHS expression based on string comparison.'''
        if RHSString1 == RHSString2:
            #print 'Match'
            return True
        else:
            #print 'Mistmatch'
            return False


    def compareRHSExpressionNumerically(self, k, l):
        print 'check right hand side'
        str_expr1 = self.getRHSExpression(k)
        str_expr2 = self.getRHSExpression(l)
        print 'input answer RHS numerical:', str_expr1
        print 'step answer RHS numerical:', str_expr2
        expr1=sympify(str_expr1)
        print 'convert to mathematical expression',expr1
        expr2=sympify(str_expr2)

        x1=0
        x2=1
        x3=-1
        eq=expr1-expr2
        print eq
        if eq == 0:
            #print "Correct"
            return True
        elif (((expr1.subs(x,x1)==expr2.subs(x,x1))&(expr1.subs(x,x2)==expr2.subs(x,x2)))&(expr1.subs(x,x3)==expr2.subs(x,x3))):
            print "Correct"
            return True
        else:
            print "Wrong"
            return False

    


    '''main engine'''    
    def checkStepAnswer(self, input, obtStepAnswer):
        '''loop the dictionary to reach the answer from the database, also take away all empty space, comma and put in lower case in the stepAnswer'''
        for item in obtStepAnswer:
            stepCongrats = str(item["exeCongratulatory"])
            stepFeedback = str(item["exeGeneralFeedback"])
            stepAnswer = str(item["exeStepAnswer"])
            print "into step Answer"
            stepAnswer = self.preprocessStepAnswer(stepAnswer)
            print " failure"
            stepHint = str(item["exeStepHint"])
            stepVisualAid = str(item["exeHintVisualAid"])
            if self.compareLHSExpression(input, stepAnswer)== True:
                    print "1"
                    if self.compareRHSExpression(input, stepAnswer) == True:
                        print "2"
                        return stepCongrats, 1, None
                    elif self.compareRHSExpressionNumerically(input, stepAnswer) ==True:
                        print "3"
                        return stepCongrats, 1, None
                    elif self.checkPossibleMistake(input)[0] == True:
                        print "4"
                        return self.checkPossibleMistake(input)[1], 0, self.checkPossibleMistake(input)[2]
                    else:
                        print "5"
                        return stepFeedback, 0, stepVisualAid
                        break
            else:
                print "6"
                return "There is error on the left hand side of the equation.", 0, None

    # def incretStepQue (self, result):
    #     print "type",  type(result)
    #     print "type for self.StepNo", type(self.StepNo)
    #     print "type for self.exeQueNum", type(self.exeQueNum)
    #     if (self.stepCount == self.StepNo)&(result ==1):
    #         # increase question number
    #         a = int(self.exeQueNum)
    #         a = a +1
    #         # call the function to update the database on student progress details
    #         return unicode(a), self.stepCount
    #     else:
    #         # increase step number
    #         b = int(self.stepCount)
    #         b = b +1
    #         return self.exeQueNum, unicode(b)


    def intermediaGetValue (self):
        
        print "input passed"
        # skill_id = self.skill_id
        # stepNo = self.StepNo
        # exeQueNum = self.exeQueNum
        obtStepAnswer = self.getStepAnswer()
        
        print "success with getStepAnswer"
        output1, output2, output3 = self.checkStepAnswer(self.input, obtStepAnswer)
        print "output"
        print output1, output2, output3
        # output4, output5 = self.incretStepQue(output2)
        # print output4, output5
        return output1, output2, output3


