import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investment_site.settings')
django.setup()

from panel.models import InvestmentProject

file_path = 'projects.xlsx'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip() # ← ستون‌ها رو پاک‌سازی می‌کنیم از فاصله اضافی

count = 0
for index, row in df.iterrows():
    title = row.get('نام پروژه')
    if pd.isna(title) or title in ['0', 0, '']:
        continue
    InvestmentProject.objects.create(
        title=str(title).strip(),
        province=row.get('نام استان', ''),
        city=row.get('نام شهر', ''),
        neighborhood_type=row.get('گونه محله', ''),
        area=row.get('مساحت عرصه (متر مربع)', 0) or 0,
        land_use=row.get('نوع کاربری', ''),
        residential_units=row.get('تعداد واحد مسکونی', 0) or 0,
        commercial_units=row.get('تعداد واحد تجاری', 0) or 0,
        service_units=row.get('تعداد واحد خدماتی', 0) or 0,
        investment_amount=row.get('برآورد حدودی حجم سرمایه گذاری (میلیون ریال)', 0) or 0

    )
    count += 1

print(f"✅ تعداد {count} پروژه با موفقیت وارد شد.")