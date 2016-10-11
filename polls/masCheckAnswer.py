import sqlite3 as lite
from sympy.abc import x,y
from sympy import *  #for mathematical calculation
import string
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
class MasStepChecking:
    def __init__(self, input, skill_id, masQueNum, stepCount, StepNo):
        self.input = input
        self.skill_id = skill_id
        self.masQueNum = masQueNum
        self.StepNo = StepNo
        self.stepCount = stepCount
        print "stepCount", self.stepCount
        print "masQueNum", self.masQueNum
        print "skill_id", self.skill_id
        
        
      
    def get_masStepAnswer(self):
        '''connect to the database to retrive the stepAnswer, hint, feedback using the skill id, question number and work step number '''
        cur1 = con.cursor()
        cur1.execute('''SELECT polls_mastery.[masQueLevel], polls_mastery.[masTotalWorkSteps], polls_mastery.[masHint], polls_mastery.[masRightFeedback], polls_mastery.[masWrongFeedback], polls_mas_working.[masWorkStepAnswer], polls_mas_working.[masWorkingStep], polls_mas_working.[masStepNo]
        FROM polls_mastery
        INNER JOIN polls_mas_working
        ON polls_mastery.[mastery] = polls_mas_working.[mastery_id]
        WHERE polls_mastery.[skill_id]= %s AND polls_mastery.[mastery] = %s AND polls_mas_working.[masStepNo] = %s'''%(self.skill_id, self.masQueNum, self.stepCount))
        masStepAnswer = dictfetchall(cur1)
        print "StepAnswer", masStepAnswer
        return masStepAnswer
        

    '''The function to clear all the whitespace from the answers derive from the database'''
    def preprocess_masStepAnswer(self):
        obStepAnswer = self.get_masStepAnswer()
        for item in obStepAnswer:
            masstepAnswer = str(item["masWorkStepAnswer"])
            print masstepAnswer
            # rawStepAnswer = stepAnswer.translate(None, string.whitespace)
            masstepAnswer = masstepAnswer.replace(' ', '')
            masStepAnswer = masStepAnswer.replace(',','')
            masStepAnswer = masStepAnswer.lower()
        print "masStepAnswer", masStepAnswer
        return masStepAnswer


    # '''The function to get the hint from the database.'''
    # def getWorkStepHint(self):
    #     obStepAnswer = self.getStepAnswer()
    #     for item in obStepAnswer:
    #         StepHint = item["exeStepHint"]
    #     print StepHint
    #     return StepHint
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
    

    #     #return None
    # def checkPossibleMistake (self, input):
    #     PossibleMistake = self.getPossibleMistake()
    #     for item in PossibleMistake:
    #         '''loop the dictionary to reach the possible mistake from the database'''
    #         possibleMistake = str(item["exePossibleMistake"])
    #         '''take away the whitespace'''
    #         # possibleMistake = possibleMistake.translate(None, string.whitespace)
    #         possibleMistake = possibleMistake.replace(' ','')
    #         possibleMistake = possibleMistake.replace (',', '')
    #         '''lower case for possible mistake'''
    #         possibleMistake = possibleMistake.lower()
    #         '''get the right hand side of possible mistake expression.'''
    #         possibleFeedback =  str(item["exeMistakeFeedback"])
    #         possibleHint = str(item['exeFeedbackVisualAid'])
    #         print "possible mistake", possibleMistake
    # #        print "7",possibleMistake
    #         if self.compareRHSExpression(input, possibleMistake)  == True:
    # #            print "8"
    #             return True, possibleFeedback, possibleHint
    #         else:
    #             print "9"
    #             return False, "Check Possible Mistake", None

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
        x3=-2
        eq=expr1-expr2
        print eq
        if eq == 0:
            #print "Correct"
            return True
        elif (expr1.subs(x,x1)==expr2.subs(x,x1))&(expr1.subs(x,x2)==expr2.subs(x,x2))&(expr1.subs(x,x3)==expr2.subs(x,x3)):
            print "Correct"
            return True
        else:
            print "Wrong"
            return False

    


    '''main engine'''    
    def mascheckStepAnswer(self, input, obtStepAnswer):
        '''loop the dictionary to reach the answer from the database, also take away all empty space, comma and put in lower case in the stepAnswer'''
        for item in obtStepAnswer:
            masstepAnswer = str(item["masWorkStepAnswer"])
            print masstepAnswer
            masstepAnswer = unicode(masstepAnswer)
            print "1"
            masstepAnswer = masstepAnswer.replace(" ", "")
            print "2"
            masstepAnswer = masstepAnswer.replace(",","")
            print "3"
            masstepAnswer = masstepAnswer.lower()
            print "4"
            print masstepAnswer
            lhs_masstepAnswer = masstepAnswer.split("=")[0]
            lhs_masstepAnswer = lhs_masstepAnswer.replace('(', '')
            lhs_masstepAnswer = lhs_masstepAnswer.replace(')','')
            rhs_masstepAnswer = masstepAnswer.split("=")[1]
            rhs_masstepAnswer = unicode(rhs_masstepAnswer)
            print lhs_masstepAnswer
            print rhs_masstepAnswer

            '''insert * between digit and variable x '''
            rhs_StepAnswer = re.sub(r'(\d+)([u - x])', r'\1*\2',rhs_masstepAnswer)
            print "1"
            '''insert * between digit and open parentheses '''  
            rhs_StepAnswer = re.sub(r'(\w)(\()', r'\1*\2',rhs_StepAnswer)
            print "2"
            '''insert * between closing parentheses and digit '''         
            rhs_StepAnswer = re.sub(r'(\))(\w)', r'\1*\2',rhs_StepAnswer)
            print "3"
            '''insert * between closing parentheses and open parentheses '''         
            rhs_StepAnswer = re.sub(r'(\))(\()', r'\1*\2',rhs_StepAnswer)
            print "4"
            '''insert * between variable x and digit '''        
            rhs_StepAnswer = re.sub(r'([u - x])(\d+)', r'\1*\2',rhs_StepAnswer)
            print "5"
            '''insert * between digits and square roots '''
            rhs_StepAnswer = re.sub(r'(\d+)([sqrt])', r'\1*\2', rhs_StepAnswer)


            print rhs_StepAnswer
            masstepAnswer = lhs_masstepAnswer+"="+rhs_StepAnswer

            masHint = str(item["masHint"])
            masRightFeedback = str(item["masRightFeedback"])
            masWrongFeedback = str(item["masWrongFeedback"])
            if self.compareLHSExpression(input, masstepAnswer)== True:
                    print "1"
                    if self.compareRHSExpression(input, masstepAnswer) == True:
                        print "2"
                        return masRightFeedback, 1
                        break
                    elif self.compareRHSExpressionNumerically(input, masstepAnswer) ==True:
                        print "3"
                        return masRightFeedback, 1
                        break
                    else:
                        print "5"
                        return masWrongFeedback, 0
                        break
            else:
                print "6"
                return "There is error on the left hand side of the equation.", 0

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
        obtStepAnswer = self.get_masStepAnswer()
        
        print "success with getStepAnswer"
        output1, output2 = self.mascheckStepAnswer(self.input, obtStepAnswer)
        print "output"
        print output1, output2
        return output1, output2


