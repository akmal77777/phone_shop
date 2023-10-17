from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍 Store"),
            KeyboardButton(text="🛍 Mening zakazlarim"),
        ],
        [
            KeyboardButton(text="👤 Profile"),
            KeyboardButton(text="📞 Contact"),
        ]
    ], resize_keyboard=True
)

user_order_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳ WAITING"),
            KeyboardButton(text="✅ ACCEPTED")
        ],
        [
            KeyboardButton(text="📊 Statistics"),
            KeyboardButton(text="❌ CANCELED")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ],
    ], resize_keyboard=True
)

user_air_pots_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Air Pots 2.2"),
            KeyboardButton(text="Air Pots 3")

        ],
        [
            KeyboardButton(text="Air Pots pro"),
            KeyboardButton(text="Air Pots pro 2")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)

user_product_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Air Pots"),
            KeyboardButton(text="Powerbank")
        ],
        [
            KeyboardButton(text="Smart Watch"),
            KeyboardButton(text="Watch Ultra")
        ],
        [
            KeyboardButton(text="Back ⬅️")
        ]
    ], resize_keyboard=True
)

user_power_bank_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Power Bank, 20W 10000mAh 🔋"),
            KeyboardButton(text="Baseus Power Bank, 65W 20000mAh 🔋 ")
        ],
        [
            KeyboardButton(text="Wireless Power Bank, 33W 10000 mAh 🔋"),
            KeyboardButton(text="Li-Pol 10000 мAh🔋 ")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)


user_smart_watch_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Smart 8 Ultra"),
            KeyboardButton(text="Smart X8 + Ultra")

        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)


user_watch_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Watch ULTRA Series 8"),
            KeyboardButton(text="Watch Ultra 8 49mm")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)

user_main_menu_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)

user_product_back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ], resize_keyboard=True
)


