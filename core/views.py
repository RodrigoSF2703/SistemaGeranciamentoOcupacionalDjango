from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core.paginator import Paginator
from .models import Funcao, Setor, TipoRisco, Risco, Exame, Grupo, GrupoFuncao, GrupoRisco, GrupoExame, TipoExame
from .models import Empregado, Coordenador, Atendimento, AtendimentoExame, AtendimentoRisco
from .forms import FuncaoForm, SetorForm, TipoRiscoForm, RiscoForm, ExameForm, GrupoForm, GrupoFuncaoForm, GrupoRiscoForm, GrupoExameForm
from .forms import GrupoRiscoForm, GrupoExameForm, TipoExameForm, EmpregadoForm, CoordenadorForm
from .forms import AtendimentoForm
from django.contrib.auth.decorators import login_required
import datetime

from django.views.generic.base import View
import xhtml2pdf.pisa as pisa
import io
from django.template.loader import get_template


# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def lista_funcoes(request):
    form = FuncaoForm
    funcoes_list = Funcao.objects.all().order_by('nome')
    paginator = Paginator(funcoes_list, 2)
    page = request.GET.get('page')
    funcoes = paginator.get_page(page)
    data = {}
    data['funcoes'] = funcoes
    data['form'] = form
    return render(request, 'core/lista_funcoes.html', data)

@login_required
def funcao_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Funcao.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('funcao_novo')
        else:
            form = FuncaoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render(request, 'core/funcao_novo.html', {'form': form})

@login_required
def funcao_update(request, id):
    funcao = Funcao.objects.get(id=id)
    form = FuncaoForm(request.POST or None, instance=funcao)
    data = {}
    data['funcao'] = funcao
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_funcoes')
    else:
        form = FuncaoForm
        return render(request, 'core/funcao_update.html', data)

@login_required
def funcao_search(request):
    search = request.GET.get('search')
    funcoes = Funcao.objects.filter(nome__icontains=search)
    form = FuncaoForm()
    data = {}
    data['funcoes'] = funcoes
    data['form'] = form
    return render(request, 'core/lista_funcoes.html', data)

@login_required
def funcao_delete(request, id):
    funcao = Funcao.objects.get(id=id)
    funcao.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_funcoes')

@login_required
def lista_setores(request):
    form = SetorForm
    setores_list = Setor.objects.all().order_by('nome')
    paginator = Paginator(setores_list, 2)
    page = request.GET.get('page')
    setores = paginator.get_page(page)
    data = {}
    data['setores'] = setores
    data['form'] = form
    return render(request, 'core/lista_setores.html', data)

@login_required
def setor_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Setor.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('setor_novo')
        else:
            form = SetorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_setores')
    else:
        form = SetorForm
        return render(request, 'core/setor_novo.html', {'form': form})

@login_required
def setor_update(request, id):
    setor = Setor.objects.get(id=id)
    form = SetorForm(request.POST or None, instance=setor)
    data = {}
    data['setor'] = setor
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_setores')
    else:
        form = SetorForm
        return render(request, 'core/setor_update.html', data)

@login_required
def setor_search(request):
    search = request.GET.get('search')
    setores = Setor.objects.filter(nome__icontains=search)
    form = SetorForm()
    data = {}
    data['setores'] = setores
    data['form'] = form
    return render(request, 'core/lista_setores.html', data)

@login_required
def setor_delete(request, id):
    setor = Setor.objects.get(id=id)
    setor.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_setores')

@login_required
def lista_tiporiscos(request):
    form = TipoRiscoForm
    tiporiscos = TipoRisco.objects.all().order_by('nome')
    data = {}
    data['tiporiscos'] = tiporiscos
    data['form'] = form
    return render(request, 'core/lista_tiporiscos.html', data)

@login_required
def tiporisco_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = TipoRisco.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('tiporisco_novo')
        else:
            form = TipoRiscoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_tiporiscos')
    else:
        form = TipoRiscoForm
        return render(request, 'core/tiporisco_novo.html', {'form': form})

@login_required
def tiporisco_update(request, id):
    tiporisco = TipoRisco.objects.get(id=id)

    nome = request.POST.get('nome')
    count = TipoRisco.objects.filter(nome=nome).exclude(id=id).count()
    if count > 0:
        messages.error(request, 'Registro já cadastrado com este Nome !')
        return redirect('lista_tiporiscos')

    form = TipoRiscoForm(request.POST or None, instance=tiporisco)
    data = {}
    data['tiporisco'] = tiporisco
    data['form'] = form
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_tiporiscos')
    else:
        form = TipoRiscoForm
        return render(request, 'core/tiporisco_update.html', data)

@login_required
def tiporisco_delete(request, id):
    tiporisco = TipoRisco.objects.get(id=id)
    tiporisco.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_tiporiscos')

@login_required
def lista_riscos(request):
    form = RiscoForm
    riscos = Risco.objects.all().order_by('nome')
    data = {}
    data['riscos'] = riscos
    data['form'] = form
    return render(request, 'core/lista_riscos.html', data)

@login_required
def risco_novo(request):
    if request.method == "POST":
        nome = request.POST.get('id_nome')
        tiporisco_id = request.POST.get('id_tiporisco')
        count = Risco.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('risco_novo')
        else:
            form = RiscoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_riscos')
    else:
        form = RiscoForm
        tiporiscos = TipoRisco.objects.all().order_by('nome')
        data = {}
        data['tiporiscos'] = tiporiscos
        data['form'] = form
        return render(request, 'core/risco_novo.html', data)

@login_required
def risco_update(request, id):
    risco = Risco.objects.get(id=id)
    nome = request.POST.get('nome')
    count = Risco.objects.filter(nome=nome).exclude(id=id).count()
    if count > 0:
        messages.error(request, 'Registro já cadastrado com este Nome !')
        return redirect('lista_riscos')

    form = RiscoForm(request.POST or None, instance=risco)
    tiporiscos = TipoRisco.objects.all().order_by('nome')
    data = {}
    data['tiporiscos'] = tiporiscos
    data['risco'] = risco
    data['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('lista_riscos')
    else:
        form = RiscoForm
        return render(request, 'core/risco_update.html', data)

@login_required
def risco_delete(request, id):
    risco = Risco.objects.get(id=id)
    risco.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_riscos')

@login_required
def lista_exames(request):
    form = ExameForm
    exames = Exame.objects.all().order_by('nome')
    data = {}
    data['exames'] = exames
    data['form'] = form
    return render(request, 'core/lista_exames.html', data)

@login_required
def exame_novo(request):
    if request.method == "POST":
        nome = request.POST.get('id_nome')
        validade = request.POST.get('validade')
        count = Exame.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('exame_novo')
        else:
            form = ExameForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_exames')
    else:
        form = ExameForm
        data = {}
        data['form'] = form
        return render(request, 'core/exame_novo.html', data)

@login_required
def exame_update(request, id):
    exame = Exame.objects.get(id=id)
    form = ExameForm(request.POST or None, instance=exame)
    data = {}
    data['exame'] = exame
    data['form'] = form

    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Exame.objects.filter(nome=nome).exclude(id=id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('lista_exames')        
        if form.is_valid():
            form.save()
            return redirect('lista_exames')
    else:
        form = ExameForm
        return render(request, 'core/exame_update.html', data)

@login_required
def exame_delete(request, id):
    exame = Exame.objects.get(id=id)
    exame.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_exames')

@login_required
def lista_grupos(request):
    form = GrupoForm
    grupos = Grupo.objects.all().order_by('nome')
    data = {}
    data['grupos'] = grupos
    data['form'] = form
    return render(request, 'core/lista_grupos.html', data)

@login_required
def grupo_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Grupo.objects.filter(nome=nome).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('grupo_novo')
        else:
            form = GrupoForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('lista_grupos')
    else:
        form = GrupoForm
        return render(request, 'core/grupo_novo.html', {'form': form})

@login_required
def grupo_update(request, id):
    grupo = Grupo.objects.get(id=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    data = {}
    data['grupo'] = grupo
    data['form'] = form
    if request.method == "POST":
        nome = request.POST.get('nome')
        count = Grupo.objects.filter(nome=nome).exclude(id=id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome !')
            return redirect('lista_grupos')
        
        if form.is_valid():
            form.save()
            return redirect('lista_grupos')
    else:
        form = GrupoForm
        return render(request, 'core/grupo_update.html', data)

@login_required
def grupo_delete(request, id):
    grupo = Grupo.objects.get(id=id)
    grupo.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_grupos')

@login_required
def grupofuncao_novo(request, id):
    grupo = Grupo.objects.get(id=id)
    grupofuncoes = GrupoFuncao.objects.filter(grupo_id=id)
    setores = Setor.objects.all().order_by('nome')
    funcoes = Funcao.objects.all().order_by('nome')
    data = {}
    data['grupo'] = grupo
    data['grupofuncoes'] = grupofuncoes
    data['setores'] = setores
    data['funcoes'] = funcoes
    if request.method == "POST":
        funcao_id = request.POST.get('funcao_id')
        setor_id = request.POST.get('setor_id')
        count = GrupoFuncao.objects.filter(grupo_id=id, funcao_id=funcao_id, setor_id=setor_id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado !')
            return redirect('/grupofuncao_novo/' + str(id))
        else:
            g = GrupoFuncao.objects.create(
                grupo_id = id,
                funcao_id = funcao_id,
                setor_id = setor_id
            )
            return redirect('/grupofuncao_novo/' + str(id))
    else:
        return render(request, 'core/grupofuncao_novo.html', data)

@login_required
def grupofuncao_delete(request, id):
    grupofuncao = GrupoFuncao.objects.get(id=id)
    grupo_id = grupofuncao.grupo_id
    grupofuncao.delete()
    return redirect('/grupofuncao_novo/' + str(grupo_id))

@login_required
def gruporisco_novo(request, id):
    grupo = Grupo.objects.get(id=id)
    gruporiscos = GrupoRisco.objects.filter(grupo_id=id)
    riscos = Risco.objects.all().order_by('nome')
    data = {}
    data['grupo'] = grupo
    data['gruporiscos'] = gruporiscos
    data['riscos'] = riscos
    if request.method == "POST":
        risco_id = request.POST.get('risco_id')
        count = GrupoRisco.objects.filter(grupo_id=id, risco_id=risco_id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado !')
            return redirect('/gruporisco_novo/' + str(id))
        else:
            g = GrupoRisco.objects.create(
                grupo_id = id,
                risco_id = risco_id
            )
            return redirect('/gruporisco_novo/' + str(id))
    else:
        return render(request, 'core/gruporisco_novo.html', data)

@login_required
def gruporisco_delete(request, id):
    gruporisco = GrupoRisco.objects.get(id=id)
    grupo_id = gruporisco.grupo_id
    gruporisco.delete()
    return redirect('/gruporisco_novo/' + str(grupo_id))

@login_required
def grupoexame_novo(request, id):
    grupo = Grupo.objects.get(id=id)
    grupoexames = GrupoExame.objects.filter(grupo_id=id)
    exames = Exame.objects.all().order_by('nome')
    tipoexames = TipoExame.objects.all().order_by('nome')
    data = {}
    data['grupo'] = grupo
    data['grupoexames'] = grupoexames
    data['exames'] = exames
    data['tipoexames'] = tipoexames
    if request.method == "POST":
        exame_id = request.POST.get('exame_id')
        tipoexame_id = request.POST.get('tipoexame_id')
        count = GrupoExame.objects.filter(grupo_id=id, exame_id=exame_id, tipoexame_id=tipoexame_id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado !')
            return redirect('/grupoexame_novo/' + str(id))
        else:
            g = GrupoExame.objects.create(
                grupo_id = id,
                exame_id = exame_id,
                tipoexame_id = tipoexame_id
            )
            return redirect('/grupoexame_novo/' + str(id))
    else:
        return render(request, 'core/grupoexame_novo.html', data)

@login_required
def grupoexame_delete(request, id):
    grupoexame = GrupoExame.objects.get(id=id)
    grupo_id = grupoexame.grupo_id
    grupoexame.delete()
    return redirect('/grupoexame_novo/' + str(grupo_id))

@login_required
def lista_empregados(request):
    form = EmpregadoForm
    empregados = Empregado.objects.all().order_by('nome')
    data = {}
    data['empregados'] = empregados
    data['form'] = form
    return render(request, 'core/lista_empregados.html', data)

@login_required
def empregado_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        ctps = request.POST.get('ctps')
        serie = request.POST.get('serie')
        data_nascimento = request.POST.get('data_nascimento')
        dia = data_nascimento[0:2]
        mes = data_nascimento[3:5]
        ano = data_nascimento[6:10]
        data_nascimento = str(ano) + '-' + str(mes) + '-' + str(dia)

        data_admissao = request.POST.get('data_admissao')
        dia = data_admissao[0:2]
        mes = data_admissao[3:5]
        ano = data_admissao[6:10]
        data_admissao = str(ano) + '-' + str(mes) + '-' + str(dia)

        data_demissao = request.POST.get('data_demissao')
        grupo_id = request.POST.get('grupo_id')
        setor_id = request.POST.get('setor_id')
        funcao_id = request.POST.get('funcao_id')

        count = Empregado.objects.filter(nome=nome, cpf=cpf).count()
        if count > 0:
            messages.error(request, 'Empregado já cadastrado com este nome e CPF')
            return redirect('empregado_novo')
        else:
            if data_demissao == '':
                e = Empregado.objects.create(
                    nome = nome,
                    cpf = cpf,
                    ctps = ctps,
                    serie = serie,
                    data_nascimento = data_nascimento,
                    data_admissao = data_admissao,
                    grupo_id = grupo_id,
                    setor_id = setor_id,
                    funcao_id = funcao_id,
                    data_demissao = None
                )
            else:
                dia = data_demissao[0:2]
                mes = data_demissao[3:5]
                ano = data_demissao[6:10]
                data_demissao = str(ano) + '-' + str(mes) + '-' + str(dia)
                e = Empregado.objects.create(
                    nome = nome,
                    cpf = cpf,
                    ctps = ctps,
                    serie = serie,
                    data_nascimento = data_nascimento,
                    data_admissao = data_admissao,
                    grupo_id = grupo_id,
                    setor_id = setor_id,
                    funcao_id = funcao_id,
                    data_demissao = data_demissao
                )
            messages.success(request, 'Registro cadastrado com sucesso!')
            return redirect('lista_empregados')
    else:
        form = EmpregadoForm()
        setores =  Setor.objects.all().order_by('nome')
        funcoes =  Funcao.objects.all().order_by('nome')
        grupos =  Grupo.objects.all().order_by('nome')
        return render(request, 'core/empregado_novo.html', 
        {
            'form': form, 
            'setores': setores, 
            'funcoes': funcoes,
            'grupos': grupos
        })

@login_required
def load_funcoes(request):
    setor_id = request.GET.get('setor_id')
    grupos = GrupoFuncao.objects.filter(setor_id=setor_id).all()
    return render(request, 'core/funcao_ajax.html', {'grupos': grupos})

@login_required
def load_grupos(request):
    setor_id = request.GET.get('setor_id')
    funcao_id = request.GET.get('funcao_id')
    grupos = GrupoFuncao.objects.filter(setor_id=setor_id, funcao_id=funcao_id).all()
    return render(request, 'core/grupo_ajax.html', {'grupos': grupos})

@login_required
def empregado_update(request, id):
    empregado = Empregado.objects.get(id=id)
    setor_id = empregado.setor_id
    funcao_id = empregado.funcao_id
    grupo_id = empregado.grupo_id

    setores = Setor.objects.all().order_by('nome')
    funcoes = Funcao.objects.all().filter(id=funcao_id)
    grupos = Grupo.objects.all().filter(id=grupo_id)
    data = {}
    data['empregado'] = empregado
    data['setores'] = setores
    data['funcoes'] = funcoes
    data['grupos'] = grupos
    if request.method == "POST":
        empregado.nome = request.POST.get('nome')
        empregado.cpf = request.POST.get('cpf')
        empregado.serie = request.POST.get('serie')
        empregado.ctps = request.POST.get('ctps')
        data_nascimento = request.POST.get('data_nascimento')
        dia = data_nascimento[0:2]
        mes = data_nascimento[3:5]
        ano = data_nascimento[6:10]
        empregado.data_nascimento = str(ano) + '-' + str(mes) + '-' + str(dia)
        data_admissao = request.POST.get('data_admissao')
        dia = data_admissao[0:2]
        mes = data_admissao[3:5]
        ano = data_admissao[6:10]
        empregado.data_admissao = str(ano) + '-' + str(mes) + '-' + str(dia)
        data_demissao = request.POST.get('data_demissao')
        empregado.grupo_id = request.POST.get('grupo_id')
        empregado.setor_id = request.POST.get('setor_id')
        empregado.funcao_id = request.POST.get('funcao_id')
        if data_demissao == '':
            empregado.data_demissao = None
            empregado.save()
        else:
            dia = data_demissao[0:2]
            mes = data_demissao[3:5]
            ano = data_demissao[6:10]
            empregado.data_demissao = str(ano) + '-' + str(mes) + '-' + str(dia)
            empregado.save()

        messages.success(request, 'Registro alterado com sucesso !')
        return redirect('lista_empregados')
    else:
        return render(request, 'core/empregado_update.html', data)

@login_required
def lista_coords(request):
    coords = Coordenador.objects.all().order_by('-data_inicio')
    return render(request, 'core/lista_coords.html', { 'coords': coords})

@login_required
def coord_novo(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        data_inicio = request.POST.get('data_inicio')
        count = Coordenador.objects.filter(nome=nome, data_inicio=data_inicio).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado com este Nome e Data!')
            return redirect('coord_novo')
        form = CoordenadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Cadastrado com sucesso !')
            return redirect('lista_coords')
    else:
        form = CoordenadorForm()
        return render(request, 'core/coord_novo.html', {'form': form})

@login_required
def coord_update(request, id):
    coord = Coordenador.objects.get(id=id)
    form = CoordenadorForm(request.POST or None, instance=coord)
    data = {}
    data['coord'] = coord
    data['form'] = form
    if request.method == "POST":
        nome = request.POST.get('nome')
        data_inicio = request.POST.get('data_inicio')
        count = Coordenador.objects.filter(nome=nome, data_inicio=data_inicio).exclude(id=id).count()
        if count > 0:
            messages.error(request, 'Existe um Registro já cadastrado com este Nome e Data!')
            return redirect('/coord_update/' + str(id))
        if form.is_valid():
            form.save()
            return redirect('lista_coords')
    else:
        return render(request, 'core/coord_update.html', data)

@login_required
def coord_delete(request, id):
    coord = Coordenador.objects.get(id=id)
    coord.delete()
    messages.success(request, 'Registro Excluido com sucesso !')
    return redirect('lista_coords')

@login_required
def lista_atendimentos(request):
    atendimentos_list = Atendimento.objects.all().order_by('-data_atendimento')
    paginator = Paginator(atendimentos_list, 10)
    page = request.GET.get('page')
    atendimentos = paginator.get_page(page)
    form = AtendimentoForm
    return render(request, 'core/lista_atendimentos.html', {'atendimentos': atendimentos, 'form': form})

@login_required
def atendimento_novo(request):
    empregados = Empregado.objects.all().order_by('nome')
    tipoexames = TipoExame.objects.all().order_by('nome')
    data = {}
    data['empregados'] = empregados
    data['tipoexames'] = tipoexames
    if request.method == "POST":
        empregado_id = request.POST.get('empregado_id')
        tipoexame_id = request.POST.get('tipoexame_id')
        data_atendimento = request.POST.get('data_atendimento')
        trabalhoaltura = request.POST.get('altura')
        if (trabalhoaltura == "on"):
            trabalhoaltura = 1
        else:
            trabalhoaltura = 0
        espacoconfinado = request.POST.get('espaco')
        if (espacoconfinado == "on"):
            espacoconfinado = 1
        else:
            espacoconfinado = 0
        apto = request.POST.get('apto')
        if (apto == "on"):
            apto = 1
        else:
            apto = 0
        dia = data_atendimento[0:2]
        mes = data_atendimento[3:5]
        ano = data_atendimento[6:10]
        data_atendimento = str(ano) + '-' + str(mes) + '-' + str(dia)
        empregado = Empregado.objects.get(id=empregado_id)
        coordenador = Coordenador.objects.get(data_fim=None)
        coordenador_id = coordenador.id
        grupo_id = empregado.grupo_id
        setor_id = empregado.setor_id
        funcao_id = empregado.funcao_id
        e = Atendimento.objects.create(
            empregado_id = empregado_id,
            coordenador_id = coordenador_id,
            data_atendimento = data_atendimento,
            tipoexame_id = tipoexame_id,
            trabalhoaltura = trabalhoaltura,
            espacoconfinado = espacoconfinado,
            apto = apto,
            grupo_id = grupo_id,
            setor_id = setor_id,
            funcao_id = funcao_id
        )
        atendimento_id = Atendimento.objects.latest('pk').pk
        gruporiscos = GrupoRisco.objects.all().filter(grupo_id=grupo_id)
        for gruporisco in gruporiscos:
            a = AtendimentoRisco.objects.create(
                atendimento_id = atendimento_id,
                risco_id = gruporisco.risco.id
            )

        grupoexames = GrupoExame.objects.all().filter(grupo_id=grupo_id)
        for grupoexame in grupoexames:
            a = AtendimentoExame.objects.create(
                atendimento_id = atendimento_id,
                exame_id = grupoexame.exame.id
            )

        messages.success(request, 'Registro cadastrado com sucesso !')
        return redirect('lista_atendimentos') 
    else:
        return render(request, 'core/atendimento_novo.html', data)

@login_required
def atendimento_search(request):
    nome = request.GET.get('nome')
    data1 = request.GET.get('data1')
    data2 = request.GET.get('data2')

    if data2 == '':
        data2 = data1
    if nome == '':
        if data1 == '':
            messages.error(request, 'Informe pelo menos uma condição de pesquisa!')
            return redirect('lista_atendimentos')
        else:
            atendimentos = Atendimento.objects.filter(data_atendimento__range=[data1, data2])
    else:
        if data1 == '':
            atendimentos = Atendimento.objects.filter( empregado__nome__icontains=nome )
        else:
            a = Atendimento.objects.filter( empregado__nome__icontains=nome )
            atendimentos = a.filter(
                data_atendimento__range=[data1, data2]
            )
            
    form = AtendimentoForm()
    return render(request, 'core/lista_atendimentos.html', {'atendimentos': atendimentos, 'form': form})

@login_required
def atendimento_update(request, id):
    atendimento = Atendimento.objects.get(id=id)
    empregado_id = atendimento.empregado_id
    grupo_id = atendimento.grupo_id
    setor_id = atendimento.setor_id
    funcao_id = atendimento.funcao_id
    empregados = Empregado.objects.all().filter(id=empregado_id)
    tipoexames = TipoExame.objects.all().order_by('nome')
    form = AtendimentoForm(request.POST or None, instance=atendimento)  
    data = {}
    data['atendimento'] = atendimento
    data['tipoexames'] = tipoexames
    data['empregados'] = empregados
    data['form'] = form
    if request.method == "POST":
        tipoexame_id = str(request.POST.get('tipoexame_id'))
        tipoexame_anterior_id = str(atendimento.tipoexame_id)
        trabalhoaltura = request.POST.get('altura')
        espacoconfinado = request.POST.get('espaco')
        apto = request.POST.get('apto')
        if (trabalhoaltura == 'on'):
            atendimento.trabalhoaltura = 1
        else:
            atendimento.trabalhoaltura = 0
        if (espacoconfinado == 'on'):
            atendimento.espacoconfinado = 1
        else:
            atendimento.espacoconfinado = 0
        if (apto == 'on'):
            atendimento.apto = 1
        else:
            atendimento.apto = 0
        data_atendimento = request.POST.get('data_atendimento')
        dia = data_atendimento[0:2]
        mes = data_atendimento[3:5]
        ano = data_atendimento[6:10]
        atendimento.data_atendimento = str(ano) + '-' + str(mes) + '-' + str(dia)
        atendimento.grupo_id = grupo_id
        atendimento.setor_id = setor_id
        atendimento.funcao_id = funcao_id
        if tipoexame_anterior_id == tipoexame_id:
            deletou = False
        else:
            # aqui deletar todos os atendimentorisco e atendimentoexame
            AtendimentoRisco.objects.all().filter(atendimento_id=id).delete()
            AtendimentoExame.objects.all().filter(atendimento_id=id).delete()
            deletou = True

        atendimento.tipoexame_id = tipoexame_id
        atendimento.save()

        if deletou == True:
            riscos = GrupoRisco.objects.all().filter(grupo_id=grupo_id)
            exames = GrupoExame.objects.all().filter(grupo_id=grupo_id, tipoexame_id=tipoexame_id)
            # aqui vai gravar atendimentorisco
            for risco in riscos:
                r = AtendimentoRisco.objects.create(
                    atendimento_id = id,
                    risco_id = risco.risco_id
                )
            # aqui vai gravar atendimentoexame
            for exame in exames:
                r = AtendimentoExame.objects.create(
                    atendimento_id = id,
                    exame_id = exame.exame_id
                ) 
        messages.success(request, 'Registro alterado com sucesso !')
        return redirect('lista_atendimentos')
    else:
        return render(request, 'core/atendimento_update.html', data)
    
@login_required
def atendimento_delete(request, id):
    atendimento = Atendimento.objects.get(id=id)
    AtendimentoRisco.objects.all().filter(atendimento_id=id).delete()
    AtendimentoExame.objects.all().filter(atendimento_id=id).delete()
    atendimento.delete()
    atendimentos = Atendimento.objects.all().order_by('-data_atendimento')
    messages.success(request, 'Atendimento total excluido com sucesso !')
    return render(request, 'core/lista_atendimentos.html', {'atendimentos': atendimentos})

@login_required
def atendimentorisco_novo(request, id):
    atendimento = Atendimento.objects.get(id=id)
    riscos = Risco.objects.all().order_by('nome')
    atendimentoriscos = AtendimentoRisco.objects.filter(atendimento_id=id)
    data = {}
    data['atendimento'] = atendimento
    data['riscos'] = riscos
    data['atendimentoriscos'] = atendimentoriscos
    if request.method == "POST":
        risco_id = request.POST.get('risco_id')
        count = AtendimentoRisco.objects.filter(atendimento_id=id, risco_id=risco_id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado !')
            return redirect('/atendimentorisco_novo/' + str(id))
        else:
            g = AtendimentoRisco.objects.create(
                atendimento_id = id,
                risco_id = risco_id
            )
            return redirect('/atendimentorisco_novo/' + str(id))
    else:
        return render(request, 'core/atendimentorisco_novo.html', data)


@login_required
def atendimentorisco_delete(request, id):
    atendimentorisco = AtendimentoRisco.objects.get(id=id)
    atendimento_id = atendimentorisco.atendimento_id
    atendimentorisco.delete()
    return redirect('/atendimentorisco_novo/' + str(atendimento_id))

@login_required
def atendimentoexame_novo(request, id):
    atendimento = Atendimento.objects.get(id=id)
    exames = Exame.objects.all().order_by('nome')
    atendimentoexames = AtendimentoExame.objects.filter(atendimento_id=id)
    data = {}
    data['atendimento'] = atendimento
    data['exames'] = exames
    data['atendimentoexames'] = atendimentoexames
    if request.method == "POST":
        exame_id = request.POST.get('exame_id')
        count = AtendimentoExame.objects.filter(atendimento_id=id, exame_id=exame_id).count()
        if count > 0:
            messages.error(request, 'Registro já cadastrado !')
            return redirect('/atendimentoexame_novo/' + str(id))
        else:
            g = AtendimentoExame.objects.create(
                atendimento_id = id,
                exame_id = exame_id
            )
            return redirect('/atendimentoexame_novo/' + str(id))
    else:
        return render(request, 'core/atendimentoexame_novo.html', data)


@login_required
def atendimentoexame_delete(request, id):
    atendimentoexame = AtendimentoExame.objects.get(id=id)
    atendimento_id = atendimentoexame.atendimento_id
    atendimentoexame.delete()
    return redirect('/atendimentoexame_novo/' + str(atendimento_id))


@login_required
def rel_aso(request, id):
    atendimento = Atendimento.objects.get(id=id)
    exames = AtendimentoExame.objects.filter(atendimento_id=id)
    riscos = AtendimentoRisco.objects.filter(atendimento_id=id)
    params = {
        'atendimento': atendimento,
        'exames': exames,
        'riscos': riscos,
        'request': request,
    }
    return Render.render('core/rel_aso.html/', params, 'rel_aso')

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
