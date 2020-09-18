from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from apps.api.views import CategoryViewSet, CategoryProducts, SingleCategoryProduct, ProductsViewSet,\
    CategoryTutorials, SingleCategoryTutorial, TutorialViewSet, SingleProductComment,\
    CommentViewSet, ProductComments

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductsViewSet, basename='products')
router.register('comments', CommentViewSet, basename='comments')
router.register('tutorials', TutorialViewSet, basename='tutorials')

custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/products$', CategoryProducts.as_view(), name='category_products'),
    url(r'categories/(?P<category_pk>\d+)/products/(?P<pk>\d+)$', SingleCategoryProduct.as_view(),
        name='single_category_product'),
    url(r'categories/(?P<category_pk>\d+)/tutorial$', CategoryTutorials.as_view(), name='category_tutorials'),
    url(r'categories/(?P<category_pk>\d+)/tutorials/(?P<pk>\d+)$', SingleCategoryTutorial.as_view(),
        name='single_category_tutorial'),
    url(r'categories/(?P<category_pk>\d+)/products/(?P<pk>\d+)/comments$', ProductComments.as_view(),
        name='product_comments'),
    url(r'products/(?P<pk>\d+)/comments$', SingleProductComment.as_view(),
        name='single_product_comments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

urlpatterns = router.urls
urlpatterns += custom_urlpatterns



# urlpatterns = [
#     path('', include(router.urls))
#
# ]