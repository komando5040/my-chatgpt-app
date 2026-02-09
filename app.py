"""
Entry point for Android build
"""
import sys
import os

# اضافه کردن مسیر جاری به sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import ChatGPTApp
    ChatGPTApp().run()
except Exception as e:
    print(f"Error starting app: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")
