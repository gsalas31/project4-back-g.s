from rest_framework import serializers
from apps.api.models import Category, Product, Comment, Tutorial

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ('id', 'image', 'description', 'owner', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'subject', 'description', 'owner', 'created_at', 'updated_at')


class TutorialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'description', 'image', 'materials', 'procedure', 'owner', 'created_at', 'updated_at')