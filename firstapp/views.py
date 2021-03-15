from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse
from .models import Step, Documents, Company, Profile
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


#старт
def index(request):
	return render(request, "welcome.html")
# проверка авторизации
def read_data(request):
	flag = False
	if "login" in request.session and "password" in request.session:
		flag = True
	return flag


# ГЛАВНАЯ СТРАНИЦА
# главная
def welcome(request):
	return redirect(index)
# контакты
def contacts(request):
	return render(request, "contacts.html")
# информации о предприятии
def about(request):
	return render(request, "about.html")
# начать учиться	
def start(request):
	if read_data(request):
		#s = request.session["login"]
		#profile = Profile.objects.get(login=s)
		return redirect(profile)
	else:
		return redirect(login_window)
# документ
def get_document(request, id):
	docs = Documents.objects.get(id=id)
	return render(request, "docs.html", {"docs": docs})
	

# ОКНО ПРОФИЛЯ
# профиль
def profile(request):
	s = request.session["login"]
	profile = Profile.objects.get(login=s)	
	return render(request, "profile.html", {"profile": profile})
# настройки
def settings(request):
	s = request.session["login"]
	profile = Profile.objects.get(login=s)
	return render(request, "settings.html", {"profile": profile})
# выход
def exit(request):
	try:
		del request.session["login"]
		del request.session["password"]
		return redirect(welcome)
	except:
		return redirect(welcome)
# изменение данных профиля
def edit(request, id):
	try:
		s = request.session["login"]
		profile = Profile.objects.get(login=s)
		if request.method == "POST":
			profile.name = request.POST.get("name")
			profile.surname = request.POST.get("surname")
			profile.patronymic = request.POST.get("patronymic")
			profile.email = request.POST.get("email")
			profile.save()
			return redirect(settings)
	except:
		return HttpResponseNotFound("<h2>Ошибка</h2>")	


# ОБУЧЕНИЕ
# содержание курса
def content(request):
	s = request.session["login"]
	profile = Profile.objects.get(login=s)
	return render(request, "content.html", {"profile": profile})
# страница с тестом
def step(request, id):
	steps = Step.objects.get(id=id)
	s = request.session["login"]
	profile = Profile.objects.get(login=s)
	return render(request, "lesson.html", {"steps": steps, "profile": profile})


# АВТОРИЗАЦИЯ\РЕГИСТРАЦИЯ
# для отображения окна авторизации
def login_window(request):
	if read_data(request):
		return redirect(profile)
	else:
		return render(request, "login.html")
# для отображения окна регистрации	
def register_window(request):
	if read_data(request):
		return redirect(profile)
	else:
		return render(request, "register.html")
# вход 
def login(request):	
	try:
		if request.method == "POST":
			input_login = request.POST.get("login")
			input_password = request.POST.get("password")
			prof = Profile.objects.get(login=request.POST.get("login"))
			base_login = prof.login
			base_password = prof.password
			if base_login == input_login and base_password == input_password:
				request.session["login"] = base_login
				request.session["password"] = base_password
				prof = Profile.objects.get(login=base_login)
				return redirect(profile)
			else:
				return HttpResponse("<h2>Неверные данные</h2>")
	except:
		return render(request, "login.html", {"msg": "Ошибка входа"})
# регистрация
def register(request):
	try:
		if request.method == "POST":		
			# Профиль
			profile = Profile()
			profile.name = request.POST.get("name")	
			profile.surname = request.POST.get("surname")
			profile.patronymic = request.POST.get("patronymic")
			profile.birth = request.POST.get("birth")		
			# Данные компании
			title = request.POST.get("company_title")
			company = Company.objects.filter(company_title=title).exists()
			if company:
				company = Company.objects.get(company_title=title)
				profile.company = company
			else:
				company = Company()
				company.company_title = title
				profile.company = company
				
			profile.login = request.POST.get("login")
			profile.password = request.POST.get("password")
			profile.email = request.POST.get("email")
			profile.phone_number = request.POST.get("phone_number")
			try:
				validators.validate_email(profile.email)
			except ValidationError:
				return HttpResponseNotFound("<h2>Ошибка при вводе эл почты...</h2>")
			
			# Шаг
			step = Step.objects.get(id=1)
			profile.current_step = step
			
			company.save()
			profile.save()
			return redirect(welcome)	
	except:
		return render(request, "register.html", {"msg": "Ошибка"})
	