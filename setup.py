import os
import telebot

bot = telebot.TeleBot("")

admin = 
users = []

@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.reply_to(message, """
	
	🤖සාදරයෙන් පිළිගන්නවා RS SOFTWARES BOT වෙත💚
	
	❯❯මෙම බොට්ගෙන් ඔබට අපගේ නවතම මෘදුකාංග හා welcome message, warn to user වැනි සේවා ලබාගත හැක.විස්තර සදහා owner ගෙන් විමසන්න.❮❮
	
	commands සදහා /menu ලෙස එවන්න...
	
	🤖Owner : Ranuja Sanmira
	🦾Copyright ©2021 RS45 Crew
	
	
ඉතින් කොහොමද """ + message.from_user.first_name + "?")

@bot.message_handler(commands=["how"])
def send_message(message):
	bot.reply_to(message, "**Visit our official youtube channel.**")
	
@bot.message_handler(commands=["menu"])
def send_message(message):
	bot.reply_to(message, """
	
	🌹Welcome⃝✥to⃟☺😮RS⃝৫⃟➤Software  Bot᭄᭄̊̊̊̊Stable Version࿓࿔️᭄ꦿ
	
	🔰/start :
		💬මෙම බොට්ව start කිරීමට භාවිතා කරන්න.
	🔰/menu :
		💬මෙම කමාඩ් ලිස්ට් එක ලබා ගැනීමට.
	🔰/info :
		💬බොට්ගෙ විස්තර බැලීමට.
	🔰/dwn :
		💬අපගේ මෘදුකාංග සහ ඇප්ස් github සහ blog එකෙන් ලබාගැනීමට.
	🔰/adminf :
		💬ඇඩ්මින්ගෙ විස්තර ගැනීමට.
	🔰/mngrpinf :
		💬අපගෙ නිල ටෙලිග්‍රෑම් සමූහයට සම්බන්ධ වීමට.
	🔰/ytlink :
		💬අපගේ නිල youtube නාලිකාව ලබාගන්න.කරුණාකර subscribe කරන්න.
	🔰/whatsapp :
		💬ඇඩ්මින් හට බාධා වන බැවින් මෙම පහසුකම ඉවත් කර ඇත!
	
	
	""")
	
@bot.message_handler(commands=["info"])
def send_message(message):
	bot.reply_to(message, """
	
	🔛Bot Information😐
	
	🤖Name : RS SOFTWARES BOT
	🌀Version : Stable(V4.0)
	💁‍♀️Owner : Ranuja Sanmira
	🛣User Name : @soft_by_rs_bot
	🛠Last Modify : 2021/10/23 at 7.25 PM
	🌏Hosted on : █████████.com
	
	
	වැඩි විස්තර ඇඩ්මින්ගෙන් ලබාගන්න...
	
	""")
	
@bot.message_handler(commands=["dwn"])
def send_message(message):
	bot.reply_to(message, """
	
	🌀Github
	┕https://github.com/ranujas
	🌀Blog
	┕https://rs45softwaresofficial.blogspot.com
	═════════════════════════
	🌀Youtube
	┕https://www.youtube.com/channel/UCft0sPPD2LqJZlZzKNCvJzA?sub_confirmation=1
	🌀Telegram
	┕https://t.me/qPfItjLihPhkYzll
	
	
	
	""")

@bot.message_handler(commands=["adminf"])
def send_message(message):
	bot.reply_to(message, """
	
	මෙම බොට්වරයා නිර්මාණය කරන ලද්දෙ රනුජ සන්මිර වන මන් විසිනි. මම තවමත් පාසල් ශිෂ්‍යයෙක් බව කරුනාවෙන් සලකන්න. ඔබට මා ටෙලිග්‍රෑම් හරහා සම්බන්ධ කර ගැනීමට හැක. ඒ සදහා අපගේ නිල ටෙලිග්‍රෑම් සමූහයට එක් වී එහි owner වන මා හට පණිවිඩය යොමු කරන්න. සමූහයේ ලින්ක් එක ගැනීමට /mngrpinf ලෙස එවන්න. මෙම බොට්ව භාවිතා කිරීමට ස්තූතියි.නමුත් සමහර වෙලාවන් වලදි බොට් ක්‍රියාත්මක නොවන බවද සලකන්න.
	
	""")
	
	
@bot.message_handler(commands=["mngrpinf"])
def send_message(message):
	bot.reply_to(message, 
	"""
	╔═══My main group═══╗
	══════════════════
	
	🏘
	┕Name : 🇱🇰 - RS45 Crew Official 2021 - 🇱🇰
	
	🌏
	┕Link : https://t.me/qPfItjLihPhkYzll
	
	👨‍💻
	┕Owner : RS45 Softwares Official
	
	🎁
	┕Youtube : https://www.youtube.com/channel/UCft0sPPD2LqJZlZzKNCvJzA?sub_confirmation=1
	
**┍╍╍┑Subscribe Us!┍╍╍┑**
	
	"""	)
	
	
@bot.message_handler(commands=["ytlink"])
def send_message(message):
	bot.reply_to(message, "https://www.youtube.com/channel/UCft0sPPD2LqJZlZzKNCvJzA?sub_confirmation=1")
	
	
@bot.message_handler(commands=["whatsapp"])
def send_message(message):
	bot.reply_to(message, "wa.me/+94760769366?text=Hi.%20Im%20from%20the%20RS%20Bot")


@bot.message_handler(commands=["warn"])
def send_message(message):
	bot.reply_to(message, """
	⚠ඔබට  """ + message.from_user.first_name + """  විසින් අනතුරු ඇගවීමක් කර ඇත.⚠	
	
	╔කරුණාකර සමූහය තුළ විනීතව හැසිරෙන්න╗
	
	නැතහොත් මෙම සමූහයෙන් ඔබව ඉවත් කරනු ඇත...🚷""")
	
	
@bot.message_handler(commands=["warnlst"])
def send_message(message):
	bot.reply_to(message, """
	
	බල්ලො😂.තොට ආයි කියන්නෙ නෑ.
	විනීතව හැසිරියන් ගෲප් එකේ😐💔.නැත්නම් රිමූ කරලා විතරක් නිකන් ඉන්නෙ නෑ😈 🏳
	
	""")
	
	
@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
	bot.reply_to(message, """
	හායී හායී කෝමද🌝🤟
	
	සාදරයෙන් පිළිගන්නවා.👍
	මගෙ නම ඩේවිඩ්.මන් බොට් කෙනෙක්.🤖
	
	මාව පාවිච්චි කරලා RS45 සමාගමේ මෘදුකාංග download කිරීමේ ලින්ක් ගන්න පුළුවන්😺.වැඩි විස්තර වලට /menu කියලා එවන්න.😜
	
	ඔයාව මේ ගෲප් එකට ඇඩ් කලේ """ + message.from_user.first_name)
	
	
	

@bot.message_handler(content_types=["audio"])
def send_message(message):
        bot.reply_to(message, "මම හිතනවා මේ කටහඩ මියුරු යැයි කියා.මම බොට් කෙනෙකු බැවින් මෙවැනි දේවල් හදුනාගත නොහැක.😐💔")
        
        
@bot.message_handler(content_types=["photo"])
def send_message(message):
   bot.reply_to(message, "මට පොටෝ එවන්න එපා අනේ.මන් බොට් කෙනෙක්නෙ.මට පොටෝ ඕන නෑ🙃")
   
   
@bot.message_handler(content_types=["video"])
def send_message(message):
   bot.reply_to(message, "Youtube video download කිරීමේ පහසු කම ඉදිරි update වලදී බලාපොරොත්තු වන්න.☺❤")
   
   
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, message.text)
    if message.chat.type == "group":
        bot.reply_to(message, "හලෝ බොක්ක.😜ඉතින් මොකෝ වෙන්නෙ.ඇයි මාව මතක් කලේ.උදව්වක් ඕනිද.ඒනම් /menu කියලා එවලා කමාන්ඩ් ටික ගන්න.")
        
            
bot.polling()

while True:
		pass
