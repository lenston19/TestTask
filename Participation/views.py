from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from Participation.models import Participant
from .forms import ParticipantForm

# Create your views here.

def lk(request):
    return render(request, 'lk/lk.html')

def succes(request):
    return render(request, 'main/participant_succes.html')

class participation(CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'main/participant_create_form.html'
    success_url = '/ViewParticipation/succes/'

class participationList(ListView):
    paginate_by = 10
    model = Participant
    template_name = 'lk/lk.html'

