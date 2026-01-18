from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
<<<<<<< HEAD

from user.models import User
=======
from .models import User
>>>>>>> 1f225beee00415b859782acdae7cb6ded83764f9

admin.site.register(User, UserAdmin)
