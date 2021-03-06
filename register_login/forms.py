#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from form import Form, forms
from django.core.validators import RegexValidator
from .config import ResetPwSendMailVcodeLength


# 注册
class RegisterForm(Form):
    email = forms.CharField(label='email',
                            min_length=4,
                            max_length=60,
                            validators=[
                                RegexValidator(
                                    r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                                    '【邮箱】格式错误'
                                )
                            ],
                            error_messages={
                                'required': '你没有填写【邮箱】',
                                'max_length': '【邮箱】长度需要在4~60位之间',
                                'min_length': '【邮箱】长度需要在4~60位之间'
                            }
                            )
    phone = forms.CharField(label='phone',
                            min_length=11,
                            max_length=11,
                            required=False,
                            error_messages={
                                'max_length': '【手机号码】长度需要11位',
                            }
                            )
    password = forms.CharField(label='password',
                               min_length=8,
                               max_length=40,
                               error_messages={
                                   'required': '你没有填写密码',
                                   'max_length': '密码长度需要在8~40位之间',
                                   'min_length': '密码长度需要在8~40位之间'
                               }
                               )


# 登录
class LoginForm(Form):
    email = forms.CharField(label='email',
                            min_length=4,
                            max_length=60,
                            validators=[
                                RegexValidator(
                                    r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                                    '【邮箱】格式错误'
                                )
                            ],
                            error_messages={
                                'required': '你没有填写【邮箱】',
                                'max_length': '【邮箱】长度需要在4~60位之间',
                                'min_length': '【邮箱】长度需要在4~60位之间'
                            }
                            )
    password = forms.CharField(label='password',
                               min_length=8,
                               max_length=40,
                               error_messages={
                                   'required': '你没有填写密码',
                                   'max_length': '密码长度需要在8~40位之间',
                                   'min_length': '密码长度需要在8~40位之间'
                               }
                               )


# 发送账号激活邮件（第2次）
class SendVerifyEmailForm(Form):
    email = forms.CharField(label='email',
                            min_length=4,
                            max_length=60,
                            validators=[
                                RegexValidator(
                                    r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                                    '【邮箱】格式错误'
                                )
                            ],
                            error_messages={
                                'required': '你没有填写【邮箱】',
                                'max_length': '【邮箱】长度需要在4~60位之间',
                                'min_length': '【邮箱】长度需要在4~60位之间'
                            }
                            )


# 发送密码重置邮件
class SendResetPasswordMailForm(SendVerifyEmailForm):
    pass


# 校验密码重置邮件的链接
class VerifyRPHrefForm(Form):
    email = forms.CharField(label='email',
                            min_length=4,
                            max_length=60,
                            validators=[
                                RegexValidator(
                                    r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$',
                                    '【邮箱】格式错误'
                                )
                            ],
                            error_messages={
                                'required': '你没有填写【邮箱】',
                                'max_length': '【邮箱】长度需要在4~60位之间',
                                'min_length': '【邮箱】长度需要在4~60位之间'
                            }
                            )
    vcode = forms.CharField(label='vcode',
                            min_length=ResetPwSendMailVcodeLength,
                            max_length=ResetPwSendMailVcodeLength,
                            error_messages={
                                'required': '你没有填写【验证码】',
                                'max_length': '【验证码】长度错误',
                                'min_length': '【验证码】长度错误'
                            }
                            )


# 校验密码重置的 request
class ResetPasswordForm(VerifyRPHrefForm):
    password = forms.CharField(label='password',
                               min_length=8,
                               max_length=40,
                               error_messages={
                                   'required': '你没有填写密码',
                                   'max_length': '密码长度需要在8~40位之间',
                                   'min_length': '密码长度需要在8~40位之间'
                               }
                               )
    rp_password = forms.CharField(label='rp_password',
                                  min_length=8,
                                  max_length=40,
                                  error_messages={
                                      'required': '你没有填写重复密码',
                                      'max_length': '密码长度需要在8~40位之间',
                                      'min_length': '密码长度需要在8~40位之间'
                                  }
                                  )
