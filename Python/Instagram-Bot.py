from instabot import Bot
bot = Bot()

bot.login(username='user_name', password='user_password')

bot.upload_photo('Photo.jpg', caption='caption of Post Here')