from django.contrib import admin
from .models import Exercise
from .models import Skill
from .models import Exe_Working
from .models import Exe_Possible
from .models import Mastery
from .models import Mas_Working
from .models import Tutorial


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exeQueNum', 'exeQueText', 'exeQueExpression')


class WorkingAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'exeWorkStepNo', 'exeStepAnswer')



class PossibleAdmin(admin.ModelAdmin):
    list_display = ('exeWorkingStep', 'exePossibleMistake', 'exeMistakeFeedback')

class MasteryAdmin(admin.ModelAdmin):
	list_display = ('masQueText', 'masQueExpression', 'masTotalWorkSteps')

class MasAnswerAdmin (admin.ModelAdmin):
	list_display = ('mastery', 'masWorkStepAnswer', 'masStepNo')

class TutorialAdmin (admin.ModelAdmin):
	list_display = ('skill', 'tutorialNo', 'tutorial_animation', 'tutName', 'tutLevel')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Skill)
admin.site.register(Exe_Working, WorkingAdmin)
admin.site.register(Exe_Possible, PossibleAdmin)
admin.site.register(Mastery, MasteryAdmin)
admin.site.register(Mas_Working, MasAnswerAdmin)
admin.site.register(Tutorial, TutorialAdmin)
# Register your models here.
