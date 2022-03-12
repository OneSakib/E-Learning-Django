from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsEnrolled
from .serializers import CourseWithContentSerializer
from rest_framework import authentication
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions



class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    # authentication_classes = [BaseAuthentication]
    permission_classes = [IsAuthenticated, ]

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(methods=['post'],
            detail=True)
    def enroll(self, request, *args, **kwargs):
        course = self.get_queryset()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(methods=['get'],
            permission_classes=[IsAuthenticated, IsEnrolled],
            detail=True)
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
