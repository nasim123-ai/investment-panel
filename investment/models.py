from django.db import models
class InvestmentProject(models.Model):

    province = models.CharField("نام استان", max_length=100, default="")
    city = models.CharField("نام شهر", max_length=100, default="")
    neighborhood_type = models.CharField("گونه محله", max_length=100, default="")
    title = models.CharField("نام پروژه", max_length=255)
    area = models.DecimalField("مساحت عرصه (متر مربع)", max_digits=12, decimal_places=2, default=0)
    land_use = models.CharField("نوع کاربری", max_length=100, default="")
    residential_units = models.IntegerField("تعداد واحد مسکونی", default=0)
    commercial_units = models.IntegerField("تعداد واحد تجاری", default=0)
    service_units = models.IntegerField("تعداد واحد خدماتی", default=0)
    investment_amount = models.DecimalField("برآورد حدودی حجم سرمایه‌گذاری (میلیون ریال)", max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.title