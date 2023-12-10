from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View

from rest_framework.views import APIView    
from rest_framework.response import Response
from .models import DriverInformation

from django.views import generic
from django.template import loader
#from django.http import JsonResponse 


# Create your views here.
# def IndexView(generic.ListView):
#     template_name = 'driverManagement/index.html'
#     context_object_name = 'latest_driverManagement_list'
    
#     def get_queryset(self):
#         return driverManagement.objects.order_by('firstLogInTime')[:5]

class DetailView(generic.DetailView):
    model = DriverInformation
    template_name = 'driverManagement/detail.html'

class ResultsView(generic.DetailView):
    model = DriverInformation
    template_name = 'driverManagement/results.html'


def index(request):
    latest_driverManagement_list = DriverInformation.objects.order_by('drivingDuration')[:5]
    template = loader.get_template('driverManagement/index.html')
    context = {
        'latest_driverManagement_list' : latest_driverManagement_list,
    }
    return HttpResponse(template.render(context, request))



class HomeView(View): 
    def get(self, request, *args, **kwargs): 
        return render(request, 'driverManagement/index.html') 

class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            'January', 
            'February',  
            'March',  
            'April',  
            'May',  
            'June',  
            'July'
        ] 
        chartLabel = "my data"
        chartdata = [0, 10, 5, 2, 20, 30, 45] 
        data ={ 
            "labels":labels, 
            "chartLabel":chartLabel, 
            "chartdata":chartdata, 
        } 
        return Response(data) 
