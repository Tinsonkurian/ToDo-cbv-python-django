from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def index(request):
    dict_task = {
        'task1': Todo.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        priority = request.POST['priority']
        date = request.POST['date']

        task = Todo(
            name=name,
            priority=priority,
            date=date
        )
        task.save()
        print('inserted')
        return redirect('/')
    
    return render(request, 'index.html', dict_task)

class Tasklistview(ListView):
    model = Todo
    context_object_name = 'task1'
    template_name='index.html'

class Taskdetailview(DetailView):
    model = Todo
    context_object_name = 'task'
    template_name='details.html'

class Taskupdateview(UpdateView):
    model = Todo
    context_object_name = 'task'
    template_name='update.html'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})
    
class Taskdeleteview(DeleteView):
    model = Todo
    template_name='delete.html'
    success_url = reverse_lazy('cbvindex')
