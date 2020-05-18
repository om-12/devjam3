from django.contrib import admin
from .models import Rentyourhouse
from .models import rent1payee
from .models import Feedback
from .models import Image


admin.site.register(rent1payee)
admin.site.register(Rentyourhouse)
admin.site.register(Feedback)
admin.site.register(Image)