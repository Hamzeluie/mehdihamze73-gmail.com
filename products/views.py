from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import ProductGroup, Product
from .form import *
from django.views import generic


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


