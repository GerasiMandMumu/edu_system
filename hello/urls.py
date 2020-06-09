from django.urls import path
from firstapp import views
from django.contrib import admin

urlpatterns = [
	#начало
	path('', views.index),
	
	# профиль
	path('profile', views.profile),
	# настройки
	path('settings', views.settings),
	# изменение
	path('edit/<int:id>/', views.edit),
	# выход
	path('exit', views.exit),
	# содержание
	path('content', views.content),
	
	# главная
	path('welcome', views.welcome),
	# о нас	
	path('about', views.about),
	# контакты
	path('contacts', views.contacts),
	# документы
	path('get_document/<int:id>/', views.get_document),
	# начать учиться
	path('start', views.start),
	
	#Регистрация и авторизация
	path('login', views.login),
	path('register', views.register),
	#авторизация
	path('login_window', views.login_window),
	#регистрация
	path('register_window', views.register_window),
	
	#Переход к тесту
	path('step/<int:id>/', views.step),
	
	#Администрирование
	path('admin/', admin.site.urls),
]