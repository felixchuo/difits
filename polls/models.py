from django.db import models
from django import forms

# Create your models here.

    


class Student (models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    GRADE = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )

    SCHOOL = (
        ('1', 'KOLEJ DPAH ABDILLAH'),
        ('2', 'SMK BATU LINTANG'),
        ('3', 'SMK KUCHING HIGH'),
        ('4', 'SMK GREEN ROAD'),
        ('5', 'SMK SG. MAONG'),
    )
    student = models.AutoField(primary_key=True)
    student_loginid = models.IntegerField(default=0)
    student_firstname = models.CharField(max_length=200)
    student_lastname = models.CharField(max_length=200)
    student_class = models.CharField(max_length=10)
    student_school = models.CharField(max_length=1, choices=SCHOOL)
    student_dob = models.DateTimeField('Date of Birth')
    student_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_pmr = models.IntegerField(default=0)
    student_maths = models.CharField(max_length=1, choices=GRADE)


class Progress (models.Model):
    PROGRESS = (
        ('NA', 'NOT ATTEMPTED'),
        ('NC', 'NOT COMPLETED'),
        ('CM', 'COMPLETED'),
    )

    progress = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student)
    skill = models.IntegerField()
    tutorial_progress = models.CharField(max_length=2, choices=PROGRESS)
    mastery_progress=models.CharField(max_length=2, choices=PROGRESS)
    exercise_progress=models.CharField(max_length=2, choices=PROGRESS, default='NA')
    t_status = models.IntegerField(default=0)
    e_status = models.IntegerField(default=0)
    m_status = models.IntegerField(default=0)


class Skill (models.Model):
    skill = models.AutoField(primary_key=True)
    #student = models.ForeignKey(Student)
    skill_name = models.CharField(max_length = 200)

    def __unicode__(self):
        return u'%s %s' % (self.skill, self.skill_name)



class Tutorial (models.Model):
    LEVEL = (
        ('1', 'Simple'),
        ('2', 'Moderate'),
        ('3', 'Challenging'),
    )
    tutorial = models.AutoField(primary_key=True)
    tutorialNo = models.IntegerField()
    skill = models.ForeignKey(Skill)
    tutorial_animation = models.CharField(max_length=255)
    tutName = models.CharField(max_length=255)
    tutLevel = models.CharField(max_length=1, choices=LEVEL)
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.skill, self.tutorialNo, self.tutorial_animation, self.tutName, self.tutLevel)

class Mastery (models.Model):
    LEVEL = (
        ('1', 'Simple'),
        ('2', 'Moderate'),
        ('3', 'Challenging'),
    )

    NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )

    mastery = models.AutoField(primary_key=True)
    skill = models.ForeignKey(Skill)
    masQueText = models.CharField(max_length=255)
    masQueExpression = models.CharField(max_length=255)
    masQueLevel = models.CharField(max_length=1, choices=LEVEL)
    masTotalWorkSteps = models.CharField(max_length=255)
    masHint = models.CharField(max_length=255)
    masRightFeedback = models.CharField(max_length=255, null=True )
    masWrongFeedback = models.CharField(max_length=255, null=True)
    def __unicode__(self):
        return u'%s %s %s' % (self.masQueText, self.masQueExpression, self.masTotalWorkSteps)



class Mas_Working (models.Model):
    masWorkingStep = models.AutoField(primary_key=True)
    mastery = models.ForeignKey(Mastery)
    masWorkStepAnswer = models.CharField(max_length=255)
    masStepNo = models.IntegerField()
    def __unicode__(self):
        return u'%s %s %s' % (self.mastery, self.masWorkStepAnswer, self.masStepNo)


class T_Progress_Details (models.Model):
    tpd = models.AutoField(primary_key=True)
    progress = models.ForeignKey(Progress)
    student = models.IntegerField()
    tutorial = models.IntegerField(Tutorial)
    animation_progress = models.CharField(max_length=255)

class M_Progress_Details (models.Model):
    mpd = models.AutoField(primary_key=True)
    progress = models.ForeignKey(Progress)
    student = models.IntegerField()
    mastery = models.IntegerField(blank=True)
    question_progress = models.CharField(max_length=10)
    mas_easy_progress = models.IntegerField()
    mas_mod_progress = models.IntegerField()
    mas_adv_progress = models.IntegerField()
    mastery_score = models.IntegerField()

class Exe_Progress_Details (models.Model):
    exeProDetails = models.AutoField(primary_key=True)
    progress = models.ForeignKey(Progress)
    student = models.IntegerField()
    exercise = models.IntegerField(blank=True)
    exeQueNumStatus = models.IntegerField()

class PostForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_firstname', 'student_lastname', 'student_gender', 'student_dob', 'student_school', 'student_class', 'student_maths', 'student_pmr') 


class Exercise (models.Model):
    LEVEL = (
        ('1', 'Simple'),
        ('2', 'Moderate'),
        ('3', 'Challenging'),
    )

    NUMBER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
    )

    exercise = models.AutoField(primary_key=True)
    skill = models.ForeignKey(Skill)
    exeQueNum = models.IntegerField()
    exeQueText = models.CharField(max_length=255)
    exeQueExpression = models.CharField(max_length=255)
    exeQueLevel = models.CharField(max_length=1, choices=LEVEL)
    exeTotalWorkSteps = models.CharField(max_length=1, choices=NUMBER)

    def __unicode__(self):
        return u'%s %s %s' % (self.exeQueNum, self.exeQueText, self.exeQueExpression)


class Exe_Working (models.Model):
    exeWorkingStep = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(Exercise)
    exeWorkStepNo = models.IntegerField()
    exeStepAnswer = models.CharField(max_length=255)
    exeStepHint = models.CharField(max_length=255)
    exeHintVisualAid = models.CharField(max_length=255)
    exeGeneralFeedback = models.CharField(max_length=255)
    exeCongratulatory = models.CharField(max_length=255)
    def __unicode__(self):
        return u'%s %s %s' % (self.exercise, self.exeWorkStepNo, self.exeStepAnswer)


class Exe_Possible (models.Model):
    exe_Possible = models.AutoField(primary_key=True)
    exeWorkingStep = models.ForeignKey(Exe_Working)
    exePossibleMistake = models.CharField(max_length=255)
    exeMistakeFeedback = models.CharField(max_length=255)
    exeFeedbackVisualAid = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s %s %s' % (self.exeWorkingStep, self.exePossibleMistake, self.exeMistakeFeedback)



