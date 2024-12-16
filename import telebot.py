import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# إعداد البوت باستخدام التوكن الخاص بك
BOT_TOKEN = "7547663858:AAGOC_rmsGMb2gNT-wnC9qa_F5NBXH3iyUc"
bot = telebot.TeleBot(BOT_TOKEN)

# رابط صفحة MiniApp
MINIAPP_URL = "https://saad2451.github.io/houseTap/"  # استبدل بالرابط الفعلي

# دالة بدء البوت
@bot.message_handler(commands=["start"])
def start_message(message):
    user_id = message.chat.id

    # إنشاء لوحة الأزرار
    markup = InlineKeyboardMarkup()
    # زر PLAY يفتح واجهة MiniApp
    markup.add(InlineKeyboardButton("🎮 PLAY", web_app=WebAppInfo(url=MINIAPP_URL)))
    # زر My Balance
    markup.add(InlineKeyboardButton("💰 My Balance", callback_data="balance"))
    
    bot.send_message(user_id, "Welcome to the Mining Bot! Choose an option below:", reply_markup=markup)

# معالجة الأزرار الأخرى
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    user_id = call.message.chat.id
    if call.data == "balance":
        # هنا يمكن إضافة كود لمعالجة الرصيد
        bot.answer_callback_query(call.id, "Your balance: 0.00 coins 💰")

# تشغيل البوت
bot.polling()
