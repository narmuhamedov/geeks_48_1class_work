from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


# create todo_list
class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)




# def create_todo_view(request):
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form =  forms.TodoForm()
#     return render(request, template_name='todo/create_todo.html',
#                   context={'form': form})

# Read list detail
@method_decorator(cache_page(60*15), name='dispatch')
class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    model = models.TodoModel

    def get_queryset(self):
        todos = cache.get('todos')
        if not todos:
            todos = self.model.objects.all().order_by('-id')
            cache.set('todos', todos, 60*15)
        return todos

class TodoDetailView(generic.DetailView):
    template_name = 'todo/todo_detail.html'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)




# def todo_list_view(request):
#     if request.method == 'GET':
#         todo_list = models.TodoModel.objects.all().order_by("-id")
#         context = {'todo_list': todo_list}
#         return render(request, template_name='todo/todo_list.html',
#                       context=context)

# def todo_detail_view(request, id):
#     if request.method == 'GET':
#         todo_id = get_object_or_404(models.TodoModel, id=id)
#         context = {'todo_id': todo_id}
#         return render(request, template_name='todo/todo_detail.html',
#                       context=context)

# UPDATE TODO_TASK
class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)





# def todo_update_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     if request.method == 'POST':
#         form = forms.TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = forms.TodoForm(instance=todo_id)
#     return render(request, template_name='todo/update_todo.html',
#                   context={'form': form, 'id': id})

#Delete TodoTask
class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)




# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(models.TodoModel, id=id)
#     todo_id.delete()
#     return redirect('todo_list')