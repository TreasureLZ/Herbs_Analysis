from django.db import models


# Create your models here.
class Prescript(models.Model):
    uid = models.CharField(verbose_name="药方id", max_length=255, null=True, blank=True)
    name = models.CharField(verbose_name="药方名", max_length=255, null=True, blank=True)
    recipe = models.CharField(verbose_name="药方配方", max_length=255, null=True, blank=True)
    dosage = models.CharField(verbose_name="使用方式", max_length=255, null=True, blank=True)
    excerpt = models.CharField(verbose_name="出处", max_length=255, null=True, blank=True)
    indications = models.CharField(verbose_name="功效", max_length=255, null=True, blank=True)
    note = models.CharField(verbose_name="注意事项", max_length=255, null=True, blank=True)
    processing = models.CharField(verbose_name="加工方式", max_length=255, null=True, blank=True)
    tcmName = models.CharField(verbose_name="中药名称", max_length=255, null=True, blank=True)
    recipe_pz = models.TextField(verbose_name="药方配料", null=True, blank=True)
    class Meta:
        verbose_name = "药方信息"
        verbose_name_plural = "药方信息"
        db_table = "prescript"


class OriginPrice(models.Model):
    keyword = models.CharField(verbose_name="药材", max_length=255, null=True, blank=True)
    origin = models.CharField(verbose_name="产地", max_length=255, null=True, blank=True)
    price = models.CharField(verbose_name="价格", max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "产地价格"
        verbose_name_plural = "产地价格"
        db_table = "originprice"

class HistoryPrice(models.Model):
    keyword = models.CharField(verbose_name="药材", max_length=255, null=True, blank=True)
    updateTime = models.CharField(verbose_name="日期", max_length=255, null=True, blank=True)
    price = models.CharField(verbose_name="价格", max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "历史价格"
        verbose_name_plural = "历史价格"
        db_table = "historyprice"

class OriginStatistics(models.Model):
    keyword = models.CharField(verbose_name="药材", max_length=255, null=True, blank=True)
    origin = models.CharField(verbose_name="产地", max_length=255, null=True, blank=True)
    count = models.CharField(verbose_name="出现次数", max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "供应产地"
        verbose_name_plural = "供应产地"
        db_table = "originstatistics"

class Info(models.Model):
    keyword = models.CharField(verbose_name="药材", max_length=255, null=True, blank=True)
    title = models.CharField(verbose_name="标题", max_length=255, null=True, blank=True)
    content = models.CharField(verbose_name="内容", max_length=255, null=True, blank=True)
    class Meta:
        verbose_name = "市场资讯"
        verbose_name_plural = "市场资讯"
        db_table = "info"
