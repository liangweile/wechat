# -*- coding:utf-8 -*-
from django.shortcuts import render
from Shop.models import goods, shopcart, consignee, order, comment, category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import random

#输出随机码
def generate_random_str(randomlength):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str)-1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

# Create your views here.
# 首页
def index(request):
    goods_list = goods.objects.all()
    return render(request, 'index.html', {'goods_list': goods_list})

# 我的
@login_required
def member(request):
    return render(request, 'member.html')


# 系统设置
def step(request):
    return render(request, 'step.html')


# 关于
def about(request):
    return render(request, 'about.html')


# 个人资料
def infor(req):
    return render(req, 'infor.html')


# 安全设置
def saftystep(req):
    return render(req, 'saftystep.html')


# 注册
def reg(req):
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']
        user = User.objects.create_user(username=username, password=password)
        shopcart.objects.create(user=user)
        user.save()
        return HttpResponseRedirect('/member.html')
    return render(req, 'reg.html')


# 登录
def mylogin(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, '登录成功,跳转到首页')
        else:
            messages.error(request, '帐号或密码错误！')
    return render(request, 'login.html')


# 退出登录
def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/index.html')


# 购物车
@login_required
def shopcart_views(req):
    user = User.objects.get(username=req.user.username)
    if req.POST:
        goods_number = req.POST['number']
        goods_id = req.POST['goods_id']
        good = goods.objects.get(id=goods_id)
        good.goods_shopcart_number += int(goods_number)
        good.save()
        user.shopcart.goods_set.add(good)
        goods_list = user.shopcart.goods_set.all()
        all_price = 0
        for goods_ in goods_list:
            all_price += goods_.price * goods_.goods_shopcart_number
        user.shopcart.goods_all_price = all_price
        user.shopcart.save()
        return render(req, 'shopcart.html', {"goods_list": goods_list, "shopcart": user.shopcart})
    user = User.objects.get(username=req.user.username)
    goods_list = user.shopcart.goods_set.all()
    return render(req, 'shopcart.html', {"goods_list": goods_list, "shopcart": user.shopcart})


# 所有订单
@login_required
def allorder(req):
    if req.POST:
        user = User.objects.get(username=req.user.username)
        statue = req.POST['statue']
        orders = user.order_set.filter(statue=statue)
        return render(req, 'allorder.html',{"orders":orders,"statue":req.POST['statue']})
    user = User.objects.get(username=req.user.username)
    orders = user.order_set.all()
    return render(req, 'allorder.html', {'orders': orders,"statue":"全部"} )
#删除订单
def delorder(req):
    user = User.objects.get(username=req.user.username)
    user.order_set.get(order_id=req.POST['order_id']).delete()
    user.save()
    orders = user.order_set.all()
    return render(req, 'allorder.html', {'orders': orders,"statue":"全部"} )
#取消订单
def cancelorder(req):
    user = User.objects.get(username=req.user.username)
    order_get = user.order_set.get(order_id=req.POST['order_id'])
    order_get.statue = "退发货"
    order_get.save()
    orders = user.order_set.all()
    return render(req, 'allorder.html', {'orders': orders,"statue":"全部"} )

# 订单
def order_views(req):
    user = User.objects.get(username=req.user.username)
    consignee_order = user.consignee_set.get(consignee_sign=True)
    order_new = user.order_set.create(user=user, order_pk=consignee_order, order_id=generate_random_str(16))
    price = 0
    for i in range(0, len(req.POST)):
        id_num = req.POST[str(i)]
        id_num_split = id_num.split(':')
        goods_id = id_num_split[0]
        goods_num = id_num_split[1]
        good = goods.objects.get(id=goods_id)
        order_new.goods_set.add(good)
        user.shopcart.goods_set.remove(good)
        good.goods_shopcart_number = 0
        price += int(goods_num) * good.price
        order_new.order_price = price
        order_new.order_price_pay = price
        good.save()
        order_new.save()
    goods_list = order_new.goods_set.all()
    order_consignee = order_new.order_pk
    return render(req, 'order.html', {'goods_list':goods_list, 'order_consignee':order_consignee, 'order_price':price,'order_id':order_new.order_id})


@login_required
# 结算
def tureorder(req):
    tureorder_list = []
    price = 0
    for i in range(0, len(req.POST)):
        id_num = req.POST[str(i)]
        id_num_split = id_num.split(':')
        goods_id = id_num_split[0]
        goods_num = id_num_split[1]
        good = goods.objects.get(id=goods_id)
        good.goods_order_number = goods_num
        good.save()
        price += good.price * int(goods_num)
        tureorder_list.append(good)
    return render(req, 'tureorder.html', {"goods_list": tureorder_list, "allprice":price})


# 订单详情
def orderdetail(req):
    order_get = order.objects.get(order_id=req.POST['order_id'])
    consignee_get = order_get.order_pk
    goods_get = order_get.goods_set.all()
    return render(req, 'orderdetail.html',{'goods_list':goods_get,'order':order_get,'consignee':consignee_get})


# 显示所有地址和设置默认地址
def gladdress(req):
    user = User.objects.get(username=req.user.username)
    if req.POST:
        consignee_true = user.consignee_set.get(consignee_sign=True)
        consignee_true.consignee_sign = False
        consignee_true.save()
        consignee_set = user.consignee_set.get(consignee_id=req.POST['input1'])
        consignee_set.consignee_sign = True
        consignee_set.save()
    consignee_all = user.consignee_set.all()
    return render(req, 'gladdress.html', {'consignee_all': consignee_all})

#删除地址
def deladdress(req):
    user = User.objects.get(username=req.user.username)
    if req.POST:
        user.consignee_set.get(consignee_id=req.POST['input2']).delete()
        user.save()
    consignee_all = user.consignee_set.all()
    return render(req, 'gladdress.html', {'consignee_all': consignee_all})


# 新增收货地址
def address(req):
    if req.POST:
        user = User.objects.get(username=req.user.username)
        if (len(req.POST) == 4):
            try:
                consignee_sign_True = user.consignee_set.get(consignee_sign=True)
                consignee_sign_True.consignee_sign = False
                consignee_sign_True.save()
                consignee.objects.create(user=user, consignee_sign=True, consignee_name=req.POST['name'],
                                         consignee_address=req.POST['address'], consignee_phone=req.POST['phone'],consignee_id=generate_random_str(16))
            except ObjectDoesNotExist:
                consignee.objects.create(user=user, consignee_sign=True, consignee_name=req.POST['name'],
                                         consignee_address=req.POST['address'], consignee_phone=req.POST['phone'],consignee_id=generate_random_str(16))
        else:
            consignee.objects.create(user=user, consignee_sign=False, consignee_name=req.POST['name'],
                                     consignee_address=req.POST['address'], consignee_phone=req.POST['phone'],consignee_id=generate_random_str(16))

        user = User.objects.get(username=req.user.username)
        consignee_all = user.consignee_set.all()
        return render(req, 'gladdress.html', {'consignee_all': consignee_all})
    return render(req, 'address.html')


# 动态
@login_required
def message(req):
    return render(req, 'message.html')


# 分类
def category_views(req):
    if req.POST:
        category_get = category.objects.get(category_name=req.POST['name'])
        goods_all = category_get.goods_set.all()
        return render(req, 'category.html',{'goods_all':goods_all,'category':category_get})
    category_apple = category.objects.get(category_name='苹果')
    goods_apple = category_apple.goods_set.all()
    return render(req, 'category.html', {'goods_all': goods_apple, 'category': category_apple})


#评价
def comment_views(req):
    if "order_id" in req.POST:
        order_comment = order.objects.get(order_id = req.POST["order_id"])
        goods_list = order_comment.goods_set.all()
        return render(req, 'comment.html',{"goods_list":goods_list})
    else:
        comment_text = req.POST['text']
        comment_level = req.POST['radiovalue']
        for i in range(0, len(req.POST)-2):
            goods_id = req.POST[str(i)]
            goods_comment = goods.objects.get(id=goods_id)
            new_comment = comment.objects.create(comment_name=req.user.username, comment_content=comment_text, comment_level=comment_level)
            goods_comment.comment_set.add(new_comment)
            goods_comment.save()
            return HttpResponse("1")
#添加评价
def addcomment(req):
    return HttpResponse("")

# 收藏
def collect(req):
    if req.POST:
        goods_collect = goods.objects.get(id=req.POST["goods_id"])
        user = User.objects.get(username=req.user.username)
        user.goods_set.add(goods_collect)
        user.save()
    user = User.objects.get(username=req.user.username)
    goods_collect = user.goods_set.all()
    return render(req, "collect.html", {'goods_collect':goods_collect})


# 收藏编辑
def collect_edit(req):
    user = User.objects.get(username=req.user.username)
    goods_collect = user.goods_set.all()
    return render(req, 'collect-edit.html',{"goods_collect":goods_collect})

#收藏删除
def delcollect(req):
    user = User.objects.get(username=req.user.username)
    for i in range(0,len(req.POST)):
        collect_del = goods.objects.get(id=req.POST[str(i)])
        user.goods_set.remove(collect_del)
        user.save()
    goods_collect = user.goods_set.all()
    return render(req, 'collect-edit.html',{"goods_collect":goods_collect})

# 联系人
def contact(req):
    return render(req, 'contact.html')


# 商品详情
def detail(req, goods_id):
    good = 0
    middle = 0
    bad = 0
    if req.user.is_authenticated:
        user = User.objects.get(username=req.user.username)
        goods_list = user.goods_set.all()
        goods_detail = goods.objects.get(id=goods_id)
        if goods_detail in goods_list:
            sign = 1
        else:
            sign = 0
        comment_list = goods_detail.comment_set.all()
        for com in comment_list:
            if com.comment_level == 'good':
                good += 1
            elif com.comment_level == 'middle':
                middle += 1
            else:
                bad += 1
        if ((good!=0)|(middle!=0)|(bad!=0)):
            good_bili = good/(good+middle+bad)*100
            middle_bili = middle/(good+middle+bad)*100
            bad_bili = bad/(good+middle+bad)*100
        else:
            good_bili = 0
            middle_bili = 0
            bad_bili = 0
        return render(req, 'detail.html', {'goods_detail': goods_detail, "collect":sign, "comment_list":comment_list,
                                           'good':good,'middle':middle,'bad':bad,
                                           'good_bili': good_bili,
                                           'middle_bili': middle_bili,
                                           'bad_bili': bad_bili
                                           })
    else:
        goods_detail = goods.objects.get(id=goods_id)
        return render(req, 'detail.html', {'goods_detail':goods_detail,
                                           'good':good,'middle':middle,'bad':bad,
                                           'good_bili':good_bili,
                                           'middle_bili':middle_bili,
                                           'bad_bili':bad_bili})



# 忘记密码
def forgetpassword(req):
    return render(req, 'forgetpassword.html')


# 积分
def integral(req):
    user = User.objects.get(username=req.user.username)
    if req.POST:
        return HttpResponse(user.jifen)
    return render(req, 'integral.html',{'user':user})


# 积分兑换
def integralexchange(req):
    return render(req, 'integralexchange.html')


# 积分兑换记录
def integralrecords(req):
    return render(req, 'integralrecords.html')





# 动态详情
def messdetail(req):
    return render(req, 'messdetail.html')




# 我的钱包
def money(req):
    return render(req, 'money.html')




# 我的推荐
def myrecommend(req):
    return render(req, 'myrecommend.html')


# 新闻
def news(req):
    return render(req, 'news.html')




# 密码
def password(req):
    if req.POST:
        username = req.POST['username']
        old_password = req.POST['old_password']
        new_password = req.POST['new_password']
        user = authenticate(req, username=username, password=old_password)
        if new_password != '':
            if user:
                user = User.objects.get(username=username)
                user.set_password(new_password)
                user.save()
                messages.info(req, '修改成功需重新登录')
            else:
                messages.error(req, '帐号或密码错误')
        else:
            messages.error(req, '新密码为空')
    return render(req, 'password.html')


# 支付
def pay(req):
    user = User.objects.get(username=req.user.username)
    order_get = user.order_set.get(order_id=req.POST["order_id"])
    if(len(req.POST)>1):
        order_get.pay_method = req.POST["paymethod"]
        if req.POST["paymethod"]=="zhanghu":
            balance = user.money - order_get.order_price_pay
            if balance >=0:
                user.money = balance
                messages.info(req, "支付成功,跳转到主页")
                user.save()
                order_get.statue = "待收货"
                order_get.save()
            else:
                messages.error(req, "支付失败,跳转到充值")
    return render(req, 'pay.html',{"order":order_get})

# 支付密码
def payment(req):
    return render(req, "payment.html")


# 充值
def recharge(req):
    return render(req, 'recharge.html')


# 推荐有奖
def recommend(req):
    return render(req, 'recommend.html')


# 账户余额
def records(req):
    user = User.objects.get(username=req.user.username)
    return render(req, 'records.html',{'user':user})



# 消息中心
def tidings(req):
    return render(req, 'tidings.html')


# 过期红包
def ygq(req):
    return render(req, 'ygq.html')


# 可使用红包
def yhq(req):
    return render(req, 'yhq.html')


class Mybackend(ModelBackend):
    def authenticate(self, username=None, password=None, ):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
