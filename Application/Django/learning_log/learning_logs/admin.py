from django.contrib import admin
from learning_logs.models import Topic
from learning_logs.models import Entry


# Register your module here.

admin.site.register(Topic)
admin.site.register(Entry)