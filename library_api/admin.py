from django.contrib import admin
from .models import Book, Author, User, Tracker

# Register your models here.


# Register the User model with the admin site
admin.site.register(User)

# Register the Book model with the admin site
admin.site.register(Book)

# Register the Author model with the admin site
admin.site.register(Author)

# Register the Tracker model with the admin site
admin.site.register(Tracker)
