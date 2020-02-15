# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    return HttpResponse("<p>" + list + "</p>")