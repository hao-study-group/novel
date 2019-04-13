from django.db import models
from datetime import datetime

__all__ = ['Channel', 'TagModel', 'Tage', 'NovelModel', 'NovelChaPter', 'NovelCol']


class Channel(models.Model):
    """小说频道"""
    channel_name = models.CharField(max_length=20, default="", verbose_name="小说的频道")

    class Meta:
        verbose_name = "频道管理"
        verbose_name_plural = verbose_name
        db_table = "Channel"
        app_label = 'novel'

    def __str__(self):
        return self.channel_name

    '''获取小说的所有类别'''

    def get_tag(self):
        return self.tagmodel_set.all().order_by("id")[:12]


class TagModel(models.Model):
    '''小说的类别'''
    tag_id = models.ForeignKey(Channel, verbose_name="小说的频道", on_delete=models.SET_NULL, null=True, blank=True)
    tag_name = models.CharField(max_length=20, verbose_name="小说的类别")

    class Meta:
        verbose_name = "类别管理"
        verbose_name_plural = verbose_name
        db_table = "TagModel"
        app_label = 'novel'

    def __str__(self):
        return self.tag_name


class Tage(models.Model):
    '''小说的标签管理'''
    tag_name = models.CharField(max_length=20, verbose_name="标签名称")

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "添加标签"
        verbose_name_plural = verbose_name
        db_table = "Tage"
        app_label = 'novel'


class NovelModel(models.Model):
    """
    小说信息
    """
    novel_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="小说的名称")
    novel_image = models.ImageField(upload_to="static/novel/", null=True, blank=True, max_length=100,
                                    verbose_name="小说的封面图")
    novel_user = models.CharField(max_length=30, null=True, blank=True, verbose_name="小说的作者", default="佚名")
    novel_byte = models.IntegerField(default=0, verbose_name="字节数")
    novel_read = models.IntegerField(default=0, verbose_name="阅读量")
    novel_comment = models.IntegerField(default=0, verbose_name="评论量")
    novel_tag = models.ForeignKey(TagModel, null=True, blank=True, verbose_name="小说的类别", on_delete=models.SET_NULL)
    novel_text = models.TextField(max_length=200, null=True, blank=True, verbose_name="小说的简介")
    novel_fave = models.IntegerField(default=0, verbose_name="小说的收藏数")
    novel_next = models.IntegerField(default=0, verbose_name="浏览量")
    novel_time = models.DateTimeField(default=datetime.now, verbose_name="小说更新时间")

    class Meta:
        verbose_name = "小说管理"
        verbose_name_plural = verbose_name
        db_table = "NovelModel"
        app_label = 'novel'

    def __str__(self):
        return self.novel_name

    '''获取小说的章节'''

    def get_book(self):
        return self.novelchapter_set.all()

    '''获取小说最新的章节'''

    def get_time_book(self):
        return self.novelchapter_set.all().order_by("-id")[:1]

    '''获取小说第一章节'''

    def get_book_to(self):
        return self.novelchapter_set.all().order_by("id")[:1]


class NovelChaPter(models.Model):
    '''小说的章节信息'''
    novelchapter_cover = models.ForeignKey(NovelModel, verbose_name="所属小说", on_delete=models.CASCADE)
    novelchapter_name = models.CharField(max_length=30, verbose_name="章节名称")
    novelchapter_text = models.TextField(verbose_name='章节内容')
    novelchapter_num = models.IntegerField(default=0, verbose_name="章节数")
    novelchapter_time = models.DateTimeField(default=datetime.now, verbose_name="章节更新时间")

    class Meta:
        verbose_name = "章节管理"
        verbose_name_plural = verbose_name
        db_table = "NovelChaPter"
        app_label = 'novel'

    def __str__(self):
        return self.novelchapter_name


class NovelCol(models.Model):
    """
    收藏小说
    """
    novel = models.ForeignKey("NovelModel", on_delete=models.SET_NULL, verbose_name="关联小说", null=True, blank=True)
    user = models.IntegerField(verbose_name='关联用户的ID')
    addtime = models.DateTimeField(db_index=True, auto_now=True, verbose_name="添加时间")

    def __repr__(self):
        return self.novel

    def __str__(self):
        return self.novel.__str__()

    class Meta:
        verbose_name = "收藏小说"
        verbose_name_plural = verbose_name
        db_table = "NovelCol"
        app_label = 'novel'
