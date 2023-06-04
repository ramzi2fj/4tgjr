import telebot
import re
from telebot import apihelper, util, types
# Replace YOUR_TOKEN_HERE with your actual token
bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"""
<b> سلام {first_name} عزیز به لیچر « بیاتوکره » خوش آمدید</b>
                                     
با ارسال دستور /help راهنما ربات را مشاهده فرمایید 
""", parse_mode="HTML")

@bot.message_handler(commands=['help'])
def send_help(message):
    first_name = message.from_user.first_name
    bot.reply_to(message, f"""
<b>راهنما:</b>
برای لیچ کردن میتوانید لینک های خود را به صورت تکی و گروهی برای ربات ارسال کنید. 



جهت ارتباط با ادمین ربات @admin را تایپ کنید و پیام خود را بنویسید.  

""", parse_mode="HTML") 


@bot.message_handler(func=lambda message: '@admin' in message.text)
def send_to_admin(message):
    # Get the username of the sender
    sender_username = message.chat.username
    
    # Construct the message to be sent to admin
    admin_message = f"پیام جدید از طرف کاربر  @{sender_username}:\n{message.text}"
    
    # Send the message to admin
    bot.send_message(642558901, admin_message)


def restricted_access(func):
    def wrapper(message):
        if message.from_user.id != 642558901:
            bot.reply_to(message, "*شما مجوز دسترسی به این دستور را ندارید!*", parse_mode="Markdown")
            return
        return func(message)
    return wrapper

@bot.message_handler(commands=['users'])
@restricted_access
def get_users_count(message):
    users = bot.get_chat_member_count(message.chat.id)
    bot.reply_to(message, f"* تعداد کاربران ربات : {users}*", parse_mode="Markdown")









@bot.message_handler(func=lambda message: True, content_types=['text'])
def replace_links(message):
    # Regular expression to match the link pattern
    regex = r"https://b2kupdl\.ir/download\.php\?url=dl/(s\d+)/"

    # Check if there is a link in the message text
    match = re.search(regex, message.text)

    # If there is a match, replace the link and send it back to the user
    if match:
        fr_number = match.group(1)
        new_link = f"http://{fr_number}.b2kupdl.ir/"
        replaced_message = message.text.replace(match.group(), new_link)
        bot.reply_to(message, f"{replaced_message}")
        bot.reply_to(message," عملیات با موفقیت انجام شد *:)*", parse_mode="Markdown")
bot.polling()













