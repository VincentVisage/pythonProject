from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton('Майки', url='https://sneakers.by/katalog/odezhda/futbolki-majki/'),
                 InlineKeyboardButton('Аксессуары', url='https://sneakers.by/katalog/aksessuary/'),
                 InlineKeyboardButton('Головные уборы', url='https://sneakers.by/katalog/golovnye_ubory/kepki/'),
                 InlineKeyboardButton('Обувь', url='https://sneakers.by/katalog/obuv-belarus/kupit-krossovki-v-belarusi/pol_muzhskie'))
