# AI Assistant - اپلیکیشن چت هوش مصنوعی

یک اپلیکیشن ChatGPT-like ساده برای اندروید که با پایتون و Kivy ساخته شده است.

## ویژگی‌ها
- رابط کاربری شبیه به ChatGPT
- پاسخ به سوالات سلام و احوالپرسی
- پشتیبانی از فارسی و انگلیسی
- طراحی مدرن و تاریک
- ساخت آسان با GitHub Actions

## ساخت APK

### روش ۱: با GitHub Actions
1. این ریپوزیتوری را Fork کنید
2. به تب Actions بروید
3. workflow "Build APK" را اجرا کنید
4. APK از بخش Artifacts قابل دانلود است

### روش ۲: با Buildozer محلی
```bash
# نصب buildozer
pip install buildozer

# ساخت APK
buildozer android debug
