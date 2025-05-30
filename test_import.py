import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investment_site.settings')
django.setup()

from panel.models import InvestmentProject

df = pd.read_excel('projects.xlsx')

# حذف فاصله‌های اضافی از اسم ستون‌ها:
df.columns = df.columns.str.strip()

df["مساحت عرصه(متر مربع)"] = df["مساحت عرصه(متر مربع)"].fillna(0)
df["برآورد حدودی حجم سرمایه گذاری (میلیون ریال)"] = df["برآورد حدودی حجم سرمایه گذاری (میلیون ریال)"].fillna(0)

# حالا می‌تونی با خیال راحت از نام‌های درست استفاده کنی
for index, row in df.iterrows():
    project = InvestmentProject(
        province=row["نام استان"],
        city=row["نام شهر"],
        neighborhood_type=row["گونه محله"],
        title=row["نام پروژه"],
        area=row["مساحت عرصه(متر مربع)"],
        land_use=row["نوع کاربری"],
        residential_units=row["تعداد واحد مسکونی"],
        commercial_units=row["تعداد واحد تجاری"],
        service_units=row["تعداد واحد خدماتی"],
        investment_amount=row["برآورد حدودی حجم سرمایه گذاری (میلیون ریال)"],
)
project.save()

print("✅ تمام داده‌ها با موفقیت ذخیره شدند.")