from asyncio.windows_events import NULL
from random import choices
from django.db import models

# Create your models here.
'''
subject master
subject_id
subject_name
'''

branch_list=(
        ('CS','Computer Science'),
        ('EC','Electronics and communication engineering'),
        ('IT','Information Technology'),
        ('ME','Mechanical Engineering'),
        ('CE','Civil Engineering'),
        ('MCA','Master in Computer Application'),
        ('Oth','Others'),

)

sem_list = (
            ('1', 'First'),
            ('2', 'Second'),
            ('3', 'Third'),
            ('4', 'Fourth'),
            ('5', 'Fifth'),
            ('6', 'Sixth'),
            ('7', 'Seventh'),
            ('8', 'Eighth'),
)




class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='UserID')
    first_name = models.CharField(max_length=20, db_column='First_Name')
    last_name = models.CharField(max_length=20, db_column='Second_Name')
    college = models.CharField(max_length=100, db_column='College_Name')
    branch = models.CharField(max_length=20, choices=branch_list,null=True)
    sem = models.CharField(max_length=1, choices=sem_list,null=True)
    yopassing = models.BooleanField(default=False,db_column='YearofPassing')
    email = models.EmailField(max_length=100, db_column='Email')
    mobileno = models.CharField(max_length=10,db_column='MobileNo')


    def __str__(self) -> str:
        return str(self.first_name)

    class Meta:
        db_table = 'UserProfile'



class SubjectMaster(models.Model):
    subject_id = models.AutoField(primary_key=True, db_column='SubjectID')
    subject_name = models.CharField(max_length=30, db_column='SubjectName')
    
    def __str__(self) -> str:
        return str(self.subject_id)

    class Meta:
        db_table = 'SubjectMaster'



class TopicMaster(models.Model):
    topic_id = models.AutoField(primary_key=True, db_column='TopicID')
    topic_name = models.CharField(max_length=120, db_column='TopicName')

    def __str__(self) -> str:
        return str(self.topic_id)

    class Meta:
        db_table = 'TopicMaster'

class SubjectDetail(models.Model):

    subject_id = models.ForeignKey('SubjectMaster', on_delete=models.SET_NULL, null=True, db_column='SubjectID')
    topic_id = models.ForeignKey('TopicMaster', on_delete=models.SET_NULL, null=True, db_column='TopicID')
    noofTest = models.IntegerField(db_column= 'MunberofTest')
    totalMarks =models.IntegerField(db_column='TotalMarks')
    passing_marks = models.IntegerField(db_column='PassingMarks')


    def __str__(self) -> str:
        return str(self.subject_id)

    class Meta:
        db_table = 'SubjectDetail'
    
ans_choice = (
    ('N','------'),
    ('A', 'Option-A'),
    ('B', 'Option-B'),
    ('C', 'Option-C'),
    ('D', 'Option-D')
)

class QuestionsBank(models.Model):
    subject_id = models.ForeignKey('SubjectMaster', on_delete=models.CASCADE, null=True, db_column='SubjectID')
    topic_id = models.ForeignKey('TopicMaster', on_delete=models.SET_NULL, null=True, db_column='TopicID' )
    noofQues = models.IntegerField(db_column='NumberofQues')
    answer= models.CharField( max_length=2, db_column='Answer')
    choice= models.CharField(max_length=1, choices=ans_choice, default='N', db_column='UserChoice')
    questions = models.CharField(max_length=100, db_column='Questions')
    option_1 = models.CharField(max_length=100, db_column='Option_1')
    option_2 = models.CharField(max_length=100, db_column='Option_2')
    option_3 = models.CharField(max_length=100, db_column='Option_3')
    option_4 = models.CharField(max_length=100, db_column='Option_4')


    def __str__(self) -> str:
        return str(self.topic_id)

    class Meta:
        db_table = 'QuestionBank'


   

class Student_review(models.Model):
    student_id = models.IntegerField(db_column = 'StudentID')
    questionsAttempted = models.IntegerField(db_column='QuesAttempted', default=0)
    rightAnswers = models.IntegerField(db_column='RightAnswers', default=0)
    wrongAnswers = models.IntegerField(db_column='WrongAnswers', default=0)
    marksObtained = models.IntegerField(db_column='MarksObtained', default=0)
    grade = models.CharField(max_length=2, db_column='Grade')


    def __str__(self) -> str:
        return str(self.student_id)

    class Meta:
        db_table = 'Student_review'


class Leaderboard(models.Model):
    student_id = models.IntegerField(db_column='StudentID')
    marksObtained = models.IntegerField(db_column='MarksObtained')
    rank = models.IntegerField(db_column='Rank')

    def __str__(self) -> str:
        return str(self.student_id)

    class Meta:
        db_table = 'Leaderboard'

'''
class UserDetails(models.Model):
    userID = models.CharField(max_length=50,)
    firstname = models.CharField(max_length=)
'''