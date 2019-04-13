from django.db import models

__all__ = ['User', 'Userlog', 'Tag', 'Movie', 'Comment', 'Moviecol']


class User(models.Model):
    """
    会员
    """
    name = models.CharField(verbose_name="昵称", max_length=100)
    pwd = models.CharField(verbose_name="密码", max_length=100)
    email = models.CharField(verbose_name="邮箱", max_length=100, unique=True)
    phone = models.CharField(verbose_name="手机号码", max_length=11, unique=True)
    info = models.TextField(verbose_name="个性简介")
    face = models.ImageField(upload_to="static/movie/face/%Y/%m", null=True, blank=True, max_length=100,
                             verbose_name="个人头像")
    addtime = models.DateTimeField(verbose_name="注册时间", auto_now=True, db_index=True)
    uuid = models.UUIDField(verbose_name="唯一标识符", unique=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def check_pwd(self, pwd):
        """
        加密密码
        :param pwd: 密码
        :return: 加密完成的密码
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)

    class Meta:
        app_label = 'movie'
        verbose_name = '会员'
        db_table = 'user'
        verbose_name_plural = verbose_name


# 会员登录日志
class Userlog(models.Model):
    """
    会员登录日志
    """
    user = models.ForeignKey('User', on_delete=models.SET_NULL, verbose_name="会员外键", null=True, blank=True)
    ip = models.CharField(max_length=100, verbose_name="ip地址")
    addtime = models.DateTimeField(auto_now=True, verbose_name="登录时间")

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id

    class Meta:
        app_label = 'movie'
        verbose_name = '会员登录日志'
        db_table = 'Userlog'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    电影标签
    """
    name = models.CharField(max_length=100, verbose_name="标题", unique=True)
    addtime = models.DateTimeField(auto_now=True, verbose_name="添加时间", db_index=True)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'movie'
        verbose_name = '电影标签'
        db_table = 'Tag'
        verbose_name_plural = verbose_name


class Movie(models.Model):
    """
    电影
    """
    title = models.CharField(max_length=255, verbose_name="标题", unique=True)
    url = models.CharField(max_length=255, unique=True, verbose_name="url地址")
    info = models.TextField(verbose_name="简介")
    logo = models.ImageField(upload_to="static/movie/log/%Y/%m", null=True, blank=True, max_length=100,
                             verbose_name="电影封面")
    star = models.PositiveSmallIntegerField(verbose_name="星级")
    playnum = models.BigIntegerField(verbose_name="播放量")
    commentnum = models.BigIntegerField(verbose_name="评论量")
    area = models.CharField(max_length=255, verbose_name="上映地区")
    release_time = models.DateField(verbose_name='上映时间')
    length = models.CharField(max_length=100, verbose_name="播放时间")
    addtime = models.DateTimeField(auto_now=True, db_index=True, verbose_name="添加时间")
    tags = models.ManyToManyField('Tag', verbose_name="所属标签")

    def __repr__(self):
        return "<Movie %r>" % self.title

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'movie'
        verbose_name = '电影详情'
        db_table = 'Movie'
        verbose_name_plural = verbose_name


# # 上映预告
# class Preview(models.Model):
#     """
#     上映预告
#     """
#     title = models.CharField(max_length=255, verbose_name="标题", unique=True)
#     logo = models.CharField(max_length=255, unique=True, verbose_name="封面")
#     addtime = models.DateTimeField(db_index=True, auto_now=True)
#
#     def __repr__(self):
#         return self.title
#
#     class Meta:
#         app_label = 'movie'


# 评论
class Comment(models.Model):
    """
    评论
    """
    content = models.TextField(verbose_name="评论内容")
    addtime = models.DateTimeField(db_index=True, auto_now=True, verbose_name="添加时间")
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, verbose_name="所属电影", null=True, blank=True)
    user = models.ForeignKey("User", on_delete=True, verbose_name="所属用户")

    def __repr__(self):
        return self.content[:5] + '...'

    def __str__(self):
        return self.content[:5] + '...'

    class Meta:
        app_label = 'movie'
        verbose_name = '电影评论'
        db_table = 'Comment'
        verbose_name_plural = verbose_name


# 电影收藏
class Moviecol(models.Model):
    """
    电影收藏
    """
    movie = models.ForeignKey("Movie", on_delete=models.SET_NULL, verbose_name="关联电影", null=True, blank=True)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, verbose_name="关联用户", null=True, blank=True)
    addtime = models.DateTimeField(db_index=True, auto_now=True, verbose_name="添加时间")

    def __repr__(self):
        return "<Moviecol %r>" % self.id

    def __str__(self):
        return self.id

    class Meta:
        app_label = 'movie'
        verbose_name = '电影收藏'
        db_table = 'Moviecol'
        verbose_name_plural = verbose_name


