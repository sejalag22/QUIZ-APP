# Generated by Django 4.0.5 on 2022-07-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(db_column='StudentID')),
                ('marksObtained', models.IntegerField(db_column='MarksObtained')),
                ('rank', models.IntegerField(db_column='Rank')),
            ],
        ),
        migrations.CreateModel(
            name='Student_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(db_column='StudentID')),
                ('questionsAttempted', models.IntegerField(db_column='QuesAttempted', default=0)),
                ('rightAnswers', models.IntegerField(db_column='RightAnswers', default=0)),
                ('wrongAnswers', models.IntegerField(db_column='WrongAnswers', default=0)),
                ('marksObtained', models.IntegerField(db_column='MarksObtained', default=0)),
                ('grade', models.CharField(db_column='Grade', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMaster',
            fields=[
                ('subject_id', models.AutoField(db_column='SubjectID', primary_key=True, serialize=False)),
                ('subject_name', models.CharField(db_column='SubjectName', max_length=30)),
            ],
            options={
                'db_table': 'SubjectMaster',
            },
        ),
        migrations.CreateModel(
            name='TopicMaster',
            fields=[
                ('topic_id', models.AutoField(db_column='TopicID', primary_key=True, serialize=False)),
                ('topic_name', models.CharField(db_column='TopicName', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noofTest', models.IntegerField(db_column='MunberofTest')),
                ('totalMarks', models.IntegerField(db_column='TotalMarks')),
                ('passing_marks', models.IntegerField(db_column='PassingMarks')),
                ('subject_id', models.ForeignKey(db_column='SubjectID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizapp.subjectmaster')),
                ('topic_id', models.ForeignKey(db_column='TopicID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizapp.topicmaster')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noofQues', models.IntegerField(db_column='NumberofQues')),
                ('answer', models.CharField(db_column='Answer', max_length=2)),
                ('choice', models.CharField(choices=[('N', '------'), ('A', 'Option-A')], db_column='UserChoice', default='N', max_length=1)),
                ('questions', models.CharField(db_column='Questions', max_length=100)),
                ('option_1', models.CharField(db_column='Option_1', max_length=100)),
                ('option_2', models.CharField(db_column='Option_2', max_length=100)),
                ('option_3', models.CharField(db_column='Option_3', max_length=100)),
                ('option_4', models.CharField(db_column='Option_4', max_length=100)),
                ('subjectID', models.ForeignKey(db_column='SubjectID', null=True, on_delete=django.db.models.deletion.CASCADE, to='quizapp.subjectmaster')),
                ('topicID', models.ForeignKey(db_column='TopicID', null=True, on_delete=django.db.models.deletion.SET_NULL, to='quizapp.topicmaster')),
            ],
        ),
    ]
