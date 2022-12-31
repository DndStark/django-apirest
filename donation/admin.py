from django.contrib import admin
from .models import UserType, Person, User, Condition, ConditionList, Category, Campaign, Location, DonationDetail

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('user_type_name', 'user_type_description', 'user_type_state')
admin.site.register(UserType, UserTypeAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'person_document', 'person_address', 'person_photo', 'person_phone')
admin.site.register(Person, PersonAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_password', 'user_state', 'person', 'user_type')
admin.site.register(User, UserAdmin)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('condition_name', 'condition_description')
admin.site.register(Condition, ConditionAdmin)

class ConditionListAdmin(admin.ModelAdmin):
    list_display = ('category', 'condition')
admin.site.register(ConditionList, ConditionListAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'category_logo')
admin.site.register(Category, CategoryAdmin)

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('campaign_name', 'campaign_description', 'campaign_start_date', 'campaign_finish_date', 'user', 'location')
admin.site.register(Campaign, CampaignAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_latitude', 'location_latitude', 'location_longitude', 'location_reference')
admin.site.register(Location, LocationAdmin)

class DonationDetailAdmin(admin.ModelAdmin):
    list_display = ('detail_expiration_state', 'detail_expiration_date', 'detail_amount', 'detail_observation', 'detail_solidarity_points', 'detail_register_date')
admin.site.register(DonationDetail, DonationDetailAdmin)