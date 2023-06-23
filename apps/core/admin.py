from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, Issues, IssueCategories, Videos, Courses, Classroom


@admin.register(Users)
class UsersAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'country', 'is_staff', 'is_superuser')
    list_editable = ('is_staff', 'is_superuser')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('İzinler', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
        ('Tarihler', {'fields': ('last_login',)}),
        ('Ekstra Profil Alanları', {'fields': ('gender', 'avatar', 'birth_date', 'country', 'bio',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'groups'),
        }),
    )


admin.site.register(IssueCategories)
admin.site.register(Issues)
admin.site.register(Videos)
admin.site.register(Courses)
admin.site.register(Classroom)
