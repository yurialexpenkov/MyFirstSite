from django.contrib import admin
from app_news.models import News, MyComment
from django.contrib.auth.models import User



class MyCommentInline(admin.TabularInline):
	model = MyComment

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'status_verifications', ]
    list_filter = ['activity']
    inlines = [MyCommentInline]

    actions = ['mark_as_active', 'mark_as_not_active']

    def mark_as_active(self, request, queryset):
        queryset.update(status_verifications='a')
        print(queryset.values_list)
        profile_id = queryset.values_list("user_id", flat=True)
        print(profile_id)
        for id in profile_id:
            user = User.objects.get(id=id)
            print(user)
            user.profile.count_of_news += 1
            user.profile.save()
            print(user.profile.count_of_news)

    def mark_as_not_active(self, request, queryset):
        queryset.update(status_verifications='n')
        print(queryset.values_list)
        profile_id = queryset.values_list("user_id", flat=True)
        print(profile_id)
        for id in profile_id:
            user = User.objects.get(id=id)
            user.profile.count_of_news -= 1
            user.profile.save()
            print(user.profile.count_of_news)

    mark_as_active.short_description = 'Перевести в статус активно'
    mark_as_not_active.short_description = 'Перевести в статус неактивно'


class MyCommentAdmin(admin.ModelAdmin):
    list_display = ['user_name', MyComment.trim15, 'news', 'user']
    list_filter = ['user_name']
    actions = ['deleted_by_the_administrator',]

    def deleted_by_the_administrator(self, request, queryset):
        queryset.update(comment_text='Удалено администратором')

admin.site.register(News, NewsAdmin)
admin.site.register(MyComment, MyCommentAdmin)

