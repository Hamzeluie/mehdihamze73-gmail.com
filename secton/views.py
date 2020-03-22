from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *
from .form import SectionGroupFromModel, SectionFromModel


"""section group class views"""


class SectionGroupIndexView(generic.ListView):
    template_name = 'group/index.html'
    queryset = SectionGroup.objects.all()
    context_object_name = 'object'


class SectionGroupCreateView(generic.CreateView):
    template_name = 'group/create.html'

    def get(self, request, *args, **kwargs):
        form = SectionGroupFromModel()
        return render(request, self.template_name, {'form':
                                                    form})

    def post(self, request, *args, **kwargs):
        form = SectionGroupFromModel(request.POST)
        if form.is_valid():
            form.save()
        return redirect('../')


class SectionGroupUpdateView(generic.UpdateView):
    template_name = 'group/update.html'

    def get(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        obj = get_object_or_404(SectionGroup, id=g_id)
        if obj is not None:
            form = SectionGroupFromModel(instance=obj)
        return render(request, self.template_name, {'form': form,
                                                    'object': obj
                                                    })

    def post(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        obj = get_object_or_404(SectionGroup, id=g_id)
        if obj is not None:
            form = SectionGroupFromModel(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        return redirect('../../')


class SectionGroupDeleteView(generic.DeleteView):
    template_name = 'group/delete.html'

    def get(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        obj = get_object_or_404(SectionGroup, id=g_id)
        if obj is not None:
            form = SectionGroupFromModel(instance=obj)
        return render(request, self.template_name, {'form': form,
                                                    'object': obj})

    def post(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        obj = get_object_or_404(SectionGroup, id=g_id)
        if obj is not None:
            obj.delete()
        return redirect('../../')


"""Section ClassViews"""


class SectionIndexView(generic.ListView):
    template_name = 'section/index.html'

    def get(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        group = get_object_or_404(SectionGroup, id=g_id)
        section = group.section_set.all()
        return render(request, self.template_name, {'section': section,
                                                    'group': group
                                                    })


class SectionCreateView(generic.CreateView):
    template_name = 'section/create.html'

    def get(self, request, *args, **kwargs):
        form = SectionFromModel()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        g_id = kwargs.get('group_id')
        group = get_object_or_404(SectionGroup, id=g_id)
        form = SectionFromModel(request.POST)
        if form. is_valid():
            section = form.save(commit=False)
            section.group = group
            section.save()
        return redirect('../')


class SectionUpdateView(generic.UpdateView):
    template_name = 'section/update.html'

    def get(self, request, *args, **kwargs):
        s_id = kwargs.get('section_id')
        obj = get_object_or_404(Section, id=s_id)
        if obj is not None:
            form = SectionFromModel(instance=obj)
        return render(request, self.template_name, {'form': form,
                                                    'object': obj
                                                    })

    def post(self, request, *args, **kwargs):
        s_id = kwargs.get('section_id')
        obj = get_object_or_404(Section, id=s_id)
        if obj is not None:
            form = SectionFromModel(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        return redirect('../../')


class SectionDeleteView(generic.DeleteView):
    template_name = 'section/delete.html'

    def get(self, request, *args, **kwargs):
        s_id = kwargs.get('section_id')
        obj = get_object_or_404(Section, id=s_id)
        if obj is not None:
            form = SectionFromModel(instance=obj)
        return render(request, self.template_name, {'form': form,
                                                    'object': obj
                                                    })

    def post(self, request, *args, **kwargs):
        s_id = kwargs.get('section_id')
        obj = get_object_or_404(Section, id=s_id)
        if obj is not None:
            obj.delete()
        return redirect('../../')



