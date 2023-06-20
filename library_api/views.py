from django.shortcuts import render
from rest_framework import generics, filters, permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, User, Author, Tracker
from .serializers import BookSerializer, TrackerSerializer


# Create your views here.


class BookList(generics.ListCreateAPIView):
    # Set the queryset to fetch all Book objects
    queryset = Book.objects.all()
    # Use the BookSerializer for serialization/deserialization
    serializer_class = BookSerializer
    # Enable DjangoFilterBackend for filtering based on model fields
    filter_backends = [DjangoFilterBackend]
    # Specify the fields to be used for filtering
    filterset_fields = ["featured"]
    # Specify the fields to be used for searching
    search_fields = ["title", "author__name"]

    # Handle POST requests for creating new Book objects
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    # Set the queryset to fetch all Book objects
    queryset = Book.objects.all()
    # Use the BookSerializer for serialization/deserialization
    serializer_class = BookSerializer
    # Set the permission class to restrict access to admin users
    permission_classes = [IsAdminUser]

    # Handle PUT requests for updating Book objects
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Handle PATCH requests for partially updating Book objects
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # Handle DELETE requests for deleting Book objects
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserTracker(generics.ListCreateAPIView):
    # Set the queryset to fetch all Tracker objects
    queryset = Tracker.objects.all()
    # Use the TrackerSerializer for serialization/deserialization
    serializer_class = TrackerSerializer
    # Enable DjangoFilterBackend for filtering based on model fields
    filter_backends = [DjangoFilterBackend]
    # Specify the fields to be used for filtering
    filterset_fields = ["status"]

    # Perform additional steps during object creation
    def perform_create(self, serializer):
        # Set the user field of the Tracker object to the current user
        serializer.save(user=self.request.user)

    # Filter the queryset to only include Tracker objects for the current user
    def get_queryset(self):
        queryset = Tracker.objects.filter(user=self.request.user)
        return queryset
