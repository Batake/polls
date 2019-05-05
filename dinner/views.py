from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Menu, Dinner


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'dinner/index.html'
    context_object_name = 'latest_dinner_list'
    
    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Dinner.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Dinner
    template_name = 'dinner/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Dinner.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Dinner
    template_name = 'dinner/result.html'

def vote(request, dinner_id):
    dinner = get_object_or_404(Dinner, pk=dinner_id)
    try:
        selected_menu = dinner.menu_set.get(pk=request.POST['menu'])
    except (KeyError, Menu.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'dinner/detail.html', {
            'dinner': dinner,
            'error_message': "You didn't select a menu.",
        })
    else:
        selected_menu.votes += 1
        selected_menu.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data. 
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('dinner:results', args=(dinner.id,)))