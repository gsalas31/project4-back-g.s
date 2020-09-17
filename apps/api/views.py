from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.api.models import Category, Product, Comment, Tutorial
from apps.api.serializers import CategorySerializer, ProductSerializer, CommentSerializer, TutorialSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all().filter(owner=self.request.user)

    def perform_create(self, request, *args, **kwargs):
        #check if the category already exists
        category = Category.objects.filter(
            name=request.data.get('name'),
            owner=request.user
        )
        if category:
            msg = 'Category already exists'
            raise ValidationError(msg)
        return super().create(request)

    def perform_create(self, serializer):
        #everything is been saved to that particular user
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        category = Category.objects.get(pk=self.kwargs['pk'])
        if not request.user == category.owner:
            raise PermissionDenied('You are not allow to delete this category')
        return super().destroy(request, *args, **kwargs)










class CategoryProducts(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Product.objects.filter(
                owner=self.request.user,
                category=category
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SingleCategoryProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def get_queryset(self):
        #localhost:800/categories/category/category_pk<1>/products/pk<1>/
        if self.kwargs.get("category_pk") and self.kwargs.get('pk'):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Product.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                category=category
            )
            return queryset













class CategoryTutorials(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TutorialSerializer

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Tutorial.objects.filter(
                owner=self.request.user,
                category=category
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SingleCategoryTutorial(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TutorialSerializer

    def get_queryset(self):
        # localhost:800/categories/category/category_pk<1>/tutorial/pk<1>/
        if self.kwargs.get("category_pk") and self.kwargs.get('pk'):
            category = Category.objects.get(pk=self.kwargs['category_pk'])
            queryset = Tutorial.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                category=category
            )
            return queryset









class ProductComments(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.kwargs.get('product_pk'):
            product = Product.objects.get(pk=self.kwargs['product_pk'])
            queryset = Comment.objects.filter(
                owner=self.request.user,
                product=product
            )
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SingleProductComment(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        # localhost:800/products/product/product_pk<1>/comment/pk<1>/
        if self.kwargs.get("product_pk") and self.kwargs.get('pk'):
            product = Product.objects.get(pk=self.kwargs['product_pk'])
            queryset = Comment.objects.filter(
                pk=self.kwargs['pk'],
                owner=self.request.user,
                product=product
            )
            return queryset


