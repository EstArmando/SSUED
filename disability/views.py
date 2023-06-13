from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from disability.forms import DisabilityForm

from disability.models import Disability

# Create your views here.

def get_disability(id):
    try:
        return Disability.objects.get(disability_id=id)  
    except:
        return None

@login_required
def disabilities(request):        
    disabilities= Disability.objects.all()
    return render(request,'disabilities.html',{'title':'Discapacidades', 'panel': 'Discapacidades','disabilities': disabilities })

@login_required
def create_disability(request):
    if request.method== 'POST':
        form=DisabilityForm(request.POST)
        if form.is_valid():
            type=form.cleaned_data['type']   
            d=Disability.objects.create(type=type)   
            d.save()
            return redirect('disabilities')
    else:
        form=DisabilityForm() 
    return render(request, 'createdisability.html', {
        'title': 'Agregar Discapacidad',
        'form': form
    })        

@login_required
def delete_disability(request, id):
    d=get_disability(id)
    if d:
        d.delete()
        return redirect('disabilities')
    else:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'La discapacidad no existe.'
        })

@login_required
def edit_disability(request, id):
    d=get_disability(id)
    if not d:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'La discapacidad no existe.'
        })
    form = DisabilityForm(request.POST or None, initial={
        'type':d.type
    })    
    if request.method == 'POST':
        if form.is_valid():
            d.type=form.cleaned_data['type']
            d.save()
            return redirect('disabilities')
    return render(request, 'editdisability.html', {
        'title': 'Editar Discapacidad',
        'form': form,
        'disability': d
    })        