__author__ = 'weimin'
__date__ = '2018/3/3 0003 18:39'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

from django.utils.translation import ugettext as _

from .models import *


class PositionAdmin(object):
    list_display = ('name', 'describe', )
    search_fields = ('name', 'describe', )
    list_filter = ('name', 'describe', )
    # model_icon = 'fa fa-address-book-o'


class SectionAdmin(object):
    pass


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "观正会计师事务所"
    site_footer = "奇维科技"
    menu_style = "accordion"


# from django.contrib.auth.models import Userd
# xadmin.site.unregister(UserProfile)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(Position, PositionAdmin)
xadmin.site.register(Section, SectionAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)