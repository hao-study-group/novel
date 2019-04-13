from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class DatabaseAppsRouter():
    """
    一种路由器，用于控制身份验证应用程序中模型上的所有数据库操作。
    """

    def db_for_read(self, model, **hints):
        """
       尝试读取身份验证模型转到身份验证数据库。
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """
        尝试写入身份验证模型转到身份验证数据库。
        """
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        如果涉及auth应用程序中的模型，则允许关系。
        """
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 == db_obj2:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        确保auth应用程序只出现在'auth_db'数据库中。
        """
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None
