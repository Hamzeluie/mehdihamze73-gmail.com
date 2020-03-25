from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ProductGroup, Product
from .form import *
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import *


"""Model ViewSet rest_framework"""


class ModelViewSetProduct(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter, )
    search_filter = ('name', 'price',)


class ModelViewSetProductGroup(ModelViewSet):
    serializer_class = ProductGroupModelSerializer
    queryset = ProductGroup.objects.all()
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('group_name',)


"""ViewSet rest_framework"""


class ViewSetProductGroup(ViewSet):
    serializer_class = ProductGroupModelSerializer
    model = ProductGroup

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully deleted object id {pk}'})
        return Response({'message': f'can not deleted object id {pk}'})

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': f'successfully updated object id {pk}'})
            return Response({'message': f'can not update object id {pk}'})
        return Response({'message': f'can not find any object with id {pk}'})

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': f'successfully updated object id {pk}'})
            return Response({'message': f'can not update object id {pk}'})
        return Response({'message': f'can not find any object with id {pk}'})

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewSetProduct(ViewSet):
    serializer_class = ProductModelSerializer
    model = Product

    def list(self, request, pk=None):
        obj = self.model.objects.all()
        serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully deleted object id {pk}'})
        return Response({'message': f'can not deleted object id {pk}'})

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': f'successfully updated object id {pk}'})
            return Response({'message': f'can not update object id {pk}'})
        return Response({'message': f'can not find any object with id {pk}'})

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)

    def update(self, request, pk=None):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': f'successfully updated object id {pk}'})
            return Response({'message': f'can not update object id {pk}'})
        return Response({'message': f'can not find any object with id {pk}'})

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""ApiView rest_framework"""


class ApiProductGroupView(APIView):
    serializer_class = ProductGroupModelSerializer
    model = ProductGroup

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
                message = f'object {pk} updated successfully'
            else:
                message = f'can not update object {pk}'
        else:
            message = f'there is no any object with id {pk}'
        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object {pk} updated successfully'
            else:
                message = f'can not update object {pk}'
        else:
            message = f'there is no any object with id {pk}'
        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully delete object id {pk}'})
        return Response({'message': f'can not delete object id {pk}'})


class ApiProductView(APIView):
    serializer_class = ProductModelSerializer

    def get(self, request, pk=None):
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            serializer = self.serializer_class(obj)
        else:
            obj =Product.objects.all()
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object {pk} updated successfully'
            else:
                message = f'can not update object {pk}'
        else:
            message = f'there is no any object with id {pk}'
        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                message = f'object {pk} updated successfully'
            else:
                message = f'can not update object {pk}'
        else:
            message = f'there is no any object with id {pk}'
        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'successfully delete object id {pk}'})
        return Response({'message': f'can not delete object id {pk}'})


'''Product Group view classes'''


class ProductGroupIndexView(generic.ListView):
    template_name = 'product_group/index.html'
    queryset = ProductGroup.objects.all()
    context_object_name = 'pg'


class ProductGroupCreateView(generic.CreateView):
    template_name = 'product_group/create.html'

    def get(self, request, *args, **kwargs):
        form = ProductGroupModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductGroupModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/products/')


class ProductGroupUpdateView(generic.UpdateView):
    template_name = 'product_group/update.html'

    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        obj = get_object_or_404(ProductGroup, id=group_id)
        context = {}
        if obj is not None:
            form = ProductGroupModelForm(instance=obj)
            context['form'] = form
            context['object'] = obj
            return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        obj = get_object_or_404(ProductGroup, id=group_id)
        context = {}
        if obj is not None:
            form = ProductGroupModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                context['form'] = form
                context['object'] = obj
        return redirect('/products/')


class ProductGroupDeleteView(generic.DeleteView):
    template_name = 'product_group/delete.html'

    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        obj = get_object_or_404(ProductGroup, id=group_id)
        form = ProductGroupModelForm(instance=obj)
        context = {'form': form, 'object': obj}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        obj = get_object_or_404(ProductGroup, id=group_id)
        if obj is not None:
            obj.delete()
        return redirect('/products/')


'''product view classes'''


class ProductIndexView(generic.ListView):
    template_name = 'products/index.html'

    def get(self, request, *args, **kwargs):
        gp_id = kwargs.get('group_id')
        product_group = get_object_or_404(ProductGroup, id=gp_id)
        product = product_group.product_set.all()
        return render(request, self.template_name, {'product_group': product_group,
                                                    'product': product})


class ProductCreateView(generic.CreateView):
    template_name = 'products/create.html'

    def get(self, request, *args, **kwargs):
        form = ProductModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        pg = get_object_or_404(ProductGroup, id=group_id)
        form = ProductModelForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.product_group = pg
            product.save()
        return redirect("../")


class ProductUpdateView(generic.UpdateView):
    template_name = 'products/update.html'

    def get(self, request, *args, **kwargs):
        p_id = kwargs.get('product_id')
        obj = get_object_or_404(Product, id= p_id)
        form = ProductModelForm(instance=obj)
        return render(request, self.template_name, {'form': form,
                                                    'object': obj})

    def post(self, request, *args, **kwargs):
        p_id = kwargs.get('product_id')
        obj = get_object_or_404(Product, id=p_id)
        if obj is not None:
            form = ProductModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        return redirect('../../')


class ProductDeleteView(generic.DeleteView):
    template_name = 'products/delete.html'

    def get(self, request, *args, **kwargs):
        p_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=p_id)
        form = ProductModelForm(instance=product)
        return render(request, self.template_name, {'form': form,
                                                    'object': product})

    def post(self, request, *args, **kwargs):
        p_id = kwargs.get('product_id')
        pg_id = kwargs.get('group_id')
        product = get_object_or_404(Product, id=p_id)
        if product is not None:
            product.delete()
        return redirect(f"../../")


