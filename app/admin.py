from django.contrib import admin

from parler.admin import TranslatableAdmin

from . models import UserInfo,Services,Skills,Education,Experience,Cuntuct_us,Portfolio

# @admin.register(Post)
# class PostAdmin(TranslatableAdmin):
#     list_display = ('title', 'content')
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'content'),
#         }),
#     )
#     def save_model(self, request, obj, form, change):
#         obj.author_id = request.user.id
#         super().save_model(request, obj, form, change)

@admin.register(UserInfo)
class UserInfoAdmin(TranslatableAdmin):
    list_display = ('full_name','title')

admin.register(Services)
class ServicesAdmin(TranslatableAdmin):
    list_display = ('title',)

admin.site.register(Education)
class EducationAdmin(TranslatableAdmin):
    list_display = ('degree','education_place')

admin.site.register(Experience)
class ExperienceAdmin(TranslatableAdmin):
    list_display = ('job_title','work_place')

admin.site.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('title',)
    
admin.site.register(Skills)
admin.site.register(Cuntuct_us)
