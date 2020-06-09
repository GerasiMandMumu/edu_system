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
	test = models.OneToOneField(Tests, on_delete = models.CASCADE, primary_key = False, blank=True)
	theory = models.OneToOneField(Theory, on_delete = models.CASCADE, primary_key = False, blank=True)


#ДАННЫЕ О ПОЛЬЗОВАТЕЛЕ
#Компания
class Company(models.Model):
	company_title = models.TextField(blank=False)
	
#Профиль
class Profile(models.Model):
	name = models.CharField(max_length=20, blank=False)
	surname = models.CharField(max_length=20, blank=False)
	patronymic = models.CharField(max_length=20, blank=True)
	birth = models.DateField(blank=False)
	login = models.CharField(unique=True, max_length=20, blank=False)
	email = models.EmailField(unique=True, blank=False)
	password = models.CharField(max_length=20, blank=False)
	phone_number = models.CharField(unique=True, max_length=10, blank=False)
	knowledge_rating = models.IntegerField(default=0)
	company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=False)
	current_step = models.ForeignKey(Step, on_delete=models.DO_NOTHING, blank=False)

#СЕРТИФИКАТЫ
class Certificates(models.Model):
	title = models.CharField(max_length=20)
	content = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)


#ФОРУМ
class Comments(models.Model):
	comment = models.TextField()
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
	step = models.OneToOneField(Step, on_delete = models.CASCADE, primary_key = False)
	
