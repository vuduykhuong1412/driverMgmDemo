from django.contrib import admin 
from django.urls import path
from driverManagement import views

app_name = "driverManagement"

urlpatterns = [ 
	path('admin/', admin.site.urls), 
    path(r'', views.index, name='index'),
	path('', views.HomeView.as_view()), 
	# path('test-api', views.get_data), 
	path('api', views.ChartData.as_view())
] 
