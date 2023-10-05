# PSW8.0
Aprendendo sobre DJANGO 

Da permisão para o PowerShell:
$Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

Entrar na venv(env) -> Windowns
$env\Scripts\activate

Iniciei o projento no Django com:
$pip install django

Para iniciar o projeto. OBS.: sem (<>):
$django-admin startproject <NomeDoProjeto> .

Rodando a aplicação: 
$python manage.py runserver

Criando um app:
$python manage.py startapp <NomeDoApp>
______________________________________________________________________________________________________________
Erro ao tentar executar o comando "makemigrations"
ERRORS:
exames.TiposExames.horario_final: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
______________________________________________________________________________________________________________
Solução: 
$ python -m pip install Pillow

Leu o models para criação de tabela no banco:
$python manage.py makemigrations

Migração(salvar no banco):
$python manage.py migrate

Criar superuser:
$python manage.py createsuperuser

Fluxo do Django:
![Alt text](django-architecture.png)
