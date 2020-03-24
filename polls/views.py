from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Questions, Choice
from django.views import generic
from .form import QuestionModelForm, ChoiceModelForm


from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from .serializers import QuestionModelSerializer, ChoiceModelSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


"""rest_framework ViewSet"""


class QuestionViewSet(ViewSet):
    serializer_class = QuestionModelSerializer

    def list(self, request, pk=None):
        pass

    def create(self, request, pk=None):
        pass

    def update(self, request, pk):
        pass

    def partial_update(self, request, pk):
        pass


class ChoiceViewSet(ViewSet):
    serializer_class = ChoiceModelSerializer

    def list(self, request, pk=None):
        pass

    def create(self, request, pk=None):
        pass

    def update(self, request, pk):
        pass

    def partial_update(self, request, pk):
        pass


class QuestionModelViewSet(ModelViewSet):
    serializer_class = QuestionModelSerializer
    queryset = Questions
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('question_text',)
    # permission_classes =


class ChoiceModelViewSet(ModelViewSet):
    serializer_class = ChoiceModelSerializer
    queryset = Choice
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_filter = ('choice_text',)


"""rest_framework ApiView"""


class QuestionApiview(APIView):
    serializer_class = QuestionModelSerializer
    # authentication_classes = TokenAuthentication

    def get(self, request, pk=None):
        if pk is not None:
            obj = get_object_or_404(Questions, pk=pk)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        else:
            obj = Questions.objects.all()
            serializer = self.serializer_class(obj, many=True)
            return Response(serializer.data)
        return Response({'message': 'hello'})

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        obj = get_object_or_404(Questions, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = f'Question {pk} successfully partial updated'
            else:
                message = f'can not update Question {pk}'
        else:
            message = f'Query string Object is None'

        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(Questions, pk=pk)
        if obj is not None:
            serializer = self.serializer_class(instance=obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = f'Question {pk} successfully updated'
            else:
                message = f'can not update Question {pk}'
        else:
            message = f'Query string Object is None'
        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(Questions, pk=pk)
        if obj is not None:
            obj.delete()
            return Response({'message': f'object id {pk} delete successfully'})
        return Response({'message': f'can not delete object id {pk}'})


class ChoiceApiview(APIView):
    serializer_class = ChoiceModelSerializer
    # authentication_classes = TokenAuthentication

    def get(self, request, pk=None, c_id=None):
        if pk is not None:
            obj = get_object_or_404(Choice, pk=pk)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        else:
            obj = Choice.objects.all()
            serializer = self.serializer_class(obj, many=True)
            return Response(serializer.data)

    def post(self, request, pk=None, c_id=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = get_object_or_404(Choice, id=pk)
        if obj is not None:
            serializer = ChoiceModelSerializer(instance=obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                message = 'updated successfully'
            else:
                message = 'can not updated'
        else:
            message = 'object is None'

        return Response({'message': message})

    def patch(self, request, pk):
        obj = get_object_or_404(Choice, id=pk)
        if obj is not None:
            serializer = ChoiceModelSerializer(instance=obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = 'updated successfully'
            else:
                message = 'can not updated'
        else:
            message = 'object is None'

        return Response({'message': message})

    def delete(self, request, pk):
        obj = get_object_or_404(Choice, id=pk)
        if obj is not None:
            obj.delete()
            return Response({"message": "object Deleted"})
        return Response({"message": "object is None"})


"""Pure Django"""


def index(request):
    object = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': object,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})


def questionvote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selectd_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'you didnot select a choice.'
        })
    else:
        selectd_choice.vote += 1
        selectd_choice.save()

    return HttpResponseRedirect(
        reverse('polls:results', args=(question.id))
    )

'''
Class View Sections
'''


class QuestionPollsObjectsMixin(object):
    _model = Questions

    def get_objecttt(self):
        question_id = self.kwargs.get('question_id')
        obj = None
        if question_id is not None:
            obj = get_object_or_404(self._model, pk=question_id)
        return obj


class QuestionIndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    queryset = Questions.objects.order_by('-pub_date')[:5]


class QuestionResultView(generic.DetailView):
    model = Questions
    context_object_name = 'question'
    template_name = 'polls/result.html'


class QuestionCreateView(generic.CreateView):
    template_name = 'polls/polls_create.html'

    def get(self, request, *args, **kwargs):
        form = QuestionModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = QuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = QuestionModelForm()
        return render(request, self.template_name, {'form': form})


class QuestionDeleteView(generic.DeleteView, QuestionPollsObjectsMixin):
    template_name ='polls/polls_delete.html'

    def get(self, request, question_id=None, *args, **kwargs):
        object = self.get_objecttt()
        context = {}
        if object is not None:
            context['object'] = object
        return render(request, self.template_name, context)

    def post(self, request, question_id=None, *args, **kwargs):
        # object = get_object_or_404(Questions, pk=question_id)
        object = self.get_objecttt()
        context = {}
        if object is not None:
            object.delete()
            context['object'] = None
            return redirect('/polls/')
        return redirect('polls/')


class QuestionUpdateView(generic.UpdateView, QuestionPollsObjectsMixin):
    template_name = 'polls/polls_update.html'

    def get(self, request, question_id=None, *args, **kwargs):
        obj = self.get_objecttt()
        context = {}
        if obj is not None:
            form = QuestionModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, question_id=None, *args, **kwargs):
        obj = self.get_objecttt()
        context = {}
        if obj is not None:
            form = QuestionModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)


'''Choice Class Views'''

class ChoicePollsObjectsMixin(object):
    _model = Choice

    def get_objecttt(self):
        question_id = self.kwargs.get('question_id')
        obj = None
        if question_id is not None:
            obj = self._model.object.get(question=question_id)
        return obj


class ChoiceIndexView(generic.ListView):
    template_name = 'choice/index.html'

    def get(self, request, question_id=None, *args, **kwargs):
        question = get_object_or_404(Questions, id=question_id)
        choices = question.choice_set.all()
        return render(request, self.template_name, {'question': question, 'choices': choices})


class ChoiceDetailView(generic.DetailView):
    pass


class ChoiceResultView(generic.DetailView):
    pass


class ChoiceCreateView(generic.CreateView):
    template_name = 'choice/polls_create.html'
    model = Choice

    def get(self, request, *args, **kwargs):
        form = ChoiceModelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Questions, pk=kwargs.get('question_id'))
        form = ChoiceModelForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.question = question
            choice.save()
        return redirect(f"/polls/{question.id}/choice/")


class ChoiceUpdateView(generic.UpdateView):
    template_name = 'choice/polls_update.html'
    model = Choice

    def get(self, request, question_id, *args, **kwargs):
        choice_id = kwargs.get('choice_id')
        obj = get_object_or_404(self.model, id=choice_id)
        form = ChoiceModelForm(instance=obj)
        return render(request, self.template_name, {'form': form, 'object': obj})

    def post(self, request, question_id, *args, **kwargs):
        obj = get_object_or_404(self.model, id=kwargs.get('choice_id'))
        if obj is not None:
            form = ChoiceModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
        return redirect(f"/polls/{obj.question.id}/choice/")


class ChoiceDeleteView(generic.DeleteView):
    template_name = 'choice/polls_delete.html'
    model = Choice

    def get(self, request, *args, **kwargs):
        choice_id = kwargs.get('choice_id')
        obj = get_object_or_404(self.model, id=choice_id)
        form = ChoiceModelForm(instance=obj)
        return render(request, self.template_name, {'form': form, 'object': obj})

    def post(self, request, *args, **kwargs):
        choice_id = kwargs.get('choice_id')
        obj = get_object_or_404(self.model, id=choice_id)
        if obj is not None:
            obj.delete()
        return redirect(f"/polls/{obj.question.id}/choice/")
