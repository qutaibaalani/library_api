from rest_framework import serializers
from .models import User, Book, Author, Tracker


# Serializer for the Tracker model
class TrackerSerializer(serializers.ModelSerializer):
    # Use the StringRelatedField for the book field
    book = serializers.StringRelatedField()

    class Meta:
        model = Tracker
        fields = (
            "id",
            "user",
            "book",
            "status",
        )


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    # Use the TrackerSerializer for the trackings_of_user field
    trackings_of_user = TrackerSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "trackings_of_user",
        )


# Serializer for the Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "date_published",
            "genre",
            "featured",
        )


# Serializer for the Author model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "name",
        )
