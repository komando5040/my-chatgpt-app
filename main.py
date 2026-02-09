from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class TestApp(App):
    def build(self):
        Window.size = (360, 640)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        label = Label(
            text='AI Assistant v1.0\n\nHello from Kivy!',
            font_size='24sp',
            halign='center'
        )
        label.bind(size=label.setter('text_size'))
        
        button = Button(
            text='Click Me!',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        button.bind(on_press=self.on_button_click)
        
        self.message_label = Label(
            text='',
            font_size='18sp'
        )
        
        layout.add_widget(label)
        layout.add_widget(button)
        layout.add_widget(self.message_label)
        
        return layout
    
    def on_button_click(self, instance):
        messages = [
            "Hello! 👋",
            "AI Assistant is working!",
            "Build successful!",
            "Kivy app is running!"
        ]
        import random
        self.message_label.text = random.choice(messages)

if __name__ == '__main__':
    TestApp().run()        self.chat_layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=[10, 10],
            size_hint_y=None
        )
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        
        self.chat_scroll.add_widget(self.chat_layout)
        main_layout.add_widget(self.chat_scroll)
        
        # بخش ورودی
        input_layout = BoxLayout(
            size_hint_y=0.1,
            orientation='horizontal',
            spacing=10,
            padding=[10, 10]
        )
        
        self.input_field = TextInput(
            hint_text='پیام خود را بنویسید...',
            multiline=True,
            size_hint_x=0.8,
            background_color=COLORS['bg_light'],
            foreground_color=COLORS['text_white'],
            cursor_color=COLORS['text_white'],
            hint_text_color=[0.7, 0.7, 0.7, 1]
        )
        self.input_field.bind(on_text_validate=self.send_message)
        
        send_btn = Button(
            text='ارسال',
            size_hint_x=0.2,
            background_color=self.hex_to_rgb(COLORS['primary']),
            color=COLORS['text_white']
        )
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.input_field)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)
        
        # نمایش پیام خوش‌آمدگویی
        Clock.schedule_once(lambda dt: self.show_welcome(), 0.5)
        
        return main_layout
    
    def update_rect(self, instance, value):
        """بروزرسانی مستطیل پس‌زمینه"""
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
    
    def hex_to_rgb(self, hex_color):
        """تبدیل رنگ HEX به RGB"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4)) + (1,)
    
    def load_responses(self):
        """بارگذاری پاسخ‌های از پیش تعریف شده"""
        responses = {
            # سلام و احوالپرسی
            'سلام': [
                'سلام! چطور می‌تونم کمکتون کنم؟',
                'درود! خوب هستید؟',
                'سلام! خوش آمدید. 😊'
            ],
            'درود': [
                'درود بر شما! چه کمکی می‌تونم بکنم؟',
                'سلام! چطور می‌تونم خدمتتون باشم؟'
            ],
            'hello': [
                'Hello! How can I assist you today?',
                'Hi there! What can I do for you?'
            ],
            'hi': [
                'Hi! How are you doing?',
                'Hello! Nice to meet you!'
            ],
            
            # احوالپرسی
            'حالت چطوره': [
                'من خوبم ممنون! امیدوارم شما هم خوب باشید.',
                'عالی هستم، مرسی! شما چطورید؟'
            ],
            'چطوري': [
                'خوبم، ممنون! 😊',
                'عالی! امیدوارم شما هم همینطور باشید.'
            ],
            'how are you': [
                'I\'m doing great, thank you! How about you?',
                'I\'m fine, thanks for asking!'
            ],
            
            # تشکر
            'ممنون': [
                'خواهش می‌کنم! 😊',
                'خوشحالم که می‌تونم کمک کنم.',
                'کاری نکردم! اگر سوال دیگه‌ای دارید بپرسید.'
            ],
            'مرسي': [
                'قربونت! 😄',
                'خواهش می‌کنم!'
            ],
            'thanks': [
                'You\'re welcome!',
                'Happy to help!'
            ],
            'thank you': [
                'My pleasure!',
                'Anytime! 😊'
            ],
            
            # خداحافظی
            'خداحافظ': [
                'خداحافظ! موفق باشید.',
                'به امید دیدار! 😊',
                'خدانگهدار!'
            ],
            'باي': [
                'بای بای! 👋',
                'خداحافظ!'
            ],
            'goodbye': [
                'Goodbye! Have a nice day!',
                'See you later! 👋'
            ],
            'bye': [
                'Bye! Take care!',
                'See you! 😊'
            ],
            
            # سوالات متداول
            'اسمت چيه': [
                'من یک دستیار هوش مصنوعی هستم!',
                'من AI Assistant هستم، در خدمت شما!'
            ],
            'كی هستی': [
                'من یک دستیار مجازی هستم که با پایتون و Kivy ساخته شده‌ام.',
                'من AI Assistant هستم که برای کمک به شما طراحی شده‌ام.'
            ],
            'چه کارهايی میتونی انجام بدی': [
                'می‌تونم به سوالاتتون پاسخ بدم، با شما گپ بزنم و اطلاعات مفید ارائه بدم.',
                'من می‌تونم در زمینه‌های مختلف کمکتون کنم و به سوالاتتون پاسخ بدم.'
            ],
            
            # سوالات انگلیسی
            'what is your name': [
                'I\'m AI Assistant, created with Python and Kivy!',
                'You can call me AI Assistant!'
            ],
            'who are you': [
                'I\'m an AI assistant designed to help you with various tasks.',
                'I\'m your virtual assistant, ready to help!'
            ],
            'what can you do': [
                'I can answer your questions, chat with you, and provide useful information.',
                'I\'m here to assist you with various tasks and answer your queries.'
            ],
        }
        return responses
    
    def get_response(self, message):
        """دریافت پاسخ مناسب برای پیام کاربر"""
        message_lower = message.strip().lower()
        
        # جستجوی دقیق در کلیدها
        for key in self.responses:
            if key in message_lower:
                return random.choice(self.responses[key])
        
        # اگر کلمه کلیدی خاصی پیدا نشد
        default_responses = [
            'متاسفانه سوال شما رو کامل متوجه نشدم. می‌تونید سوالتون رو واضح‌تر بپرسید؟',
            'لطفاً سوال خود را به شکل دیگری بیان کنید.',
            'من هنوز در حال یادگیری هستم! سوالات ساده‌تر رو بهتر متوجه می‌شم.',
            'I\'m not sure I understand. Could you rephrase your question?',
            'Could you please ask in a different way?',
            'I\'m still learning! I understand simpler questions better.'
        ]
        
        # بررسی زبان پیام
        persian_chars = set('ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی')
        if any(char in persian_chars for char in message_lower):
            return 'متوجه سوال شما شدم اما پاسخی برای آن ندارم. می‌توانید سوال دیگری بپرسید؟'
        else:
            return 'I understand your question but don\'t have a specific answer. Could you ask something else?'
    
    def send_message(self, instance):
        """ارسال پیام کاربر و دریافت پاسخ"""
        user_message = self.input_field.text.strip()
        
        if not user_message:
            return
        
        # اضافه کردن پیام کاربر به چت
        self.add_message_to_chat(user_message, 'user')
        
        # پاک کردن فیلد ورودی
        self.input_field.text = ''
        
        # شبیه‌سازی تایپ AI
        Clock.schedule_once(lambda dt: self.generate_ai_response(user_message), 0.5)
    
    def generate_ai_response(self, user_message):
        """تولید پاسخ AI"""
        response = self.get_response(user_message)
        
        # اضافه کردن پاسخ AI به چت
        self.add_message_to_chat(response, 'ai')
        
        # ذخیره در تاریخچه چت
        self.chat_history.append({
            'user': user_message,
            'ai': response,
            'time': datetime.now().strftime('%H:%M')
        })
    
    def add_message_to_chat(self, message, sender):
        """افزودن پیام به رابط کاربری چت"""
        msg_widget = ChatMessage(
            message=message,
            sender=sender,
            size_hint_y=None
        )
        
        self.chat_layout.add_widget(msg_widget)
        
        # اسکرول به پایین
        Clock.schedule_once(lambda dt: self.scroll_to_bottom(), 0.1)
    
    def scroll_to_bottom(self):
        """اسکرول به آخرین پیام"""
        if self.chat_layout.height > self.chat_scroll.height:
            self.chat_scroll.scroll_y = 0
    
    def show_welcome(self):
        """نمایش پیام خوش‌آمدگویی"""
        welcome_messages = [
            "سلام! من AI Assistant هستم. 😊",
            "خوش آمدید! چطور می‌تونم کمکتون کنم؟",
            "برای شروع، می‌تونید به من سلام کنید یا سوالتون رو بپرسید."
        ]
        
        self.add_message_to_chat(random.choice(welcome_messages), 'ai')
    
    def clear_chat(self, instance):
        """پاک کردن تاریخچه چت"""
        self.chat_layout.clear_widgets()
        self.chat_history = []
        self.show_welcome()


if __name__ == '__main__':
    ChatGPTApp().run()
