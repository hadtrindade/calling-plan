from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Military, Area, SubUnit, Graduation
from django.urls import reverse_lazy
from .forms import MilitaryForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url="core:login"), name='dispatch')
class MilitaryCreate(CreateView):
    model = Military
    form_class = MilitaryForm

    template_name = "military/form_military.html"
    success_url = reverse_lazy("military:list-military")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Cadastro de Militar"
        context["button"] = "Cadastrar"
        context["icon"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


@method_decorator(login_required(login_url="core:login"), name='dispatch')
class AreaCreate(CreateView):

    model = Area
    fields = ["area", "descricao"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-area")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Cadastro de Area"
        context["button"] = "Cadastrar"
        context["icon"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


@method_decorator(login_required(login_url="core:login"), name='dispatch')
class SubUnitCreate(CreateView):

    model = SubUnit
    fields = ["nome", "sigla"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-subunit")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Cadastro de Subunidade"
        context["button"] = "Cadastrar"
        context["icon"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


@method_decorator(login_required(login_url="core:login"), name='dispatch')
class GraduationCreate(CreateView):
    model = Graduation
    fields = ["nome", "sigla"]
    template_name = "military/form.html"
    success_url = reverse_lazy("military:list-graduation")

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Cadastro de Posto e Graduação"
        context["button"] = "Cadastrar"
        context["icon"] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context


@login_required(login_url="core:login")
def list_military(request):

    content_fields = Military.objects.all().select_related(
        "graduacao", "area", "subunidade"
    )
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


@login_required(login_url="core:login")
def details_military(request, pk):

    content_fields = Military.objects.select_related(
        "graduacao", "area", "subunidade"
    ).get(id=pk)

    context = {
        "fields": content_fields,
    }

    return render(
        request, template_name="military/list_military_details.html", context=context
    )


@login_required(login_url="core:login")
def edit_military(request, pk):

    military = Military.objects.select_related(
        "graduacao", "area", "subunidade"
    ).get(id=pk)
    form = MilitaryForm(instance=military)
    if request.method == "POST":
        form = MilitaryForm(request.POST, instance=military)
        if form.is_valid():
            form.save()
            return redirect("military:list-military")

    context = {
        "form": form,
        "titulo": "Editar Militar"
    }

    return render(
        request, template_name="military/form_military.html", context=context
    )


@login_required(login_url="core:login")
def delete_military(request, pk):

    military = Military.objects.select_related(
        "graduacao", "area", "subunidade"
    ).get(id=pk)
    form = MilitaryForm(instance=military)

    if request.method == "POST":
        military.delete()
        return redirect("military:list-military")
    context = {
        "form": form,
    }

    return render(
        request, template_name="military/delete_military.html", context=context
    )


@login_required(login_url="core:login")
def list_subunit(request):

    data = SubUnit.objects.values("nome", "sigla")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Subunidade",
    }

    return render(request, template_name="military/list.html", context=context)


@login_required(login_url="core:login")
def list_graduation(request):

    data = Graduation.objects.values("nome", "sigla")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Postos e Graduações",
    }

    return render(request, template_name="military/list.html", context=context)


@login_required(login_url="core:login")
def list_area(request):

    data = Area.objects.values("descricao", "area")
    field_names = ["Nome", "Acronimo", "Editar/Excluir"]
    context = {
        "field_names": field_names,
        "fields_list": data,
        "view_name": "Areas de Chamamento",
    }

    return render(request, template_name="military/list.html", context=context)
