from django.contrib import admin

from django_simple_coupons.models import (Coupon,
                                          Discount,
                                          Ruleset,
                                          CouponUser,
                                          AllowedUsersRule,
                                          MaxUsesRule,
                                          ValidityRule)

from django_simple_coupons.actions import (reset_coupon_usage, delete_expired_coupons)


# Register your models here.
# ==========================
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'ruleset', 'times_used', 'created', )
    search_fields=['code']
    actions = [delete_expired_coupons]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display=("__str__",'value','is_percentage',)


@admin.register(Ruleset)
class RulesetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'allowed_users', 'max_uses', 'validity', )


@admin.register(CouponUser)
class CouponUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'coupon', 'times_used', )
    search_fields = ['user__username', 'coupon__code']
    autocomplete_fields=['user']
    actions = [reset_coupon_usage]


@admin.register(AllowedUsersRule)
class AllowedUsersRuleAdmin(admin.ModelAdmin):
    list_display=('__str__','all_users',)
    autocomplete_fields=['users']
    # def get_model_perms(self, request):
    #     return {}


@admin.register(MaxUsesRule)
class MaxUsesRuleAdmin(admin.ModelAdmin):
    list_display=('__str__','max_uses','is_infinite','uses_per_user',)
    # def get_model_perms(self, request):
    #     return {}


@admin.register(ValidityRule)
class ValidityRuleAdmin(admin.ModelAdmin):
    list_display=('__str__','expiration_date','is_active',)
    # def get_model_perms(self, request):
    #     return {}
