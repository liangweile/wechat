#-*- coding:utf-8 -*-
from django.shortcuts import render
from Shop.models import goods, shopcart, consignee, order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#首页
def index(request):
    goods_list = goods.objects.all()
    return render(request, 'index.html', {'goods_list':goods_list})

#我的
@login_required
def member(request):
    return render(request, 'member.html')

#系统设置
def step(request):
    return render(request, 'step.html')

#关于
def about(request):
    return render(request, 'about.html')

#个人资料
def infor(req):
    return render(req, 'infor.html')

#安全设置
def saftystep(req):
    return render(req, 'saftystep.html')
#注册
def reg(req):
    if req.POST:
        username = req.POST['username']
        password = req.POST['password']
        user = User.objects.create_user(username=username, password=password)
        shopcart_user = shopcart.objects.create(user=user)
        consignee_user = user.consignee_set.create(consignee_sign=True, consignee_name='', consignee_address='', consignee_phone='')
        order_user = user.order_set.create(user=user, order_pk=consignee_user)
        user.save()
        return HttpResponseRedirect('/member.html')
    return render(req, 'reg.html')


#登录
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
#退出登录
def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/index.html')

#购物车
@login_required
def shopcart_views(req):
    if req.POST:
        goods_number = req.POST['number']
        goods_id = req.POST['goods_id']
        good = goods.objects.get(id=goods_id)
        good.goods_shopcart_number += int(goods_number)
        good.save()
        user = User.objects.get(username=req.user.username)
        user.shopcart.goods_set.add(good)
        goods_list = user.shopcart.goods_set.all()
        all_price=0
        for goods_ in goods_list:
            all_price += goods_.price * goods_.goods_shopcart_number
        user.shopcart.goods_all_price = all_price
        user.shopcart.save()
        return render(req, 'shopcart.html', {"goods_list": goods_list, "shopcart": user.shopcart})
    user = User.objects.get(username=req.user.username)
    goods_list = user.shopcart.goods_set.all()
    return render(req, 'shopcart.html', {"goods_list":goods_list, "shopcart":user.shopcart})

#所有订单
@login_required
def allorder(req):
    user = User.objects.get(username=req.user.username)
    orders = user.order_set.all()
    return render(req, 'allorder.html',{'orders':orders})
#订单
def order_views(req):
    user = User.objects.get(username=req.user.username)
    orderset = user.order_set.get(order_sign=True)
    orderset.order_sign = False
    goods_list = orderset.goods_set.all()
    for goods in goods_list:
        user.shopcart.goods_set.remove(goods)
        goods.goods_shopcart_number = 0
    order_consignee = orderset.order_pk
    orderset.save()
    return render(req, 'order.html', {'goods_list':goods_list, 'order_consignee':order_consignee,'shopcart':user.shopcart})

#结算
def tureorder(req):
    user = User.objects.get(username=req.user.username)
    order_consignee = user.consignee_set.get(consignee_sign=True)
    createorder = order.objects.create(user=user, order_pk=order_consignee)
    for i in range(0, len(req.POST)):
        goods_id = req.POST[str(i)]
        goods_order = goods.objects.get(id=goods_id)
        createorder.goods_set.add(goods_order)
        createorder.order_price += goods_order.price * goods_order.goods_shopcart_number
    goods_list = createorder.goods_set.all()
    createorder.save()
    return render(req, 'tureorder.html', {"goods_list":goods_list, "allprice":createorder.order_price})

#订单详情
def orderdetail(req):
    return render(req, 'orderdetail.html')

#收货地址
def gladdress(req):
    user = User.objects.get(username=req.user.username)
    consignee_all = user.consignee_set.all()
    return render(req, 'gladdress.html',{'consignee_all':consignee_all})

#动态
@login_required
def message(req):
    return render(req, 'message.html')

#新增收货地址
def address(req):
    return render(req, 'address.html')

#兼职申请记录
def application(req):
    return render(req, 'application.html')

#兼职申请表
def applicationjob(req):
    return render(req, 'applicationjob.html')

#绑定手机
def boundphone(req):
    return render(req, 'boundphone.html')

#分类
def category(req):
    return render(req, 'category.html')

#选择城市
def city(req):
    return render(req, 'city.html')

#收藏
def collect(req):
    return render(req, 'collect.html')

#收藏编辑
def collect_edit(req):
    return render(req, 'collect-edit.html')

#联系人
def contact(req):
    return render(req, 'contact.html')

#商品详情
def detail(req, goods_id):
    goods_detail = goods.objects.get(id=goods_id)
    return render(req, 'detail.html', {'goods_detail':goods_detail})

#忘记密码
def forgetpassword(req):
    return render(req, 'forgetpassword.html')

#积分
def integral(req):
    return render(req, 'integral.html')

#积分兑换
def integralexchange(req):
    return render(req, 'integralexchange.html')

#积分兑换记录
def integralrecords(req):
    return render(req, 'integralrecords.html')

#兼职
def job(req):
    return render(req, 'job.html')

#商店
def list(req):
    return render(req, 'list.html')

#动态详情
def messdetail(req):
    return render(req, 'messdetail.html')

#动态成功
def messdetailactive(req):
    return render(req, 'messdetailactive.html')

#我的钱包
def money(req):
    return render(req, 'money.html')

#我的动态
def mymessage(req):
    return render(req, 'mymessage.html')

#我的推荐
def myrecommend(req):
    return render(req, 'myrecommend.html')

#新闻
def news(req):
    return render(req, 'news.html')

#新闻详情
def newsdetail(req):
    return render(req, 'newdetail.html')


#密码
def password(req):
    if req.POST:
        username = req.POST['username']
        old_password = req.POST['old_password']
        new_password = req.POST['new_password']
        user = authenticate(req, username=username, password=old_password)
        if new_password!='':
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

#支付
def pay(req):
    return render(req, 'pay.html')

#支付密码
def payment(req):
    return render(req, 'payment.html')

#充值
def recharge(req):
    return render(req, 'recharge.html')

#推荐有奖
def recommend(req):
    return render(req, 'recommend.html')

#账户余额
def records(req):
    return render(req, 'records.html')

#发布动态
def release(req):
    return render(req, 'release.html')

#商店
def speed(req):
    return render(req, 'speed.html')

#消息中心
def tidings(req):
    return render(req, 'tidings.html')

#选择校区
def village(req):
    return render(req, 'village.html')

#过期红包
def ygq(req):
    return render(req, 'ygq.html')

#可使用红包
def yhq(req):
    return render(req, 'yhq.html')

class Mybackend(ModelBackend):
    def authenticate(self, username=None, password=None,):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
