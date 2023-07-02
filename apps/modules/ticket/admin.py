from django.contrib import admin
from .models import *


admin.site.register(Ticket)
admin.site.register(TicketStatuses)
admin.site.register(TicketPriorities)
admin.site.register(TicketCategories)
admin.site.register(TicketMessages)
