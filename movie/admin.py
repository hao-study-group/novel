import xadmin
from movie import models


class BaseForms(object):
    pass

for i in models.__all__:
    xadmin.site.register(getattr(models, i), BaseForms)
