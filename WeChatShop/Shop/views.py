#-*- coding:utf-8 -*-
from django.shortcuts import render
from Shop.models import goods

# Create your views here.
#首页
def index(request):
    goods_list = goods.objects.all()
    return render(request, 'index.html', {'goods_list' : goods_list})

#我的
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

#登录
def login(req):
    return render(req, 'login.html')

#购物车
def shopcart(req):
    return render(req, 'shopcart.html')

#所有订单
def allorder(req):
    return render(req, 'allorder.html')

#动态
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
def detail(req):
    return render(req, 'detail.html')

#忘记密码
def forgetpassword(req):
    return render(req, 'forgetpassword.html')

#收货地址
def gladdress(req):
    return render(req, 'gladdress.html')

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

#确认订单
def order(req):
    return render(req, 'order.html')

#订单详情
def orderdetail(req):
    return render(req, 'orderdetail.html')

#密码
def password(req):
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

#注册
def reg(req):
    return render(req, 'reg.html')

#发布动态
def release(req):
    return render(req, 'release.html')

#商店
def speed(req):
    return render(req, 'speed.html')

#消息中心
def tidings(req):
    return render(req, 'tidings.html')

#确认订单
def tureorder(req):
    return render(req, 'tureorder.html')

#选择校区
def village(req):
    return render(req, 'village.html')

#过期红包
def ygq(req):
    return render(req, 'ygq.html')

#可使用红包
def yhq(req):
    return render(req, 'yhq.html')