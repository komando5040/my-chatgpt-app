[app]

# نام اپلیکیشن
title = AI Assistant

# نام پکیج
package.name = aichat

# دامنه پکیج
package.domain = org.aichat

# پوشه کد منبع
source.dir = .

# فایل اصلی
source.main = app.py

# نسخه اپلیکیشن
version = 1.0.0

# نیازمندی‌ها
requirements = python3==3.10.9,kivy==2.3.0,python-bidi==0.4.2,arabic-reshaper==3.0.0,android,plyer

# جهت صفحه
orientation = portrait

# تمام صفحه
fullscreen = 0

# API اندروید
android.api = 34
android.minapi = 21

# معماری‌ها
android.archs = arm64-v8a, armeabi-v7a

# مجوزها
android.permissions = INTERNET

# امکان بک‌آپ
android.allow_backup = True

# لودینگ اولیه
# presplash.filename = %(source.dir)s/assets/icon.png

# آیکون
# icon.filename = %(source.dir)s/assets/icon.png

# فرمت خروجی
android.debug_artifact = apk

# لوگ‌گیری
log_level = 2

[buildozer]
# مسیر ساخت
build_dir = ./.buildozer
bin_dir = ./bin
