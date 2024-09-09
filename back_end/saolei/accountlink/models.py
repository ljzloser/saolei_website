# -*- coding: utf-8 -*-
from django.db import models
from userprofile.models import UserProfile

# 用于验证的队列
class AccountLinkQueue(models.Model):
    platform = models.CharField(max_length=1)
    identifier = models.BigIntegerField()
    userprofile = models.ForeignKey(UserProfile)
    verified = models.BooleanField(default=False)

# 网站编码 website code
# a - Authoritative Minesweeper
# c - China ranking (saolei.wang)
# g - Minesweeper GO
# l - League of Minesweeper
# s - Scoreganizer
# w - World of Minesweeper
# B - Bilibili
# D - Discord
# F - Facebook
# G - GitHub
# R - Reddit
# S - Speedrun.com
# T - Tieba
# W - Weibo
# X - X
# Y - YouTube
# Z - Zhihu