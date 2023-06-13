from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from university.forms import UniversityForm

from university.models import University

# Create your views here.

def get_university(id):
    try:
        return University.objects.get(code=id)  
    except:
        return None

@login_required
def universities(request):        
    universities= University.objects.all()
    return render(request,'universities.html',{'title':'Universidades', 'panel': 'Universidades','universities': universities })

@login_required
def create_university(request):
    if request.method== 'POST':
        form=UniversityForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code'] 
            name=form.cleaned_data['name'] 
            acronyms=form.cleaned_data['acronyms'] 
            u=University.objects.create(code=code,name=name,acronyms=acronyms)   
            u.save()
            return redirect('universities')
    else:
        form=UniversityForm() 
    return render(request, 'createuniversity.html', {
        'title': 'Agregar Universidad',
        'form': form
    })        

@login_required
def delete_university(request, id):
    u=get_university(id)
    if u:
        u.delete()
        return redirect('universities')
    else:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'La universidad no existe.'
        })

@login_required
def edit_university(request, id):
    u=get_university(id)
    if not u:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'La universidad no existe.'
        })
    form = UniversityForm(request.POST or None, initial={
        'name':u.name,
        'acronyms':u.acronyms
    })    
    if request.method == 'POST':
        if form.is_valid():
            u.name=form.cleaned_data['name'] 
            u.acronyms=form.cleaned_data['acronyms'] 
            u.save()
            return redirect('universities')
    return render(request, 'edituniversity.html', {
        'title': 'Editar Universidad',
        'form': form,
        'university': u
    })  

            
