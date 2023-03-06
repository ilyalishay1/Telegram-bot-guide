import telebot
import requests
import config
import emoji
from bs4 import BeautifulSoup
from telebot import types


smiling_face_emoji = emoji.emojize(':smiling_face:')
confused_face_emoji = emoji.emojize(':confused_emoji:')


image1 = open('images/sight1nesvizh.png', 'rb')
image2 = open('images/sight2.jpg', 'rb')
image3 = open('images/sight3.jpg', 'rb')
image4 = open('images/sight4.jpg', 'rb')
image5 = open('images/sight5.jpg', 'rb')
image6 = open('images/sight6.jpg', 'rb')
image7 = open('images/sight7.jpg', 'rb')
image8 = open('images/sight8.jpg', 'rb')
image9 = open('images/sight9.jpg', 'rb')
image10 = open('images/sight10.png', 'rb')
image11 = open('images/sight11.jpg', 'rb')
image12 = open('images/sight12.jpg', 'rb')
image13 = open('images/sight13.png', 'rb')
image14 = open('images/sight14.jpg', 'rb')
image15 = open('images/sight15.jpg', 'rb')
image16 = open('images/sight16.jpg', 'rb')
image17 = open('images/sight17.png', 'rb')
image18 = open('images/sight18.png', 'rb')
image19 = open('images/sight19.png', 'rb')
image20 = open('images/sight20.png', 'rb')
image21 = open('images/sight21.jpeg', 'rb')


url1 = 'https://belarusmini.by/news/20-dostoprimechatelnostey-belarusi/'
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.content, 'html.parser')
all_sights = soup1.find_all('ol')[0].text
sight1 = soup1.find_all('h3')[0].text
sight1_info1 = soup1.find_all('p')[4].text
sight1_info2 = soup1.find_all('p')[5].text
sight1_info = sight1_info1 + sight1_info2

sight2 = soup1.find_all('h3')[1].text
sight2_info1 = soup1.find_all('p')[10].text
sight2_info2 = soup1.find_all('p')[11].text
sight2_info = sight2_info1 + sight2_info2

sight3 = soup1.find_all('h3')[2].text
sight3_info1 = soup1.find_all('p')[13].text
sight3_info2 = soup1.find_all('p')[14].text
sight3_info = sight3_info1 + sight3_info2

sight4 = soup1.find_all('h3')[3].text
sight4_info = soup1.find_all('p')[16].text

sight5 = soup1.find_all('h3')[4].text
sight5_info = soup1.find_all('p')[18].text

sight6 = soup1.find_all('h3')[5].text
sight6_info1 = soup1.find_all('p')[20].text
sight6_info2 = soup1.find_all('p')[21].text
sight6_info = sight6_info1 + sight6_info2

sight7 = soup1.find_all('h3')[6].text
sight7_info = soup1.find_all('p')[23].text

sight8 = soup1.find_all('h3')[7].text
sight8_info = soup1.find_all('p')[25].text

sight9 = soup1.find_all('h3')[8].text
sight9_info = soup1.find_all('p')[27].text

sight10 = soup1.find_all('h3')[9].text
sight10_info1 = soup1.find_all('p')[29].text
sight10_info2 = soup1.find_all('p')[30].text
sight10_info = sight10_info1 + sight10_info2

sight11 = soup1.find_all('h3')[10].text
sight11_info = soup1.find_all('p')[32].text

sight12 = soup1.find_all('h3')[11].text
sight12_info = soup1.find_all('p')[34].text

sight13 = soup1.find_all('h3')[12].text
sight13_info1 = soup1.find_all('p')[36].text
sight13_info2 = soup1.find_all('p')[37].text
sight13_info = sight13_info1 + sight13_info2

sight14 = soup1.find_all('h3')[13].text
sight14_info = soup1.find_all('p')[39].text

sight15 = soup1.find_all('h3')[14].text
sight15_info = soup1.find_all('p')[41].text

sight16 = soup1.find_all('h3')[15].text
sight16_info = soup1.find_all('p')[43].text

sight17 = soup1.find_all('h3')[16].text
sight17_info = soup1.find_all('p')[45].text

sight18 = soup1.find_all('h3')[17].text
sight18_info = soup1.find_all('p')[47].text

sight19 = soup1.find_all('h3')[18].text
sight19_info = soup1.find_all('p')[49].text

sight20 = soup1.find_all('h3')[19].text
sight20_info = soup1.find_all('p')[50].text

sight21 = 'Буйничское поле ― мемориальный комплекс, расположенный юго-западнее Могилёва, вблизи деревни Буйничи.'


url2 = 'https://34travel.me/gotobelarus/rubric/routes'
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.content, 'html.parser')
route1 = soup2.find_all('div', class_='post-short-info')[0].text
route2 = soup2.find_all('div', class_='post-short-info')[1].text
route3 = soup2.find_all('div', class_='post-short-info')[2].text
route4 = soup2.find_all('div', class_='post-short-info')[3].text
route5 = soup2.find_all('div', class_='post-short-info')[4].text
route6 = soup2.find_all('div', class_='post-short-info')[5].text
route7 = soup2.find_all('div', class_='post-short-info')[6].text
route8 = soup2.find_all('div', class_='post-short-info')[7].text
route9 = soup2.find_all('div', class_='post-short-info')[8].text
route10 = soup2.find_all('div', class_='post-short-info')[9].text
route11 = soup2.find_all('div', class_='post-short-info')[10].text
route12 = soup2.find_all('div', class_='post-short-info')[11].text
all_routes = route1 + route2 + route3 + route4 + route5 + route6 + route7 + route8 + route9 + route10 + route11+route12


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Достопримечательности')
    button2 = types.KeyboardButton('Маршруты')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, f'Привет{smiling_face_emoji} '
                                      f'Я бот-гид по главным достопримечательностям Беларуси! '
                                      'Выберите что вас интересует', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def content(message):
    if message.text == 'Достопримечательности':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Все области')
        button2 = types.KeyboardButton('Гродненская область')
        button3 = types.KeyboardButton('Минская область')
        button4 = types.KeyboardButton('Витебская область')
        button5 = types.KeyboardButton('Могилевская область')
        button6 = types.KeyboardButton('Брестская область')
        button7 = types.KeyboardButton('Гомельская область')
        button8 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
        bot.send_message(message.chat.id, 'Отлично! Выберите область достопримечательности которой хотите посмотреть',
                         reply_markup=markup)

    elif message.text == 'Маршруты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Все маршруты')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Нажмите на кнопку, чтобы увидеть возможные маршруты', reply_markup=markup)

    elif message.text == 'Все области':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1)
        bot.send_message(message.chat.id, all_sights + '\n' + '''Если хотите узнать более подробную
         информацию о достопримечательности, найдите ее в разделе одной из областей''', reply_markup=markup)

    elif message.text == 'Гродненская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Мирский замок и Несвижский дворец')
        button2 = types.KeyboardButton('Коложская церковь в Гродно')
        button3 = types.KeyboardButton('Свято-Успенский Жировичский монастырь')
        button4 = types.KeyboardButton('Троицкий костел в деревне Гервяты')
        button5 = types.KeyboardButton('Лидский замок')
        button6 = types.KeyboardButton('Хоральная синагога в Гродно')
        button7 = types.KeyboardButton('Кревский замок')
        button8 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Гродненской области', reply_markup=markup)

    elif message.text == 'Минская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Мирский замок и Несвижский дворец')
        button2 = types.KeyboardButton('Место переправы Наполеона в деревне Студенка')
        button3 = types.KeyboardButton('Музей народных ремесел «Дудутки»')
        button4 = types.KeyboardButton('Мемориальный комплекс «Хатынь»')
        button5 = types.KeyboardButton('Историко-культурный комплекс «Линия Сталина»')
        button6 = types.KeyboardButton('Музей архитектурных миниатюр «Страна мини»')
        button7 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Минской области', reply_markup=markup)

    elif message.text == 'Витебская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Софийский собор в Полоцке')
        button2 = types.KeyboardButton('Церковь Успения в Сарье')
        button3 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Витебской области', reply_markup=markup)

    elif message.text == 'Могилевская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Буйничское поле')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Могилевской области', reply_markup=markup)

    elif message.text == 'Брестская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Дворцовый комплекс Сапег в Ружанах')
        button2 = types.KeyboardButton('Замок Пусловских в Коссово')
        button3 = types.KeyboardButton('Национальный парк «Беловежская пуща»')
        button4 = types.KeyboardButton('Брестская крепость')
        button5 = types.KeyboardButton('Каменецкая вежа')
        button6 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Брестской области', reply_markup=markup)

    elif message.text == 'Гомельская область':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Дворцово-парковый ансамбль Румянцевых-Паскевичей')
        button2 = types.KeyboardButton('Вернуться в главное меню')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Вы выбрали достопримечательности Гомельской области', reply_markup=markup)

    elif message.text == 'Все маршруты':
        bot.send_message(message.chat.id, all_routes)

    elif message.text == 'Мирский замок и Несвижский дворец':
        bot.send_message(message.chat.id, sight1 + '\n' + sight1_info)
        bot.send_photo(message.chat.id, image1)

    elif message.text == 'Коложская церковь в Гродно':
        bot.send_message(message.chat.id, sight7 + '\n' + sight7_info)
        bot.send_photo(message.chat.id, image7)

    elif message.text == 'Свято-Успенский Жировичский монастырь':
        bot.send_message(message.chat.id, sight8 + '\n' + sight8_info)
        bot.send_photo(message.chat.id, image8)

    elif message.text == 'Троицкий костел в деревне Гервяты':
        bot.send_message(message.chat.id, sight11 + '\n' + sight11_info)
        bot.send_photo(message.chat.id, image11)

    elif message.text == 'Лидский замок':
        bot.send_message(message.chat.id, sight16 + '\n' + sight16_info)
        bot.send_photo(message.chat.id, image16)

    elif message.text == 'Хоральная синагога в Гродно':
        bot.send_message(message.chat.id, sight19 + '\n' + sight19_info)
        bot.send_photo(message.chat.id, image19)

    elif message.text == 'Кревский замок':
        bot.send_message(message.chat.id, sight20 + '\n' + sight20_info)
        bot.send_photo(message.chat.id, image20)

    elif message.text == 'Место переправы Наполеона в деревне Студенка':
        bot.send_message(message.chat.id, sight2 + '\n' + sight2_info)
        bot.send_photo(message.chat.id, image2)

    elif message.text == 'Музей народных ремесел «Дудутки»':
        bot.send_message(message.chat.id, sight3 + '\n' + sight3_info)
        bot.send_photo(message.chat.id, image3)

    elif message.text == 'Мемориальный комплекс «Хатынь»':
        bot.send_message(message.chat.id, sight4 + '\n' + sight4_info)
        bot.send_photo(message.chat.id, image4)

    elif message.text == 'Историко-культурный комплекс «Линия Сталина»':
        bot.send_message(message.chat.id, sight5 + '\n' + sight5_info)
        bot.send_photo(message.chat.id, image5)

    elif message.text == 'Музей архитектурных миниатюр «Страна мини»':
        bot.send_message(message.chat.id, sight6 + '\n' + sight6_info)
        bot.send_photo(message.chat.id, image6)

    elif message.text == 'Софийский собор в Полоцке':
        bot.send_message(message.chat.id, sight15 + '\n' + sight15_info)
        bot.send_photo(message.chat.id, image15)

    elif message.text == 'Церковь Успения в Сарье':
        bot.send_message(message.chat.id, sight18 + '\n' + sight18_info)
        bot.send_photo(message.chat.id, image18)

    elif message.text == 'Буйничское поле':
        bot.send_message(message.chat.id, sight21)
        bot.send_photo(message.chat.id, image21)

    elif message.text == 'Дворцовый комплекс Сапег в Ружанах':
        bot.send_message(message.chat.id, sight9 + '\n' + sight9_info)
        bot.send_photo(message.chat.id, image9)

    elif message.text == 'Замок Пусловских в Коссово':
        bot.send_message(message.chat.id, sight10 + '\n' + sight10_info)
        bot.send_photo(message.chat.id, image10)

    elif message.text == 'Национальный парк «Беловежская пуща»':
        bot.send_message(message.chat.id, sight13 + '\n' + sight13_info)
        bot.send_photo(message.chat.id, image13)

    elif message.text == 'Брестская крепость':
        bot.send_message(message.chat.id, sight14 + '\n' + sight14_info)
        bot.send_photo(message.chat.id, image14)

    elif message.text == 'Каменецкая вежа':
        bot.send_message(message.chat.id, sight17 + '\n' + sight17_info)
        bot.send_photo(message.chat.id, image17)

    elif message.text == 'Дворцово-парковый ансамбль Румянцевых-Паскевичей':
        bot.send_message(message.chat.id, sight12 + '\n' + sight12_info)
        bot.send_photo(message.chat.id, image12)

    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Достопримечательности')
        button2 = types.KeyboardButton('Маршруты')
        markup.add(button1, button2)
        bot.send_message(message.chat.id, 'Вы вернулись в главное меню!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Такой команды не существует{confused_face_emoji}')


bot.polling(none_stop=True)
