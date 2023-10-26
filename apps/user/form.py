#  - * - coding:utf-8 - * -
"""
作者：LENOVO1
日期：2022年11月20日
"""

from flask import Flask
from wtforms import SubmitField, StringField, PasswordField, RadioField
from wtforms.fields import simple
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class User_f(FlaskForm):
    name = StringField('用户名称：', validators=[DataRequired('用户名不能为空')],
                       render_kw={"placeholder": "输入用户名"})
    sex = RadioField('性别', choices=['男', '女'], validators=[DataRequired('商品名不能为空')])
    age = StringField('年龄：', validators=[DataRequired()],
                      render_kw={"placeholder": "输入年龄"})
    passwords = PasswordField('用户密码：', validators=[DataRequired('商品名不能为空')],
                              render_kw={"placeholder": "输入密码"})
    password = PasswordField('确认密码：', validators=[DataRequired('商品名不能为空')],
                             render_kw={"placeholder": "再次输入密码"})
    submit = SubmitField(
        '注册'
    )


class User_l(FlaskForm):
    name = StringField('用户名称：', validators=[DataRequired('用户名不能为空')],
                       render_kw={"placeholder": "输入用户名"})
    password = PasswordField('输入密码：', validators=[DataRequired('商品名不能为空')],
                             render_kw={"placeholder": "再次输入密码"})
    submit = SubmitField(
        '登录'
    )


class Shopkeeper_a(FlaskForm):
    username = StringField('用户名称：', validators=[DataRequired('用户名不能为空')],
                           render_kw={"placeholder": "输入用户名"})
    password = PasswordField('用户密码：', validators=[DataRequired('密码不能为空')],
                             render_kw={"placeholder": "输入密码"})
    submit = SubmitField(
        '登录'
    )


class Shop_shops_a(FlaskForm):
    commodity = StringField('商品名称', validators=[DataRequired('商品名不能为空')],
                            render_kw={"placeholder": "输入商品名"})
    price = StringField('价格', validators=[DataRequired('价格不能为空')],
                        render_kw={"placeholder": "输入价格"})
    submit = SubmitField(
        '增加'
    )
    submit1 = SubmitField(
        '删除'
    )


class User_shops_a(FlaskForm):
    commodity = StringField('商品名称', validators=[DataRequired('商品名不能为空')],
                            render_kw={"placeholder": "输入商品名"})
    price = StringField('价格', validators=[DataRequired('价格不能为空')],
                        render_kw={"placeholder": "输入价格"})
    submits = SubmitField(
        '加入购物清单'
    )


app = Flask(import_name=__name__,
            static_folder='static', template_folder='templates')
