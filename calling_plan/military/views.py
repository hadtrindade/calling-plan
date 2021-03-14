from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Militares, Area, SubUnidade, PostoGraduacao
from django.urls import reverse_lazy


class MilitaryCreate(CreateView):
    model = Militares
    fields = [
        "identidade",
        "nome",
        "graduacao",
        "subunidade",
        "operacional",
        "telefone",
        "telefone_familia",
        "telefone_telegram",
        "telefone_whatsapp",
        "chamador",
        "rua",
        "bairro",
        "cidade",
        "estado",
        "cep",
        "area",
    ]
    template_name = "military/form_military.html"
    success_url = reverse_lazy("military:list-military")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Cadastro de Militar"
        context["botao"] = "Cadastrar"
        context["icone"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class AreaCreate(CreateView):

    model = Area
    fields = ["area", "descricao"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-area")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Cadastro de Area"
        context["botao"] = "Cadastrar"
        context["icone"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class SubUnidadeCreate(CreateView):

    model = SubUnidade
    fields = ["nome", "sigla"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-subunit")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Cadastro de Subunidade"
        context["botao"] = "Cadastrar"
        context["icone"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


class PostoGraduacaoCreate(CreateView):
    model = PostoGraduacao
    fields = ["nome", "sigla"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-graduation")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["titulo"] = "Cadastro de Posto e Graduação"
        context["botao"] = "Cadastrar"
        context["icone"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


def list_military(request):

    content_fields = Militares.objects.all().select_related("graduacao","area","subunidade")
    field_names = [
        "Posto/Graduação",
        "Nome",
        "Subunidade",
        "Área",
        "Telefone",
        "Detalhes",
        "Editar/Excluir",
    ]

    context = {
        "field_names": field_names,
        "fields_list": content_fields,
    }

    return render(
        request, template_name="military/list_military.html", context=context
    )


def list_subunit(request):

    data = SubUnidade.objects.values("nome", "sigla")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Subunidade",
    }

    return render(request, template_name="military/list.html", context=context)


def list_graduation(request):

    data = PostoGraduacao.objects.values("nome", "sigla")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Postos e Graduações",
    }

    return render(request, template_name="military/list.html", context=context)


def list_area(request):

    data = Area.objects.values("descricao", "area")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Areas de Chamamento",
    }

    return render(request, template_name="military/list.html", context=context)
