from django.contrib.admin import register, ModelAdmin
from .models import OTP

@register(OTP)
class OtpAdmin(ModelAdmin):...
