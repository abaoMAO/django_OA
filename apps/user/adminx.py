import xadmin
from xadmin import views
from .models import Department, UserProfile, Position
from xadmin.plugins.auth import UserAdmin

__author__ = 'weimin'
__date__ = '2018/3/10 0010 20:34'


# @xadmin.sites.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'department', 'position')
    search_fields = ('username', 'first_name', 'last_name', 'department', 'position')
    list_filter = ('username', 'first_name', 'last_name', 'department', 'position')


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSettings(object):
    site_title = "人事OA后台"
    site_footer = "奇维科技"
    menu_style = "accordion"


@xadmin.sites.register(Department)
class DepartmentAdmin(object):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    model_icon = 'fa fa-address-book-o'


@xadmin.sites.register(Position)
class PositionAdmin(object):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    model_icon = 'fa fa-address-book-o'

