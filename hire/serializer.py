from rest_framework import serializers
from .models import AccessibleChoice, ACCESS_CODE_STATUS_CHOICE

class AccessibleChoiceSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=8)
    user = serializers.ForeignKey(User, related_name='access_code')
    email = serializers.EmailField(max_length=255)
    status = serializers.ChoiceField(max_length=10, choices=ACCESS_CODE_STATUS_CHOICE,)

    class Meta:
        model = AccessibleChoice
        fields = ['access','user','email','status']