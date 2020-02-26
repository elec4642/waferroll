# Create your views here.
from product.models import milk
from django.shortcuts import render


#数据库操作
def milk_price(request):

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list_product = milk.objects.all()
    context = {'product_list':list_product}
    #dict_product = dict(list_product)
    return render(request, 'milk.html', context)