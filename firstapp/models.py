from django.db import models
from django.forms import ModelForm

#ДОКУМЕНТЫ
class Documents(models.Model):
	title = models.TextField()
	content = models.TextField()

#ДАННЫЕ О КУРСЕ
#Тест
class Tests(models.Model):
	question = models.TextField()
	type = models.IntegerField()
	key = models.IntegerField()
	content = models.TextField() 
#Теория
class Theory(models.Model):
	content = models.TextField()
#Шаг
class Step(models.Model):
	title = models.TextField() 
	test = models.OneToOneField(Tests, on_delete = models.CASCADE, blank=True)
	theory = models.OneToOneField(Theory, on_delete = models.CASCADE, blank=True)


#ДАННЫЕ О ПОЛЬЗОВАТЕЛЕ
#Компания
class Company(models.Model):
	company_title = models.TextField()
	
#Профиль
class Profile(models.Model):
	name = models.CharField(max_length=20)
	surname = models.CharField(max_length=20)
	patronymic = models.CharField(max_length=20, blank=True)
	birth = models.DateField()
	login = models.CharField(unique=True, max_length=20)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=20)
	phone_number = models.CharField(unique=True, max_length=10)
	knowledge_rating = models.IntegerField(default=0)
	company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
	current_step = models.ForeignKey(Step, on_delete=models.DO_NOTHING)

#СЕРТИФИКАТЫ
class Certificates(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


#ФОРУМ
class Comments(models.Model):
	comment = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	step = models.OneToOneField(Step, on_delete = models.CASCADE, primary_key = False)
	
