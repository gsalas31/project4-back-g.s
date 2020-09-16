from rest_framework import serializers
from apps.api.models import Tutorial, Product

class TutorialSerializer(serializers.ModelSerializer):
    #can i do  'owner.fullname' ?
    owner = serializers.ReadOnlyField(source='owner.fullname')

    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'description', 'owner','image', 'material', 'procedure', 'created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.fullname')

    class Meta:
        model = Product
        fields = ('id', 'description', 'owner','image', 'created_at', 'updated_at')