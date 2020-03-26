from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *
from .form import SectionGroupFromModel, SectionFromModel
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import filters

"""model viewset"""


class ModelViewSetSection(ModelViewSet):
    serializer_class = SectionModelSerializer
    queryset = Section.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('name',)


class ModelViewSetSectionGroup(ModelViewSet):
    serializer_class = SectionGroupModelSerializer
    queryset = SectionGroup.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('section_name',)

"""viewset"""


class ViewSetSection(ViewSet):
    serializer_class = SectionModelSerializer
    model = Section

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'update successfully object id {pk}'
            else:
                message = f'can not update object id {pk}'
        else:
            message = f'can not find object id {pk}'
        return Response({'message': message})

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'update successfully object id {pk}'
            else:
                message = f'can not update object id {pk}'
        else:
            message = f'can not find object id {pk}'
        return Response({'message': message})

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'object id {pk} successfully deleted'})
        return Response({'message': f'can not delete object id {pk}'})


class ViewSetSectionGroup(ViewSet):
    serializer_class = SectionGroupModelSerializer
    model = SectionGroup

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'update successfully object id {pk}'
            else:
                message = f'can not update object id {pk}'
        else:
            message = f'can not find object id {pk}'
        return Response({'message': message})

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'update successfully object id {pk}'
            else:
                message = f'can not update object id {pk}'
        else:
            message = f'can not find object id {pk}'
        return Response({'message': message})

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'object id {pk} successfully deleted'})
        return Response({'message': f'can not delete object id {pk}'})

"""ApiView"""


class ApiViewSection(APIView):
    serializer_class = SectionModelSerializer
    model = Section

    def get(self, request, pk=None):
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
            serializer = self.serializer_class(obj)
        else:
            obj = self.model.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object id {pk} updated successfully'
            else:
                message = f'can not update object with id {pk}'
        else:
            message = f'can not find any object with id {pk}'
        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object id {pk} updated successfully'
            else:
                message = f'can not update object with id {pk}'
        else:
            message = f'can not find any object with id {pk}'
        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully delete object {pk}'})
        return Response({'message': f'can not delete object {pk}'})


class ApiViewSectionGroup(APIView):
    serializer_class = SectionGroupModelSerializer
    model = SectionGroup

    def get(self, request, pk=None):
        if pk is not None:
            obj = get_object_or_404(self.model, pk=pk)
            serializer = self.serializer_class(obj)
        else:
            obj = self.model.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object id {pk} updated successfully'
            else:
                message = f'can not update object with id {pk}'
        else:
            message = f'can not find any object with id {pk}'
        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object id {pk} updated successfully'
            else:
                message = f'can not update object with id {pk}'
        else:
            message = f'can not find any object with id {pk}'
        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully delete object {pk}'})
        return Response({'message': f'can not delete object {pk}'})


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



