from django.contrib import admin

from app_users.models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'verification_flag', 'count_of_news']

    actions = ['translate_the_flag_to_the_truth', 'translate_the_flag_to_false']

    def translate_the_flag_to_the_truth(self, request, queryset):
        queryset.update(verification_flag=True)
        profile_id = queryset.values_list("user_id", flat=True)
        print(profile_id)
        for id in profile_id:
            user = User.objects.get(id=id)
            user_group = Group.objects.get(name='Верифицированные пользователи')
            user.groups.add(user_group)

    def translate_the_flag_to_false(self, request, queryset):
        queryset.update(verification_flag=False)
        profile_id = queryset.values_list("user_id", flat=True)
        print(profile_id)
        for id in profile_id:
            user = User.objects.get(id=id)
            user_group = Group.objects.get(name='Верифицированные пользователи')
            user.groups.remove(user_group)


admin.site.register(Profile, ProfileAdmin)