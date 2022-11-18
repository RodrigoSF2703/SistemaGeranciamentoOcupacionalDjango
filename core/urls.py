from django.urls import path
from .views import home, lista_funcoes, funcao_novo, funcao_update, funcao_search, funcao_delete
from .views import lista_setores, setor_novo, setor_update, setor_search, setor_delete
from .views import lista_tiporiscos, tiporisco_novo, tiporisco_update, tiporisco_delete
from .views import lista_riscos, risco_novo, risco_update, risco_delete, grupoexame_novo, grupoexame_delete
from .views import lista_exames, exame_novo, exame_update, exame_delete, gruporisco_delete
from .views import lista_grupos, grupo_novo, grupo_update, grupo_delete, grupofuncao_novo, grupofuncao_delete, gruporisco_novo
from .views import lista_empregados, empregado_novo, empregado_update, load_funcoes, load_grupos
from .views import lista_coords, coord_update, coord_novo, coord_delete
from .views import lista_atendimentos, atendimento_update, atendimento_delete, atendimento_search, atendimento_novo
from .views import atendimentorisco_novo, atendimentorisco_delete, atendimentoexame_novo, atendimentoexame_delete
from .views import rel_aso



urlpatterns = [

    path('home', home, name='home'),
    path('lista_funcoes', lista_funcoes, name='lista_funcoes'),
    path('funcao_novo', funcao_novo, name='funcao_novo'),
    path('funcao_update/<int:id>', funcao_update, name='funcao_update'),
    path('funcao_delete/<int:id>', funcao_delete, name='funcao_delete'),
    path('funcao_search', funcao_search, name='funcao_search'),

    path('lista_setores', lista_setores, name='lista_setores'),
    path('setor_novo', setor_novo, name='setor_novo'),
    path('setor_update/<int:id>', setor_update, name='setor_update'),
    path('setor_delete/<int:id>', setor_delete, name='setor_delete'),
    path('setor_search', setor_search, name='setor_search'),

    path('lista_tiporiscos', lista_tiporiscos, name='lista_tiporiscos'),
    path('tiporisco_novo', tiporisco_novo, name='tiporisco_novo'),
    path('tiporisco_update/<int:id>', tiporisco_update, name='tiporisco_update'),
    path('tiporisco_delete/<int:id>', tiporisco_delete, name='tiporisco_delete'),

    path('lista_riscos', lista_riscos, name='lista_riscos'),
    path('risco_novo', risco_novo, name='risco_novo'),
    path('risco_update/<int:id>', risco_update, name='risco_update'),
    path('risco_delete/<int:id>', risco_delete, name='risco_delete'),

    path('lista_exames', lista_exames, name='lista_exames'),
    path('exame_novo', exame_novo, name='exame_novo'),
    path('exame_update/<int:id>', exame_update, name='exame_update'),
    path('exame_delete/<int:id>', exame_delete, name='exame_delete'),

    path('lista_grupos', lista_grupos, name='lista_grupos'),
    path('grupo_novo', grupo_novo, name='grupo_novo'),
    path('grupo_update/<int:id>', grupo_update, name='grupo_update'),
    path('grupo_delete/<int:id>', grupo_delete, name='grupo_delete'),
    path('grupofuncao_novo/<int:id>', grupofuncao_novo, name='grupofuncao_novo'),
    path('grupofuncao_delete/<int:id>', grupofuncao_delete, name='grupofuncao_delete'),
    path('gruporisco_novo/<int:id>', gruporisco_novo, name='gruporisco_novo'),
    path('gruporisco_delete/<int:id>', gruporisco_delete, name='gruporisco_delete'),
    path('grupoexame_novo/<int:id>', grupoexame_novo, name='grupoexame_novo'),
    path('grupoexame_delete/<int:id>', grupoexame_delete, name='grupoexame_delete'),

    path('lista_empregados', lista_empregados, name='lista_empregados'),
    path('empregado_novo', empregado_novo, name='empregado_novo'),
    path('empregado_update/<int:id>', empregado_update, name='empregado_update'),
    path('ajax/load-funcoes', load_funcoes, name='ajax_load_funcoes'),
    path('ajax/load-grupos', load_grupos, name='ajax_load_grupos'),

    path('lista_coords', lista_coords, name='lista_coords'),
    path('coord_novo', coord_novo, name='coord_novo'),
    path('coord_update/<int:id>', coord_update, name='coord_update'),
    path('coord_delete/<int:id>', coord_delete, name='coord_delete'),

    path('lista_atendimentos', lista_atendimentos, name='lista_atendimentos'),
    path('atendimento_novo', atendimento_novo, name='atendimento_novo'),
    path('atendimento_update/<int:id>', atendimento_update, name='atendimento_update'),
    path('atendimento_search', atendimento_search, name='atendimento_search'),
    path('atendimento_delete/<int:id>', atendimento_delete, name='atendimento_delete'),
    path('atendimentorisco_novo/<int:id>', atendimentorisco_novo, name='atendimentorisco_novo'),
    path('atendimentorisco_delete/<int:id>', atendimentorisco_delete, name='atendimentorisco_delete'),

    path('atendimentoexame_novo/<int:id>', atendimentoexame_novo, name='atendimentoexame_novo'),
    path('atendimentoexame_delete/<int:id>', atendimentoexame_delete, name='atendimentoexame_delete'),
    path('rel_aso/<int:id>', rel_aso, name='rel_aso'),
]