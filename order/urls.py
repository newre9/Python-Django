from django.urls import path

from . import views
app_name ='order'#uygulamanın adını path ile çağırmak için
urlpatterns = [
    path('', views.index, name='index'),
    path('shopcart', views.shop_cart_list, name='shopcart'),
    path('addtocart/<int:proid>', views.shop_cart_add, name='addtocart'),
    path('deletefromcart/<int:id>', views.shop_cart_delete, name='deletefromcart'),
    path('checkout', views.shop_cart_checkout, name='checkout'),
    path('detail/<int:id>', views.order_detail, name='orderdetail'),



    # ex: /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
  #  path('<int:question_id>/vote/', views.vote, name='vote'),
]