

import xadmin
from .models import *

__author__ = 'weimin'
__date__ = '2018/3/3 0003 18:39'


class UserProfileAdmin(object):
    list_display = ('employee_name', 'mobile', 'position', 'section', 'superior')


class PositionAdmin(object):
    list_display = ('name', 'describe', 'level',)
    search_fields = ('name', 'describe', 'level',)
    list_filter = ('name', 'describe', 'level',)
    model_icon = 'fa fa-address-book-o'


class SectionAdmin(object):
    pass


# from django.contrib.auth.models import User
xadmin.site.unregister(UserProfile)

xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Position, PositionAdmin)
xadmin.site.register(Section, SectionAdmin)