import pandas as pd

from panel.models import InvestmentProject  # وارد کردن مدل از اپلیکیشن panel


# خواندن فایل اکسل

df = pd.read_excel('projects.xlsx')


for index, row in df.iterrows():

    project = InvestmentProject(

        province=row["نام استان"],

        city=row["نام شهر"],

        neighborhood_type=row["گونه محله"],

        title=row["نام پروژه"],

        area=row["مساحت عرصه (متر مربع)"],

        land_use=row["نوع کاربری"],

        residential_units=row["تعداد واحد مسکونی"],

        commercial_units=row["تعداد واحد تجاری"],

        service_units=row["تعداد واحد خدماتی"],

        investment_amount=row["برآورد حدودی حجم سرمایه‌گذاری (میلیون ریال)"],

    )

    project.save()


print("تمام داده‌ها با موفقیت ذخیره شدند.")