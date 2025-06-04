import pandas as pd
import glob

#  تحديد مسار ملفات CSV
all_files = glob.glob(path + "/*.csv")

print(f" عدد ملفات CSV: {len(all_files)}")

#  قراءة ودمج الملفات في DataFrame واحد
list_df = []
for file in all_files:
    print(f" جاري قراءة: {file}")
    df = pd.read_csv(file)
    list_df.append(df)

merged_df = pd.concat(list_df, ignore_index=True)
print(f" تم الدمج! عدد الصفوف: {merged_df.shape[0]}")

#  تحويل الأعمدة إلى datetime بدون حذف أو تعديل القيم
date_cols = ['started_at', 'ended_at']

for col in date_cols:
    merged_df[col] = pd.to_datetime(merged_df[col], errors='coerce')  # القيم غير الصالحة تتحول لـ NaT

#  طباعة نوع البيانات للتأكد
print(" أنواع البيانات بعد التحويل:")
print(merged_df[date_cols].dtypes)

#  طباعة شكل البيانات النهائي
print(f"\n الشكل النهائي: {merged_df.shape}")



#  إنشاء أعمدة  من started_at
merged_df['hour'] = merged_df['started_at'].dt.hour
merged_df['month'] = merged_df['started_at'].dt.month_name()
merged_df['day_of_week'] = merged_df['started_at'].dt.day_name()
merged_df['quarter'] = merged_df['started_at'].dt.quarter.map({1: 'Q1', 2: 'Q2', 3: 'Q3', 4: 'Q4'})

#  تحديد فترات اليوم (صباح، بعد الظهر، مساء، ليل)
def get_day_period(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

merged_df['day_period'] = merged_df['hour'].apply(get_day_period)
merged_df.info()




