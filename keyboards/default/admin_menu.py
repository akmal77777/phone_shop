from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db_manager

admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Mahsulotlar"),
            KeyboardButton(text="🛒 Buyurtmalar")
        ],
        [
            KeyboardButton(text=" 🔎 Search "),
            KeyboardButton(text="📊 Statistics ")
        ]
    ], resize_keyboard=True
)

admin_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="WAITING ⏳"),
            KeyboardButton(text="ACCEPTED ✅")
        ],
        [
            KeyboardButton(text="Statistics 📊"),
            KeyboardButton(text="CANCELED ❌")
        ],
        [
            KeyboardButton(text="Back ⬅️")
        ],
    ], resize_keyboard=True
)


admin_back_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)


async def add_product_menu_def():
    products = db_manager.get_all_product()
    admin_product_menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    back = KeyboardButton(text="Back ⬅️")
    product_plus = KeyboardButton(text="➕ Mahsulot qo'shish")
    admin_product_menu.insert(back)
    admin_product_menu.insert(product_plus)
    for product in products:
        keyboard = KeyboardButton(text=str(product[1]))
        admin_product_menu.insert(keyboard)

    return admin_product_menu
