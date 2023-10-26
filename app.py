#  - * - coding:utf-8 - * -
"""
作者：LENOVO1
日期：2022年11月20日
"""
import datetime

from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

import config
from flask_last.apps.user.form import User_f, User_l, User_shops_a, Shop_shops_a

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Shopkeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    pwd = db.Column(db.String(20))

    def __repr__(self):
        return '<Shopkeeper %r>' % self.title


class Shop_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品
    commodity = db.Column(db.String(20))
    price = db.Column(db.String(20))
    time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Shop_shops %r>' % self.title


class User_shops(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品
    commodity = db.Column(db.String(20))
    price = db.Column(db.String(20))
    time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<User_shops %r>' % self.content


class User_a(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    sex = db.Column(db.String(5))
    age = db.Column(db.Integer)
    password = db.Column(db.String(50))

    def __repr__(self):
        return '<User_a %r>' % self.name


@app.route('/add', methods=['GET', 'POST'])
def add():
    shopkeeper1 = Shopkeeper(name='店主', pwd='123456')
    s1 = Shop_shops(commodity='坚果', price='36￥')
    db.session.add_all([shopkeeper1, s1])
    db.session.commit()

    return '数据添加成功！'


# 用户user增加
@app.route('/', methods=['GET', 'POST'])
def user_add():
    form1 = User_f()
    if form1.validate_on_submit():
        # 验证合格，获取表单中的用户信息
        name = form1.name.data
        sex = form1.sex.data
        age = form1.age.data
        pwd = form1.password.data
        # 创建User对象并赋值
        user = User_a()
        user.name = name
        user.sex = sex
        user.age = age
        user.password = pwd
        # 在数据库中添加与提交
        db.session.add(user)
        db.session.commit()
        return redirect('login')
    return render_template("register.html", form=form1)


# user登录
@app.route('/login', methods=['GET', 'POST'])
def home():
    form = User_l()
    username = form.name.data
    pwd = form.password.data
    print(username)
    if form.validate_on_submit():
        print(pwd)
        data = User_a.query.filter_by(name=username).all()
        s = 0
        c = 0
        for i in data:
            s = data[0].name
            c = data[0].password
        print(s, c)
        if username == s:
            if pwd == '123456':
                return redirect('message')
            elif pwd == c:
                return redirect('message1')
            else:
                return redirect('error')
    return render_template('login.html', form=form)


# 错误
@app.route('/error', methods=['GET', 'POST'])
def errors():
    return render_template('error.html')


# 展示shopkeeper数据
@app.route("/list", methods=['GET', 'POST'])
def List():
    users_list = User_shops.query.all()
    return render_template('show.html', users=users_list)


@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route("/fu", methods=['GET', 'POST'])
def fu():
    return '''<script type="text/javascript">alert('支付成功，耐心等待发货!');</script>'''


@app.route('/message1', methods=['GET', 'POST'])
def message1():
    news1 = User_shops_a()
    news_list1 = Shop_shops.query.all()
    print("dg")
    if news1.validate_on_submit():
        # 验证合格，获取表单中的用户信息
        commodity = news1.commodity.data
        price = news1.price.data
        # 创建User对象并赋值
        user_c = User_shops()
        user_c.commodity = commodity
        user_c.price = price
        print("v"+user_c.price)
        # 在数据库中添加与提交
        db.session.add(user_c)
        db.session.commit()
        return redirect('message1')
    return render_template('new_other.html', users1=news_list1, form=news1)


# 展示shopkeeper数据
@app.route('/message', methods=['GET', 'POST'])
def message():
    news = Shop_shops_a()
    news_list = Shop_shops.query.all()
    if news.validate_on_submit():
        # 验证合格，获取表单中的用户信息
        commodity = news.commodity.data
        price = news.price.data
        # 创建User对象并赋值
        user_c = Shop_shops()
        user_c.commodity = commodity
        user_c.price = price
        # 在数据库中添加与提交
        db.session.add(user_c)
        db.session.commit()
        return redirect('message')
    name = news.commodity.data
    print(name)
    if name:
        sd = Shop_shops.query.filter_by(commodity=name).delete()
        print(sd)
        db.session.commit()
        return redirect('message')
    return render_template('news_show.html', users=news_list, form=news)


with app.app_context():  # 手动创建上下文
    db.create_all()  # 在数据库中创建数据表---对象映射

if __name__ == '__main__':
    app.run(debug=True, port=9000)
