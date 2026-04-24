from django.db import models
from django.utils import timezone

# 1. 日々の配布枚数を記録する箱
class StickerRecord(models.Model):
    date = models.DateField(default=timezone.now, verbose_name="日付")
    count = models.PositiveIntegerField(verbose_name="配布枚数")
    cast_name = models.CharField(max_length=50, blank=True, verbose_name="キャスト名")

    def __str__(self):
        return f"{self.date}：{self.cast_name or '匿名'} {self.count}枚"

# 2. 目標枚数を設定する箱
class GoalSetting(models.Model):
    target_count = models.PositiveIntegerField(default=3000, verbose_name="今月の目標枚数")
    
    class Meta:
        verbose_name = "目標設定"

    def __str__(self):
        return f"現在の目標：{self.target_count}枚"