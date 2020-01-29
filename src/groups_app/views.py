from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse

from groups_app.models import Group
from groups_app.forms import GroupsAddForm

# ----------------------------------------------------------------------------
# Вьюхи для групп
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
def generate_group(request):
    group = Group.generate_group()
    response = f'{group.get_info()}'
    return render(request,
                  'gen_group.html',
                  context={'gen': response})


# ----------------------------------------------------------------------------
def groups_list(request):
    queryset = Group.objects.all()
    response = ''

    # print("request.GET.get('group_name')")
    fn = request.GET.get('data')
    if fn:
        queryset = queryset.filter(Q(name__startswith=fn) |
                                   Q(id__startswith=fn))
    """for group in queryset:
        response += group.get_info() + '<br> ______________ <br><br>'"""
    """return render(request,
                  'groups_list.html',
                  context={'groups_list': response})"""
    return render(request,
                  'groups_list.html',
                  context={'groups_list': queryset})


# ----------------------------------------------------------------------------

def groups_add(request):
    if request.method == 'POST':
        form = GroupsAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupsAddForm()

    return render(request,
                  'groups_add.html',
                  context={'form': form})


# ----------------------------------------------------------------------------
def groups_edit(request, pk):
    try:
        group = Group.objects.get(id=pk)
    except Group.DoesNotExist:
        return HttpResponseNotFound(f"Group with id {pk} not found")

    if request.method == 'POST':
        form = GroupsAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupsAddForm(instance=group)

    return render(request,
                  'groups_edit.html',
                  context={'form': form, 'pk': pk})
