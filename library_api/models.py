from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


# Create your models here.


# Create a custom User model inheriting from AbstractUser
class User(AbstractUser):
    pass


# Create the Book model
class Book(models.Model):
    # Choices for the genre field
    CHOICES = (
        ("adventure", "Adventure"),
        ("historical", "Historical"),
        ("mystery", "Mystery"),
        ("science", "Science"),
        ("fantasy", "Fantasy"),
        ("drama", "Drama"),
    )

    # Fields for the Book model
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to="Author", on_delete=models.CASCADE)
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)
    featured = models.BooleanField(default=False)

    class Meta:
        # Specify a unique constraint for title and author combination
        constraints = [UniqueConstraint(fields=["title", "author"], name="constraints")]

    def __str__(self):
        return self.title


# Create the Author model
class Author(models.Model):
    # Field for the Author model
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create the Tracker model
class Tracker(models.Model):
    # Choices for the status field
    CHOICES = (
        ("pending", "Pending"),
        ("in progress", "In Progress"),
        ("completed", "Completed"),
        ("on hold", "On Hold"),
        ("abandoned", "Abandoned"),
    )

    # Fields for the Tracker model
    user = models.ForeignKey(
        to="User", on_delete=models.CASCADE, related_name="trackings_of_user"
    )
    book = models.ForeignKey(
        to="Book", on_delete=models.CASCADE, related_name="trackings_of_book"
    )
    status = models.CharField(choices=CHOICES, max_length=50)

    class Meta:
        # Specify a unique constraint for user and book combination
        constraints = [
            UniqueConstraint(fields=["user", "book"], name="tracker_constraints")
        ]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}: {self.status}"
