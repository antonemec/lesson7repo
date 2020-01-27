from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from students_app.models import Student
from students_app.forms import StudentsAddForm, ContactForm


# ----------------------------------------------------------------------------
# Вьюхи для студентов
# ----------------------------------------------------------------------------
def generate_student(request):
    student = Student.generate_students()
    response = f'{student.get_all_info()}'
    return render(request,
                  'generate_student.html',
                  context={'gen_s': response})


# ----------------------------------------------------------------------------
def students_list(request):
    queryset = Student.objects.all().select_related('group')
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(first_name__istartswith=fn) |
                                   Q(last_name__startswith=fn) |
                                   Q(email__startswith=fn))

    return render(request,
                  'students_list.html',
                  context={'students': queryset})


# ----------------------------------------------------------------------------
def students_add(request):
    if request.method == 'POST':
        form = StudentsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-s'))
        else:
            form = StudentsAddForm()
    else:
        form = StudentsAddForm()

    return render(request,
                  'students_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
def students_edit(request, pk):
    # reverse('edit-s', args=[{{ student.id }}])
    # reverse('edit-s', )
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound(f"Student with id {pk} not found")

    if request.method == 'POST':
        form = StudentsAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-s'))
    else:
        form = StudentsAddForm(instance=student)

    return render(request,
                  'students_edit.html',
                  context={'form': form, 'pk': pk})


# ----------------------------------------------------------------------------
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-s'))
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})
