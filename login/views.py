from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from .permissions import UserProfilePermission
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token


"Login Page"


class UserLogin(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


"""APIViews"""


class HelloApiView(APIView):
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (UserProfilePermission,
    #                       IsAuthenticatedOrReadOnly)

    def get(self, request, pk=None):
        if pk is not None:
            users = get_object_or_404(UserProfile, pk=pk)
            sir = self.serializer_class(users)
            return Response(sir.data)
        else:
            users = UserProfile.objects.all()
            sir = self.serializer_class(users, many=True)
            return Response(sir.data)
        return Response(self.serializer_class)

    def post(self, request, pk=None):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)
        req_data = request.data
        print(req_data)
        serializer = UserProfileSerializer(instance=user, data=req_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = f'user profile {pk} updated successfully'
        else:
            message = f'cant update user profile {pk} update is  unsuccessful'

        return Response({'message': message})

    def patch(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)
        req_data = request.data
        serializer = UserProfileSerializer(instance=user, data=req_data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = f'user profile {pk} updated successfully completely'
        else:
            message = f'cant update user profile {pk} update is  unsuccessful'

        return Response({'message': message})

    def delete(self, request, pk):
        user = get_object_or_404(UserProfile, pk=pk)
        if user is not None:
            user.delete()
            message = f'user {pk} successfully deleted.'
        else:
            message = f'cant delete user {pk}.'
        return Response({'message': message})


"""ViewSets"""


class HelloViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserProfilePermission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
