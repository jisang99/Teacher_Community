from django.contrib import admin
from .models import Funding

@admin.register(Funding)
class FundingAdmin(admin.ModelAdmin):
    list_display = ('title', 'formatted_amount', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def formatted_amount(self, obj):
        return obj.formatted_amount()

    formatted_amount.short_description = 'Amount'

    # formatted_amount 함수를 사용하여 계산된 필드를 어드민 목록에서 표시합니