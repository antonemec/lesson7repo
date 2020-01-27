from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from teachers_app.models import Teacher
from teachers_app.forms import TeachersAddForm
from django.db.models import Q
from django.urls import reverse
from datetime import datetime


# ----------------------------------------------------------------------------
# Вьюхи для  учителей
# ----------------------------------------------------------------------------
def generate_teacher(request):
    teacher = Teacher.generate_teacher()
    response = f'{teacher.get_info()}'
    return render(request,
                  'gen_teacher.html',
                  context={'gen_t': response})


# ----------------------------------------------------------------------------
def teachers_list(request):
    queryset = Teacher.objects.all()
    """response = ''"""
    # print("request.GET.get('first_name')")
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(first_name__startswith=fn) |
                                   Q(last_name__startswith=fn) |
                                   Q(email__startswith=fn))
    """for teacher in queryset:
        response += teacher.get_info() + '<br> ______________ <br><br>'"""
    # return HttpResponse(response)
    # print('queryset.query')
    # print(queryset.query)
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': queryset})


# ----------------------------------------------------------------------------

def teachers_add(request):
    if request.method == 'POST':
        form = TeachersAddForm(request.POST)
        if form.is_valid():
            form.save()
            """log = open('logs.txt', 'a')
            log.write(f'{datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), f} + \n')
            log.close()"""
            return HttpResponseRedirect(reverse('list-t'))
    else:
        form = TeachersAddForm()

    return render(request,
                  'teachers_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
def teachers_edit(request, pk):
    try:
        teacher = Teacher.objects.get(id=pk)
    except Teacher.DoesNotExist:
        return HttpResponseNotFound(f"Teacher with id {pk} not found")

    if request.method == 'POST':
        form = TeachersAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            """log = open('logs.txt', 'a')
            log.write(f'{datetime.now().strftime("%A, %d. %B %Y %I:%M%p"), f} + \n')
            log.close()"""
            return HttpResponseRedirect(reverse('list-t'))
    else:
        form = TeachersAddForm(instance=teacher)

    return render(request,
                  'teachers_edit.html',
                  context={'form': form, 'pk': pk})
