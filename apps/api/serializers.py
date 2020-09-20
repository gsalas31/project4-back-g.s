from rest_framework import serializers
from apps.api.models import Category, Product, Comment, Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tutorial
        fields = ('id', 'title', 'description', 'image', 'materials', 'procedure', 'owner', 'category',
                  'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'subject', 'the_comment', 'owner', 'product', 'created_at', 'updated_at')



class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'image', 'description', 'owner','category', 'comments', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    products = ProductSerializer(many=True, read_only=True, required=False)
    tutorials = TutorialSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Category
        fields = ('id', 'name', 'owner', 'products', 'tutorials', 'created_at', 'updated_at')