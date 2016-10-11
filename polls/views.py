from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .models import Student
from .models import Progress
from .models import Skill
from django.template import Template, Context 
from django.shortcuts import redirect
from .models import PostForm
from django.db import connection
from django.contrib.auth.models import User
from check_tru import checkworking
from check_tru import mas_checkworking
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import sys
sys.path.insert(0, '/difits/mathml2asciimath')
import mathml2ascii
import random
import json
import copy
import re


##for registering first time user requesting usernamae and password
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
                ]
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print new_user.id
            return redirect('/info_form/'+ str(new_user.id))
    else:
        form = UserCreationForm()
    return render(request, "register.html", {'form': form})



def index(request):
    lastest_student_list = Student.objects.all()
    context = {'lastest_student_list': lastest_student_list}
    return render(request, 'index.html', context)

##for showing the report page template after student login
def detail(request):
    sessionId = request.session._session_key
    print "session id", sessionId
    if request.user.is_authenticated(): 
        print request.user.id
        student = Student.objects.get(student_loginid=request.user.id)
        cursor = connection.cursor()
        cursor.execute("""SELECT polls_student.[student], polls_progress.[mastery_progress], polls_progress.[tutorial_progress], polls_progress.[skill], polls_skill.[skill_name], polls_progress.[exercise_progress], polls_progress.[progress], polls_progress.[t_status], polls_progress.[e_status], polls_progress.[m_status]
            FROM polls_student
            INNER JOIN polls_progress 
            ON polls_student.[student]=polls_progress.[student_id]
            INNER JOIN polls_skill
            ON polls_skill.[skill]=polls_progress.[skill]
            WHERE polls_student.[student_loginid]=%s""", [request.user.id])
        row = cursor.fetchall()
        print row
    return render(request, 'ReportPageTemplate.html', {'student': student, 'row': row}) 


def progress(request):
    lastest_progress_list = Progress.objects.all()
    return render(request, 'progress.html', {'recent_progress': lastest_progress_list})

def skill_list(request):
    skill_list = Skill.objects.all()
    return render(request, 'skill_list.html', {'skill_list': skill_list})

def mainGUI (request, student):
    student = Student.objects.get(pk=student)
    return render(request, 'mainGUI.html', {'student': student})

def logout_view(request): ##pass together the current data in url 
    if request.user.is_authenticated(): 
        username1 = request.user.username ##here you can see your current login username 
        print username1 
        return redirect('login') 


##fill in student details using form
def post_new(request, userid):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print 'form is valid'
            post = form.save(commit=False)
            post.student_loginid = userid
            post.save()
            print post.student
            cursor = connection.cursor()
            tp='NA'
            ep='NA'
            mp='NA'
            s='0'
            skill=[1,2,3,4,5,6]
            for i in skill:
                print i 
                cursor.execute("INSERT INTO polls_progress (tutorial_progress, exercise_progress, mastery_progress, student_id, skill, t_status, e_status, m_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(tp, ep, mp, int(post.student), i, s, s, s))
            connection.commit()

            cursor2 = connection.cursor()
            cursor2.execute ('''SELECT polls_progress.[progress]
            FROM polls_progress
            WHERE polls_progress.[student_id]= %s'''%(post.student))
            progressid = cursor2.fetchall()
            print "Progress id", progressid

            t = '1'
            a = '1'
            listProgressId = [x[0] for x in progressid]
            cursor3 = connection.cursor()
            for i in listProgressId:
                cursor3.execute("INSERT INTO polls_t_progress_details (progress_id, tutorial, animation_progress, student) VALUES (?, ?, ?, ?)",(i, t, a, int(post.student)))
            connection.commit()


            cursor4 = connection.cursor()
            for i in listProgressId:
                cursor4.execute("INSERT INTO polls_exe_progress_details (exercise, exeQueNumStatus, progress_id, student) VALUES (?, ?, ?, ?)",(t, a, i, int(post.student)))
            connection.commit()

            
            cursor5 = connection.cursor()
            for i in listProgressId:
                cursor5.execute("INSERT INTO polls_m_progress_details (mastery, question_progress, mastery_score, progress_id, student, mas_adv_progress, mas_easy_progress, mas_mod_progress) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(t, a, s, i, int(post.student), s,s,s))
            connection.commit()

            cursor6 = connection.cursor()
            cursor6.execute("""UPDATE polls_progress
            SET t_status = %s
            WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", (t, t, int(post.student)))
            connection.commit()

            return redirect('login')
    else:
        form = PostForm()
    return render(request, 'info_form.html', {'form': form}) 


    
def retrieve_password_form (request):
    return render(request, 'retrieve_password_form.html')

def registrationSuccess (request):
    return render(request, 'registrationSuccess.html')


def retrieve (request):
    if 'firstname' in request.GET and request.GET['firstname']:
        f_name=request.GET['firstname']
        l_name=request.GET['lastname']
        u_name=request.GET['username']
        n_password=request.GET['new_password']
        c_password=request.GET['confirm_password']
        print f_name
        print l_name
        print u_name
        print n_password
        print c_password

        cursor = connection.cursor()
        cursor.execute("""SELECT auth_user.[username], polls_student.[student_firstname], polls_student.[student_lastname]
            FROM polls_student
            INNER JOIN auth_user 
            ON polls_student.[student_loginid]=auth_user.[id]
            WHERE auth_user.[username]= %s AND polls_student.[student_firstname]= %s AND polls_student.[student_lastname]= %s""", (u_name, f_name, l_name))
        row = cursor.fetchone()
        print row
        if row is not None:
            if n_password == c_password:
                u = User.objects.get(username__exact=str(u_name))
                u.set_password(n_password)
                u.save()
                return redirect('login')
            else:
                return render(request, 'retrieve_password_form.html', {'error':True}) 
        else:
            return render(request, 'retrieve_password_form.html', {'error':True})
    return render(request, 'retrieve_password_form.html', {'error':True})


'''create a function for exercise which takes in one params from the previous page to retrieve all the data and then display using exercise template'''

def exercise (request, skillid):
    if request.user.is_authenticated(): 
        print "1", request.user.id
        pupil = Student.objects.get(student_loginid=request.user.id)
        '''based on the student login id retrieve from the database the student id in the form of list'''
        cursor_studentid = connection.cursor()
        cursor_studentid.execute("""SELECT polls_student.[student]
        FROM polls_student
        WHERE polls_student.[student_loginid]= %s""", [request.user.id])
        row_studentid = cursor_studentid.fetchall()
        print type(row_studentid)       
        print "Student Id", row_studentid[0][0]

        print skillid
        print type(skillid)
        '''using the params of skillid from the previous page, query from the database and retrieve the student progress in the exercise section'''
        cursor = connection.cursor()
        cursor.execute('''SELECT polls_progress.[progress]
        FROM polls_progress
        WHERE polls_progress.[student_id]= %s AND polls_progress.[skill] = %s'''%(row_studentid[0][0], skillid))
        progressid = cursor.fetchall()
        print "Progress id", progressid[0][0]

        '''get to the question number'''
        cursor1 = connection.cursor()
        cursor1.execute("""SELECT polls_exe_progress_details.[exercise]
        FROM polls_exe_progress_details
        WHERE polls_exe_progress_details.[progress_id]= %s """, [progressid[0][0]])
        row_exercise = cursor1.fetchall()
        print "row_exercise[0][0]", row_exercise[0][0]
        print "skill id", skillid


        '''using the data retrieve from the two queries above, retrieve the question for the exercise from the database and display them using the exercise template'''
        cursor2 = connection.cursor()
        cursor2.execute("""SELECT polls_exercise.[exeQueNum], polls_exercise.[exeQueText], polls_exercise.[exeQueExpression], polls_exercise.[exeTotalWorkSteps] 
        FROM polls_exercise
        WHERE polls_exercise.[exeQueNum] = %s AND polls_exercise.[skill_id]=%s""", (row_exercise[0][0], skillid))
        row2 = cursor2.fetchall()
        print row2
        print type(row2)

        cursor3 = connection.cursor()
        cursor3.execute("""SELECT polls_skill.[skill], polls_skill.[skill_name]
        FROM polls_skill""")
        row3 = cursor3.fetchall()
        '''return student_id, question information and skill id to the exercise template to display  '''
    return render_to_response('exercise.html', {'student': pupil, 'exercise_info': row2, 'skill_id': skillid, 'skill_list': row3}, context_instance=RequestContext(request)) 

@csrf_exempt
def mastery (request, skillid):

    if request.user.is_authenticated(): 
        print "1", request.user.id
        pupil = Student.objects.get(student_loginid=request.user.id)
        '''based on the student login id retrieve from the database the student id in the form of list'''
        cursor_studentid = connection.cursor()
        cursor_studentid.execute("""SELECT polls_student.[student]
        FROM polls_student
        WHERE polls_student.[student_loginid]= %s""", [request.user.id])
        row_studentid = cursor_studentid.fetchall()
        print type(row_studentid)       
        print row_studentid[0][0]

        print skillid
        print type(skillid)
        '''using the params of skillid from the previous page, query from the database and retrieve the student progress in the exercise section'''
        cursor = connection.cursor()
        cursor.execute("""SELECT polls_progress.[progress]
        FROM polls_progress
        WHERE polls_progress.[student_id]= %s AND polls_progress.[skill] = %s""", (row_studentid[0][0], skillid))
        progressid = cursor.fetchall()
        print progressid[0][0]

        #retrieve the data on the number of questions user have acheived for each level of mastery
        cursor1 = connection.cursor()
        cursor1.execute("""SELECT polls_m_progress_details.[mastery], polls_m_progress_details.[mas_easy_progress], polls_m_progress_details.[mas_mod_progress], polls_m_progress_details.[mas_adv_progress]
        FROM polls_m_progress_details
        WHERE polls_m_progress_details.[progress_id]= %s """, [progressid[0][0]])
        row_mastery = cursor1.fetchall()
        print row_mastery
        easyCount = row_mastery[0][1]
        modCount = row_mastery[0][2]
        chaCount = row_mastery[0][3]
        print "easyCount", easyCount
        print "modCount", modCount
        print "chaCount", chaCount
        #determine the mastery level of the user for that skill
        masLevel = getMasteryLevel(easyCount, modCount, chaCount)
        print masLevel

        cursor3 = connection.cursor()
        cursor3.execute("""SELECT polls_skill.[skill], polls_skill.[skill_name]
        FROM polls_skill""")
        row3 = cursor3.fetchall()
       
    return render(request, 'mastery.html', {'student': pupil, 'skill_id': skillid, 'skill_list': row3, 'masLevel': masLevel, 'progressid': progressid[0][0]}, context_instance=RequestContext(request)) 

@csrf_exempt
def mas_get_questions (request):
    if request.method == 'POST':
        print "the get mastery question from ajax is working"
        """pass the value from the user to retrieve questions from the database"""
        masQueInfo=json.loads(request.POST.get('mas_get_questions'))
        masLevel = masQueInfo['masLevel']
        skillid = masQueInfo['skill_id']
        studentId = masQueInfo['studentId']

        '''using the data, retrieve the question for the exercise from the database and display them using the exercise template'''
        cursor2 = connection.cursor()
        cursor2.execute('''SELECT *
        FROM polls_mastery
        WHERE polls_mastery.[masQueLevel]= %s AND polls_mastery.[skill_id]=%s'''%(masLevel, skillid))

        masQueList = cursor2.fetchall()
        # get the length of the list to generate the number for the question and insert them into the list
        totalQue = len(masQueList)
        print "the number of question in the list", totalQue
        QueNoList = list(range(1,totalQue+1))
        print QueNoList
        # QueNoList = tuple(QueNoList)
        # print QueNoList
        print "type for QueNoLIst", type(QueNoList)
        #radomized the questions
        random.shuffle(masQueList)
        print masQueList
        print "type for que list", type(masQueList)

        keys = ['mastery', 'masQueText', 'masQueExpression', 'masQueLevel', 'masTotalWorkSteps', 'skill_id', 'masHint', 'masRightFeedback', 'masWrongFeedback']

        quedict = [dict(zip(keys, row)) for row in masQueList ]
        print quedict
        count = 1
        for subseq in quedict:
            subseq.setdefault('Que', count)
            count+=1
            print subseq

        print quedict
        mas_question_data = {}
        mas_question_data['questions'] = quedict
        mas_question_data['skill_id'] = skillid
        mas_question_data['masLevel'] = masLevel
        mas_question_data['studentId'] = studentId
        mas_question_data['totalQue'] = totalQue
    
        return HttpResponse(
            json.dumps(mas_question_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
 



@csrf_exempt
def tutorial (request, skillid):
    if request.user.is_authenticated(): 
        print "1", request.user.id
        pupil = Student.objects.get(student_loginid=request.user.id)
        '''based on the student login id retrieve from the database the student id in the form of list'''
        cursor_studentid = connection.cursor()
        cursor_studentid.execute("""SELECT polls_student.[student]
        FROM polls_student
        WHERE polls_student.[student_loginid]= %s""", [request.user.id])
        row_studentid = cursor_studentid.fetchall()
        print type(row_studentid)       
        print row_studentid[0][0]

        print skillid
        print type(skillid)
        '''using the params of skillid from the previous page, query from the database and retrieve the student progress in the exercise section'''
        cursor = connection.cursor()
        cursor.execute("""SELECT polls_progress.[progress]
        FROM polls_progress
        WHERE polls_progress.[student_id]= %s AND polls_progress.[skill] = %s""", (row_studentid[0][0], skillid))
        progressid = cursor.fetchall()
        print progressid[0][0]
        

        
        cursor1 = connection.cursor()
        cursor1.execute("""SELECT polls_t_progress_details.[tutorial]
        FROM polls_t_progress_details
        WHERE polls_t_progress_details.[progress_id]= %s """, [progressid[0][0]])
        row_tutorial = cursor1.fetchall()
        print row_tutorial[0][0]

        
        '''using the data retrieve from the two queries above, retrieve the question for the exercise from the database and display them using the exercise template'''
        cursor2 = connection.cursor()
        cursor2.execute("""SELECT polls_tutorial.[tutorial_animation], polls_tutorial.[tutorial]
        FROM polls_tutorial
        WHERE polls_tutorial.[tutorial] = %s""", [row_tutorial[0][0]])
        row2 = cursor2.fetchall()
        print "row 2", row2
        print type(row2)
        

        cursor3 = connection.cursor()
        cursor3.execute("""SELECT polls_skill.[skill], polls_skill.[skill_name]
        FROM polls_skill""")
        row3 = cursor3.fetchall()


        '''find the total number of animation for the skill'''
        cursor4 = connection.cursor()
        cursor4.execute("""SELECT polls_tutorial.*
        FROM polls_tutorial
        WHERE polls_tutorial.[skill_id] = %s""", [skillid])
        row4 = cursor4.fetchall()
        print row4
        print type(row4)
        totalAni = len(row4)
        print "total number of animation", totalAni

    return render(request, 'tutorial.html', {'student': pupil, 'tutorial_info': row_tutorial[0][0], 'skill_id': skillid, 'skill_list': row3, 'total_ani': totalAni, 'tutName': row4 }) 

@csrf_exempt
def checkworkingstep(request):
    print 'yes'
    if request.method == 'POST':
        print "the working step from ajax"
        """get value from the user input and implicit data"""
        the_workingstep=json.loads(request.POST.get('the_workingstep'))
        post_workingstep = the_workingstep['the_workingstep']
        skillid = the_workingstep['skill_id']
        exeQueNum = the_workingstep['QueNum']
        workStepNo = the_workingstep['workStepNo']
        stepCount = the_workingstep['stepCount']
        studentId = the_workingstep['studentId']
        

        ascii_input = mathml2ascii.main(post_workingstep)
        '''function to insert * so that can be used for comparison'''
        lhs_ascii_input = ascii_input.split("=")[0]
        lhs_ascii_input = lhs_ascii_input.replace('(', '')
        lhs_ascii_input = lhs_ascii_input.replace(')','')
        rhs_ascii_input = ascii_input.split("=")[1]
        '''insert * between digit and variable x '''
        rhs_input = re.sub(r'(\d+)([u - x])', r'\1*\2',rhs_ascii_input)
        '''insert * between digit and open parentheses '''  
        rhs_input = re.sub(r'(\w)(\()', r'\1*\2',rhs_input)
        '''insert * between closing parentheses and digit '''         
        rhs_input = re.sub(r'(\))(\w)', r'\1*\2',rhs_input)
        '''insert * between closing parentheses and open parentheses '''         
        rhs_input = re.sub(r'(\))(\()', r'\1*\2',rhs_input)
        '''insert * between variable x and digit '''        
        rhs_input = re.sub(r'([u - x])(\d+)', r'\1*\2',rhs_input)
        '''insert * between digits and square roots '''
        rhs_input = re.sub(r'(\d+)([sqrt])', r'\1*\2', rhs_input)


        print rhs_input
        ascii_input = lhs_ascii_input+"="+rhs_input

        """PROCESS WITH ENGINE"""
        c1, c2, c3, input_return = checkworking(ascii_input, skillid, exeQueNum, stepCount, workStepNo)
        
        """STORE RETURN RESULT"""
                
        actionChoice = 0
        
        actionChoice, stepCount = decision(c2, stepCount, workStepNo, exeQueNum, studentId, skillid)
        print "actionChoice", actionChoice
        input_return = input_return.replace('*', '')        
        response_data = {}
        response_data['input'] = input_return
        response_data['Feedback'] = c1
        response_data['CheckingResult'] = c2
        response_data['VisualAid'] = c3
        response_data['stepCount'] = stepCount
        response_data['workStepNo'] = workStepNo
        response_data['actionChoice'] = actionChoice
        
        print "step count in view", stepCount
        print "actionChoice", actionChoice 
        
        """update student progress for the exercise of the skill"""

        if actionChoice == 3:
            cursor2 = connection.cursor()
            cursor2.execute("""UPDATE polls_progress
            SET exercise_progress = %s,
                m_status = %s
            WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("CM", 1, skillid, studentId))
            connection.commit()
        else:
            cursor2 = connection.cursor()
            cursor2.execute("""SELECT polls_progress.[exercise_progress]
            FROM polls_progress
            WHERE polls_progress.[skill]= %s AND polls_progress.[student_id] = %s""", (skillid, studentId))
            exe_progress = cursor2.fetchall()
            print exe_progress
            print exe_progress[0][0]
            if exe_progress[0][0] != "CM" :
                cursor2.execute("""UPDATE polls_progress
                SET exercise_progress = %s
                WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", skillid, studentId))
            connection.commit()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
 
        




@csrf_exempt
def getworkingstephint(request):
    if request.method == 'POST':
        print "the working step from ajax"
        """get value from the user input and implicit data"""
        stephint =json.loads(request.POST.get('stephint'))
        skillid = stephint['skill_id']
        exeQueNum = stephint['QueNum']
        workStepNo = stephint['workStepNo']
        stepCount = stephint['stepCount']
        print "success get hint"
        print skillid
        print exeQueNum
        '''connect to the database to retrive the stepAnswer, hint using the skill id, question number and work step number '''
        curhint = connection.cursor()
        curhint.execute("""SELECT polls_exe_working.[exeStepHint], polls_exe_working.[exeHintVisualAid]
        FROM polls_exercise
        INNER JOIN  polls_exe_working
        ON polls_exercise.[exercise]=polls_exe_working.[exercise_id]
        WHERE polls_exercise.[skill_id]= %s AND polls_exercise.[exeQueNum]= %s AND polls_exe_working.[exeWorkStepNo]=%s""", (skillid, exeQueNum, stepCount))
        StepHint = dictfetchall(curhint)
        print StepHint
        print type (StepHint)

        print StepHint[0]
        response_hint = StepHint[0]
        print response_hint
        print type (response_hint)
        print response_hint['exeHintVisualAid']
        print response_hint['exeStepHint']
        # c1, c2 = checkworking(post_workingstep, skillid, exeQueNum)
        # print c1
        print "FInished calling def checkworkingstep"
        return HttpResponse(
            json.dumps(response_hint),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@csrf_exempt
def getworkingstepanswer(request):
    if request.method == 'POST':
        print "the working step from ajax"
        stephint =json.loads(request.POST.get('stepanswer'))
        skillid = stephint['skill_id']
        exeQueNum = stephint['QueNum']
        workStepNo = stephint['workStepNo']
        stepCount = stephint['stepCount']
        print "success get answer request"
        '''connect to the database to retrive the step answer using the skill id, question number and work step number '''
        curanswer = connection.cursor()
        curanswer.execute("""SELECT polls_exe_working.[exeStepAnswer]
        FROM polls_exercise
        INNER JOIN  polls_exe_working
        ON polls_exercise.[exercise]=polls_exe_working.[exercise_id]
        WHERE polls_exercise.[skill_id]= %s AND polls_exercise.[exeQueNum]= %s AND polls_exe_working.[exeWorkStepNo]=%s""", (skillid, exeQueNum, stepCount))
        StepAnswer = dictfetchall(curanswer)
        '''temporary storage for step answer in order to strip away *, to enable display in mathematical expression'''
        response_answer = StepAnswer[0]
        answerStep = response_answer['exeStepAnswer']
        answerStep = answerStep.replace('*', '')
        response_answer['exeStepAnswer'] = answerStep
        print "FInished calling def workingstepanswer"
        return HttpResponse(
            json.dumps(response_answer),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


def updateExeProDet (studentId, skillid, exeQueNum):
    print "exeQueNum in function updateExeProDet", exeQueNum
    if int(exeQueNum) < 5 :
        a =  int(exeQueNum)
        a = a + 1
        print a
        print skillid
        print type(skillid)
        '''using the params of skillid from the previous page, query from the database and retrieve the student progress in the exercise section'''
        cursor = connection.cursor()
        cursor.execute("""SELECT polls_progress.[progress]
        FROM polls_progress
        WHERE polls_progress.[student_id]= %s AND polls_progress.[skill] = %s""", (studentId, skillid))
        progressid = cursor.fetchall()
        print "Progress id", progressid[0][0]
        '''get to the question number'''
        cursor1 = connection.cursor()
        cursor1.execute("""UPDATE polls_exe_progress_details
        SET exercise = %s
        WHERE polls_exe_progress_details.[progress_id]= %s""", [a, progressid[0][0]])
        return 0
    else:
        return 1

def decision (c2, stepCount, workStepNo, exeQueNum, studentId, skillid):
    if c2 == 1:
        if stepCount == workStepNo:
            if int(exeQueNum) == 5:
                stepCount = int(stepCount)+1
                return 3, stepCount
            else:
                print "calling the function to update exercise progress"
                exeSkillStatus = updateExeProDet(studentId, skillid, exeQueNum)
                print "going into the updating of student progress and question number increase"
                stepCount= int(stepCount)+1
                return 2, stepCount
        else:
            print "increase step count when answer correct"
            stepCount= int(stepCount)+1
            return 1, stepCount
    else:
        return 0, stepCount   

@csrf_exempt
def mas_checkworkingstep(request):
    print 'yes'
    if request.method == 'POST':
        print "the working step from ajax"
        """get value from the user input and implicit data"""
        masworkingstep=json.loads(request.POST.get('mas_workingstep'))
        mas_workingstep = masworkingstep['mas_workingstep']
        skillid = masworkingstep['skill_id']
        masQueNum = masworkingstep['QueNum']
        workStepNo = masworkingstep['workStepNo']
        stepCount = masworkingstep['stepCount']
        studentId = masworkingstep['studentId']
        totalQue = masworkingstep['totalQue']
        totalTry = masworkingstep['totalTry']
        progressId = masworkingstep['progressId']
        masLevel = masworkingstep['masLevel']
        print "able to forward the parameters"
        

        mas_ascii_input = mathml2ascii.main(mas_workingstep)
        print mas_ascii_input
        '''function to insert * so that can be used for comparison'''
        lhs_mas_ascii_input = mas_ascii_input.split("=")[0]
        lhs_mas_ascii_input = lhs_mas_ascii_input.replace('(', '')
        lhs_mas_ascii_input = lhs_mas_ascii_input.replace(')','')
        rhs_mas_ascii_input = mas_ascii_input.split("=")[1]
        print lhs_mas_ascii_input
        print type(rhs_mas_ascii_input)
        rhs_mas_ascii_input = unicode(rhs_mas_ascii_input)
        print type(rhs_mas_ascii_input)

        '''insert * between digit and variable x '''
        rhs_mas_input = re.sub(r'(\d+)([u - x])', r'\1*\2',rhs_mas_ascii_input) 
        '''insert * between digit and open parentheses '''  
        rhs_mas_input = re.sub(r'(\w)(\()', r'\1*\2',rhs_mas_input)
        '''insert * between closing parentheses and digit '''         
        rhs_mas_input = re.sub(r'(\))(\w)', r'\1*\2',rhs_mas_input)
        '''insert * between closing parentheses and open parentheses '''         
        rhs_mas_input = re.sub(r'(\))(\()', r'\1*\2',rhs_mas_input)
        '''insert * between variable x and digit '''        
        rhs_mas_input = re.sub(r'([u - x])(\d+)', r'\1*\2',rhs_mas_input)
        '''insert * between digits and square roots '''
        rhs_mas_input = re.sub(r'(\d+)([sqrt])', r'\1*\2', rhs_mas_input)


        print rhs_mas_input
        mas_ascii_input = lhs_mas_ascii_input+"="+rhs_mas_input
        """PROCESS WITH ENGINE"""
        mas1, mas2, mas3 = mas_checkworking(mas_ascii_input, skillid, masQueNum, stepCount, workStepNo)
        
        """STORE RETURN RESULT"""
        mas_actionChoice = 0
        
        mas_actionChoice, mas_stepCount = mas_decision(mas2, stepCount, workStepNo, totalQue, totalTry, studentId, skillid, progressId, masLevel)
        print "actionChoice", mas_actionChoice
        mas_input_return = mas3.replace('*', '')      
        response_data = {}
        response_data['input'] = mas_input_return
        response_data['Feedback'] = mas1
        response_data['CheckingResult'] = mas2
        response_data['stepCount'] = mas_stepCount
        response_data['workStepNo'] = workStepNo
        response_data['actionChoice'] = mas_actionChoice
        
        print "step count in view", stepCount
        print "actionChoice", mas_actionChoice 
        print "mas Level", masLevel

        initial = 0
        easy = 1
        moderate = 3
        challenging = 5
        if mas_actionChoice == 1:
            if int(masLevel) == 1:
                cursor1 = connection.cursor()
                cursor1.execute("""UPDATE polls_progress
                    SET tutorial_progress = %s,
                        exercise_progress = %s,
                        mastery_progress = %s,
                        m_status = %s,
                        e_status = %s
                    WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", "NC", "NC", initial, initial, skillid, studentId))
                
                print "Able to update on progress masLevel 1"
                cursor2 = connection.cursor()
                cursor2.execute("""UPDATE polls_t_progress_details
                    SET tutorial = %s
                    WHERE polls_t_progress_details.[progress_id] = %s AND polls_t_progress_details.[student] = %s""", (easy, progressId, studentId))
                
                print "Able to update on tutorial progress masLevel 1"
                cursor3 = connection.cursor()
                cursor3.execute("""UPDATE polls_exe_progress_details
                    SET exercise = %s
                    WHERE polls_exe_progress_details.[progress_id] = %s AND polls_exe_progress_details.[student] = %s""", (easy, progressId, studentId))
                connection.commit()
                print "Able to update on exercise progress masLevel 1"
            elif int(masLevel) ==2:
                cursor1 = connection.cursor()
                cursor1.execute("""UPDATE polls_progress
                    SET tutorial_progress = %s,
                        exercise_progress = %s,
                        mastery_progress = %s,
                        m_status = %s,
                        e_status = %s
                    WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", "NC", "NC", initial, initial, skillid, studentId))
                
                print "Able to update on progress masLevel 2"
                cursor2 = connection.cursor()
                cursor2.execute("""UPDATE polls_t_progress_details
                    SET tutorial = %s
                    WHERE polls_t_progress_details.[progress_id] = %s AND polls_t_progress_details.[student] = %s""", (moderate, progressId, studentId))
                
                print "Able to update on tutorial progress masLevel 2"
                cursor3= connection.cursor()
                cursor3.execute("""UPDATE polls_exe_progress_details
                    SET exercise = %s
                    WHERE polls_exe_progress_details.[progress_id] = %s AND polls_exe_progress_details.[student] = %s""", (moderate, progressId, studentId))
                connection.commit()
                print "Able to update on exercise progress masLevel 2"
            else:
                cursor1 = connection.cursor()
                cursor1.execute("""UPDATE polls_progress
                    SET tutorial_progress = %s,
                        exercise_progress = %s,
                        mastery_progress = %s,
                        m_status = %s,
                        e_status = %s
                    WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", "NC", "NC", initial, initial, skillid, studentId))
                
                print "Able to update on progress masLevel 3"
                cursor2 = connection.cursor()
                cursor2.execute("""UPDATE polls_t_progress_details
                    SET tutorial = %s
                    WHERE polls_t_progress_details.[progress_id] = %s AND polls_t_progress_details.[student] = %s""", (challenging, progressId, studentId))
               
                print "Able to update on tutorial progress masLevel 3"
                cursor3 = connection.cursor()
                cursor3.execute("""UPDATE polls_exe_progress_details
                    SET exercise = %s
                    WHERE polls_exe_progress_details.[progress_id] = %s AND polls_exe_progress_details.[student] = %s""", (challenging, progressId, studentId))
                connection.commit()
                print "Able to update on exercise progress masLevel 3"
        elif mas_actionChoice == 6:
            cursor2 = connection.cursor()
            cursor2.execute("""UPDATE polls_progress
                    SET mastery_progress = %s
                    WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("CM", skillid, studentId))
            connection.commit()
            # determine and activate the next skill tutorial link.  KIV for skill 4 and 5 to be activated when skill 1, 2 and 3 are completed
            if int(skillid) <= 5:
                if int(skillid) == 3:
                    nextSkillid = int(skillid)+1
                    nextNextSkillid = int(skillid)+2
                    cursor3 = connection.cursor()
                    cursor3.execute("""UPDATE polls_progress
                        SET t_status = %s
                        WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", (1, nextSkillid, studentId))
                    cursor4 = connection.cursor()
                    cursor4.execute("""UPDATE polls_progress
                        SET t_status = %s
                        WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", (1, nextNextSkillid, studentId))
                    connection.commit()
                else:
                    nextSkillid = int(skillid)+1
                    cursor3 = connection.cursor()
                    cursor3.execute("""UPDATE polls_progress
                        SET t_status = %s
                        WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", (1, nextSkillid, studentId))
                    connection.commit()
        else:
            cursor2 = connection.cursor()
            cursor2.execute("""SELECT polls_progress.[mastery_progress]
            FROM polls_progress
            WHERE polls_progress.[skill]= %s AND polls_progress.[student_id] = %s""", (skillid, studentId))
            mas_progress = cursor2.fetchall()
            print mas_progress
            print mas_progress[0][0]
            if mas_progress[0][0] != "CM" :
                cursor2 = connection.cursor()
                cursor2.execute("""UPDATE polls_progress
                SET mastery_progress = %s
                WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", skillid, studentId))
                connection.commit()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        ) 
#get the mastery level, pass in and update the database.  Get the info from database
def mas_decision (mas2, stepCount, workStepNo, totalQue, totalTry, studentId, skillid, progressId, masLevel):
    print "inside mas_decision"
    print progressId
    cursor1 = connection.cursor()
    cursor1.execute("""SELECT polls_m_progress_details.[mastery], polls_m_progress_details.[mas_easy_progress], polls_m_progress_details.[mas_mod_progress], polls_m_progress_details.[mas_adv_progress]
    FROM polls_m_progress_details
    WHERE polls_m_progress_details.[progress_id]= %s """, [progressId])
    row_mastery = cursor1.fetchall()
    print row_mastery
    easyCount = row_mastery[0][1]
    modCount = row_mastery[0][2]
    chaCount = row_mastery[0][3]
    print "total Try", totalTry
    print "data type for total try", type(totalTry)
    print "total Que", totalQue
    print "data type for totalQue", type(totalQue)
    if mas2 == 1:
        print "mas_decision function if 1"
        if stepCount == workStepNo:
            if masLevel == "1":
                #update the esayCount in database
                easyCount = easyCount +1
                masCursor = connection.cursor()
                masCursor.execute("""UPDATE polls_m_progress_details
                SET mas_easy_progress = %s
                WHERE polls_m_progress_details.[progress_id]= %s""", [easyCount, progressId])
                if int(easyCount) == 2:
                    return 4, stepCount
                else:
                    return 3, stepCount
            elif masLevel == "2":
                #update the modCount in database
                modCount = modCount +1
                masCursor = connection.cursor()
                masCursor.execute("""UPDATE polls_m_progress_details
                SET mas_mod_progress = %s
                WHERE polls_m_progress_details.[progress_id]= %s""", [modCount, progressId])
                if int(modCount) == 2:
                    return 5, stepCount
                else:
                    return 3, stepCount
            else:
                #update the chaCount in database
                chaCount = chaCount +1
                masCursor = connection.cursor()
                masCursor.execute("""UPDATE polls_m_progress_details
                SET mas_adv_progress = %s
                WHERE polls_m_progress_details.[progress_id]= %s""", [chaCount, progressId])
                if int(chaCount) == 1:
                    return 6, stepCount
                else:
                    return 3, stepCount
        # then another function to check if the number required have been reached, if yes update the mastery level else continue
        else:
            print "increase step count when answer correct"
            print "mas_decision function 2"
            stepCount= int(stepCount)+1
            return 2, stepCount
    else:
        if int(totalTry) == int(totalQue):
            print "mas_decision function 1"
            return 1, stepCount
        else:
            print "mas_decision function 0"
            return 0, stepCount   



@csrf_exempt
def get_masworkingstepanswer(request):
    if request.method == 'POST':
        print "the working step from ajax"
        stephint =json.loads(request.POST.get('masstepanswer'))
        skillid = stephint['skill_id']
        masQueNum = stephint['QueNum']
        workStepNo = stephint['workStepNo']
        stepCount = stephint['stepCount']
        print "success get answer request"
        '''connect to the database to retrive the step answer using the skill id, question number and work step number '''
        curanswer = connection.cursor()
        curanswer.execute("""SELECT polls_mas_working.[masWorkStepAnswer]
        FROM polls_mas_working
        INNER JOIN  polls_mastery
        ON polls_mas_working.[mastery_id]=polls_mastery.[mastery]
        WHERE polls_mastery.[skill_id]= %s AND polls_mas_working.[masStepNo]= %s AND polls_mas_working.[mastery_id]=%s""", (skillid, stepCount, masQueNum))
        masStepAnswer = dictfetchall(curanswer)
        print masStepAnswer
        print type (masStepAnswer)

        print masStepAnswer[0]
        response_mas_answer = masStepAnswer[0]
        print response_mas_answer
        print type (response_mas_answer)
        print response_mas_answer['masWorkStepAnswer']
        print "FInished calling def workingstepanswer"
        return HttpResponse(
            json.dumps(response_mas_answer),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )


@csrf_exempt
def get_masworkingstephint(request):
    if request.method == 'POST':
        print "the working step from ajax"
        """get value from the user input and implicit data"""
        masstephint =json.loads(request.POST.get('masstephint'))
        skillid = masstephint['skill_id']
        masQueNum = masstephint['QueNum']
        workStepNo = masstephint['workStepNo']
        stepCount = masstephint['stepCount']
        print "success get hint"
        print skillid
        print masQueNum
        '''connect to the database to retrive the stepAnswer, hint using the skill id, question number and work step number '''
        curhint = connection.cursor()
        curhint.execute("""SELECT polls_mastery.[masHint]
        FROM polls_mastery
        INNER JOIN  polls_mas_working
        ON polls_mastery.[mastery]=polls_mas_working.[mastery_id]
        WHERE polls_mastery.[skill_id]= %s AND polls_mastery.[mastery]= %s""", (skillid, masQueNum))
        masStepHint = dictfetchall(curhint)
        print masStepHint
        print type (masStepHint)

        print masStepHint[0]
        response_mashint = masStepHint[0]
        print response_mashint
        print type (response_mashint)
        print response_mashint['masHint']
        # c1, c2 = checkworking(post_workingstep, skillid, exeQueNum)
        # print c1
        print "FInished calling def checkworkingstep"
        return HttpResponse(
            json.dumps(response_mashint),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def getMasteryLevel (easyCount, modCount, chaCount):
    if easyCount == 2:
        print "update easy level record"
        if modCount == 2:
            print "update moderate level record"
            if chaCount ==1:
                print "update mastery progress report"
                return "4"
            else:
                print "continue attempting challenging questions"
                return "3"
        else:
            print "continue attempting moderate difficulty questions"
            return "2"
    else:
        print "continue attempting easy level questions"
        return "1"

@csrf_exempt
def get_tutorial(request):
    if request.method == 'POST':
        get_tutorial =json.loads(request.POST.get('get_tutorial'))
        skillid = get_tutorial['skill_id']
        tutorialNo = get_tutorial['tutorialNo']
        studentId = get_tutorial['studentId']
        
        print skillid
        print tutorialNo
        '''connect to the database to retrive the stepAnswer, hint using the skill id, question number and work step number '''
        curtutorial = connection.cursor()
        curtutorial.execute("""SELECT polls_tutorial.[skill_id], polls_tutorial.[tutorialNo], polls_tutorial.[tutorial_animation], polls_tutorial.[tutName], polls_tutorial.[tutLevel]
        FROM polls_tutorial 
        WHERE polls_tutorial.[skill_id]= %s AND polls_tutorial.[tutorialNo]= %s""", (skillid, tutorialNo))
        tutorialAni = dictfetchall(curtutorial)
        print "tutorial", tutorialAni
        print type (tutorialAni)
        print tutorialAni[0]['skill_id']
        print tutorialAni[0]['tutorialNo']
        

        tutorial_data = {}
        tutorial_data['skill_id'] = tutorialAni[0]['skill_id']
        tutorial_data['tutorialNo'] = tutorialAni[0]['tutorialNo']
        tutorial_data['tutorial_file'] = tutorialAni[0]['tutorial_animation']
        tutorial_data['tutName'] = tutorialAni[0]['tutName']
        tutorial_data['tutLevel'] = tutorialAni[0]['tutLevel']

        return HttpResponse(
            json.dumps(tutorial_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

@csrf_exempt
def update_tutorial_progress (request):
    if request.method == 'POST':
        update_tutorial_progress =json.loads(request.POST.get('update_tutorial_progress'))
        skillid = update_tutorial_progress['skill_id']
        tutorialNo = update_tutorial_progress['tutorialNo']
        studentId = update_tutorial_progress['studentId']
        totalAni = update_tutorial_progress['total_ani']
    
        print "tutorial progress info", skillid, tutorialNo, studentId
    
        nextTutorialNo = tutorialNo + 1
        print nextTutorialNo
        print totalAni

        print skillid
        print type(skillid)
        '''using the params of skillid from the previous page, query from the database and retrieve the student progress in the exercise section'''
        cursor = connection.cursor()
        cursor.execute("""SELECT polls_progress.[progress]
        FROM polls_progress
        WHERE polls_progress.[student_id]= %s AND polls_progress.[skill] = %s""", (studentId, skillid))
        progressid = cursor.fetchall()
        print "Progress id", progressid[0][0]
        '''get to the question number'''

        '''get the current t_progress and compare, if less than update, else ignore'''
        cursor1 = connection.cursor()
        cursor1.execute("""SELECT polls_t_progress_details.[tutorial]
            FROM polls_t_progress_details
            WHERE polls_t_progress_details.[progress_id] = %s """, [progressid[0][0]])
        current_tutorialInfo = cursor1.fetchall()
        print current_tutorialInfo[0][0]

        print "nextTutorialNo", nextTutorialNo
        print totalAni
        if int(nextTutorialNo) <= int(totalAni):
            if int(nextTutorialNo) > int(current_tutorialInfo[0][0]):
                print "we are in"
                cursor2 = connection.cursor()
                cursor2.execute("""UPDATE polls_t_progress_details
                SET tutorial = %s
                WHERE polls_t_progress_details.[progress_id]= %s""", [nextTutorialNo, progressid[0][0]])
                
                cursor3 = connection.cursor()
                cursor3.execute("""UPDATE polls_progress
                SET tutorial_progress = %s
                WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("NC", skillid, studentId))

        else:
            print "going to update tutorial progress table"
            cursor4 = connection.cursor()
            cursor4.execute("""UPDATE polls_progress
            SET tutorial_progress = %s,
                e_status =%s
            WHERE polls_progress.[skill] = %s AND polls_progress.[student_id] = %s""", ("CM", 1, skillid, studentId))
        
        nextTutorial_data = {}
        nextTutorial_data['skill_id'] = skillid
        nextTutorial_data['tutorialNo'] = nextTutorialNo
        nextTutorial_data['studentId'] = studentId
        nextTutorial_data['total_ani'] = totalAni 

        return HttpResponse(
            json.dumps(nextTutorial_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
