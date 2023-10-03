from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

def listar_cursos(request):
    """Fazendo a consulta/busca no Banco"""
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_filtrar = request.GET.get('carga_horaria')
    
    cursos = Curso.objects.all()

    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)

    if carga_filtrar:
        
        cursos = cursos.filter(caga_horaria__gte=carga_filtrar)
        """
        __gte >= (MAIOR ou IGUAL)
        __lte <= (MENOR ou IGUAL)
        __gt > (MAIOR)
        __lt < (MENOR)
        """

    return render(request, 'listar_cursos.html', {'cursos': cursos})

def criar_curso(request):
    """Salvando no banco"""
    if request.method == "GET":
        status = request.GET.get('status')
    
        return render(request, 'criar_curso.html', {'status':status}) #passando status para o html
    elif request.method == "POST":
        nome_digitado = request.POST.get('nome') 
        carga_horaria_digitado = request.POST.get('carga_horaria') #acessando pelo nome de "name"

        curso = Curso(
            nome = nome_digitado,
            caga_horaria = carga_horaria_digitado,
            data_criação = datetime.now()
        )

        curso.save()#Salvando no banco de dados

        return redirect('/cursos/criar_curso/?status=1')
    
def ver_curso(request,id):
    curso = Curso.objects.get(id=id)
    return render(request, 'ver_curso.html', {'curso':curso})

def deletar_curso(request,id):
    curso = Curso.objects.get(id=id)
    #curso.delete() para deletar do DB
    curso.ativo = False
    curso.save()
    return redirect('/cursos/listar_cursos')