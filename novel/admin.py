import xadmin
from novel import models
from xadmin import views


class BaseForms(object):
    pass


for i in models.__all__:
    xadmin.site.register(getattr(models, i), BaseForms)
from xadmin import views


class GlobalSetting(object):
    site_title = "后台管理系统"
    site_footer = "http://www.haoqihan.top/"


xadmin.site.register(views.CommAdminView, GlobalSetting)
