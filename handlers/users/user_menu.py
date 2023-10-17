from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.user_menu import user_main_menu,  user_air_pots_menu, user_power_bank_menu, \
    user_watch_menu, user_product_menu
from keyboards.inline.admin_keyboards import admin_order_decision_def
from keyboards.inline.user_keyboards import user_basket_menu
from loader import dp, db_manager
from utils.random_number import get_random_id
from keyboards.inline.user_keyboards import user_product_buy_def


@dp.message_handler(text="📱 My product")
async def product_menu_handler(message: types.Message):
    text = "Quyidagi stikerlardan birini tanlang."
    await message.answer(text=text, reply_markup=user_main_menu)


@dp.message_handler(text="🛍 Store")
async def user_order_menu_handler(message: types.Message):
    text = "Quyidagi tugmachalardan birini tanlang."
    await message.answer(text=text, reply_markup=user_product_menu)


@dp.message_handler(text="Air Pots")
async def iphone_buy_handler(message: types.Message):
    text = "Air pots menyusiga xush kelibisiz."
    await message.answer(text=text, reply_markup=user_air_pots_menu)


@dp.message_handler(text="Powerbank")
async def iphone_buy_handler(message: types.Message):
    text = "Power bank menyusiga xush kelibisiz."
    await message.answer(text=text, reply_markup=user_power_bank_menu)


@dp.message_handler(text="Smart Watch")
async def iphone_buy_handler(message: types.Message):
    text = "Smart Watch menyusiga xush kelibisiz."
    await message.answer(text=text, reply_markup=user_watch_menu)


@dp.message_handler(text="Watch Ultra")
async def iphone_buy_handler(message: types.Message):
    text = "Watch menyusiga xush kelibisiz."
    await message.answer(text=text, reply_markup=user_watch_menu)


@dp.message_handler(state="user-stickers-state")
async def get_one_sticker_handler(message: types.Message, state: FSMContext):
    name = message.text
    sticker = db_manager.search_sticker_by_name(name)
    if sticker:
        name = sticker[1]
        price = sticker[2]
        description = sticker[3]
        photo = sticker[4]
        quantity2 = sticker[5]

        data = await state.get_data()
        basket = data.get('basket') if data.get('basket') else dict()
        item = basket.get(name) if basket.get(name) else dict()
        quantity = item.get('quantity') if item.get('quantity') else 0
        total = item.get('total') if item.get('total') else 0
        await state.update_data({
            "product": name,
            "price": price
        })

        caption = f"{name} | {price} so'm | {quantity2} ta bor\n\n{description}"
        await message.answer_photo(photo=photo, caption=caption,
                                   reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Air Pots 2.2")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Air Pots 2.2") if basket.get("Air Pots 2.2") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Air Pots 2.2",
        "price": 180000
    })
    photo = "https://cdn0.youla.io/files/images/720_720_out/60/1c/601c51168d3f1e13b8104cb7-1.jpg"
    text = "Air Pots 2.2\nLux copy\nInkax firmenny AIRPODS \nNarxi: 180000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Air Pots 3")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Air Pots 3") if basket.get("Air Pots 3") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Air Pots 3",
        "price": 250000
    })
    photo = "https://i.ytimg.com/vi/aCmEy1ProEI/maxresdefault.jpg"
    text = "Air Pots 3\nLux copy\nInkax firmenny AIRPODS \nNarxi: 250000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Air Pots pro")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Air Pots pro") if basket.get("Air Pots pro") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Air Pots pro",
        "price": 250000
    })
    photo = "https://i.ebayimg.com/images/g/ykEAAOSwfahghsM3/s-l1600.jpg"
    text = "Air Pots pro\nLux copy\nInkax firmenny AIRPODS \nNarxi: 250000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Air Pots pro 2")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Air Pots 3") if basket.get("Air Pots 3") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Air Pots pro 2",
        "price": 300000
    })
    photo = "https://avatars.mds.yandex.net/get-mpic/1767151/img_id1092045755768758416.jpeg/orig"
    text = "Air Pots pro 2\nLux copy\nInkax firmenny AIRPODS\nNarxi: 300000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Power Bank, 20W 10000mAh 🔋")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Power Bank, 20W 10000mAh 🔋") if basket.get("Power Bank, 20W 10000mAh 🔋") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Power Bank, 20W 10000mAh 🔋",
        "price": 285000
    })
    photo = "https://m.media-amazon.com/images/S/aplus-media-library-service-media/83c03beb-0459-437b-864e-a2424471bb" \
            "fe.__CR0,0,970,600_PT0_SX970_V1___.jpg"
    text = "Power Bank, 20W 10000mAh 🔋\nNarxi: 285000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Baseus Power Bank, 65W 20000mAh 🔋")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Baseus Power Bank, 65W 20000mAh 🔋") if basket.get("Baseus Power Bank, 65W 20000mAh 🔋") else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Baseus Power Bank, 65W 20000mAh 🔋",
        "price": 350000
    })
    photo = "https://ae01.alicdn.com/kf/S4130025440c64df987ee89692d36c61dw/Baseus-65W-Power-Bank-20000mah-PD-QC-3-0-Fa"\
            "st-Charging-Powerbank-External-Batteries-Portable-Charger.jpg"
    text = "Baseus Power Bank, 65W 20000mAh 🔋\nNarxi: 350000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Wireless Power Bank, 33W 10000 mAh 🔋")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Wireless Power Bank, 33W 10000 mAh") if basket.get("Wireless PowerBank,33W 10000 mAh")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Wireless Power Bank, 33W 10000 mAh",
        "price": 350000
    })
    photo = "https://robot4home.ru/image/cache/catalog/123/all/00202/pb1030zm-16-1000x1000.jpg"
    text = "Wireless Power Bank, 33W 10000 mAh\nNarxi: 275000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Li-Pol 10000 мAh🔋")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Li-Pol 10000 мAh🔋") if basket.get("Li-Pol 10000 мAh🔋")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Li-Pol 10000 мAh🔋",
        "price": 500000
    })
    photo = "https://cdn.citilink.ru/13s6fF3Y0xLy15CLG6ZOx8bP5QtEcrcTE2iov83E8AE/resizing_type:fit/gravity:sm/width" \
            ":400/height:400/plain/product-images/9ab85d48-d5f2-448e-ae46-53aad4462590.jpg"
    text = " Li-Pol 10000 мAh🔋\nNarxi: 500000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Smart 8 Ultra")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Smart 8 Ultra") if basket.get("Smart 8 Ultra")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Smart 8 Ultra",
        "price": 300000
    })
    photo = "https://frankfurt.apollo.olxcdn.com/v1/files/mnhb5wa0w1z91-UZ/image;s=1000x700"
    text = "Smart 8 Ultra\nLux copy\nNarxi: 120000"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Smart X8 + Ultra")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Smart X8 + Ultra") if basket.get("Smart X8 + Ultra")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Smart X8 + Ultra",
        "price": 299000
    })
    photo = "https://catalog-sadovod.ru/images/detailed/2337/49chas.jpg"
    text = "Smart X8 + Ultra\nLux copy\nNarxi: 29900so'm"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Watch ULTRA Series 8")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Watch ULTRA Series 8") if basket.get("Watch ULTRA Series 8")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Watch ULTRA Series 8",
        "price": 400000
    })
    photo = "https://avatars.mds.yandex.net/get-mpic/4585707/img_id3317253342213206110.jpeg/orig"
    text = "Watch ULTRA Series 8\nLux copy\nNarxi: 400000so'm"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.message_handler(text="Watch Ultra 8 49mm")
async def anime_sticker_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get("Watch Ultra 8 49mm") if basket.get("Watch Ultra 8 49mm")else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    total = item.get('total') if item.get('total') else 0
    await state.update_data({
        "product": "Watch Ultra 8 49mm",
        "price": 360000
    })
    photo = "https://avatars.mds.yandex.net/get-mpic/4585707/img_id3317253342213206110.jpeg/orig"
    text = "Watch Ultra 8 49mm\nLux copy\nNarxi: 360000so'm"
    await message.answer_photo(photo=photo, caption=text, reply_markup=await user_product_buy_def(quantity, total))


@dp.callback_query_handler(text="plus_product")
async def plus_product_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product = data.get('product')
    price = data.get('price')
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get(product) if basket.get(product) else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    if quantity == 10:
        text = "Bitta zakazda bitta mahsulotdan 10 tadan ko'p olish" \
               " qatiyan man etiladi. Hurmat bilan BACK-425 guruhi"
        await call.answer(text=text, show_alert=True)
    else:
        quantity += 1
        basket[product] = {
            "quantity": quantity,
            "price": price,
            "total": price * quantity,
            "name": product
        }
        await state.update_data({
            "basket": basket
        })
        text = "Mahsulot bittaga ko'paydi xo'jayin"
        await call.answer(text=text)
        await call.message.edit_reply_markup(reply_markup=await user_product_buy_def(quantity, quantity * price))


@dp.callback_query_handler(text="minus_product")
async def minus_product_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product = data.get('product')
    price = data.get('price')
    basket = data.get('basket') if data.get('basket') else dict()
    item = basket.get(product) if basket.get(product) else dict()
    quantity = item.get('quantity') if item.get('quantity') else 0
    if quantity == 0:
        text = "0 dan kam bo'lishi mumkin emas"
        await call.answer(text=text, show_alert=True)
    else:
        quantity -= 1
        basket[product] = {
            "quantity": quantity,
            "price": price,
            "total": price * quantity,
            "name": product
        }
        await state.update_data({
            "basket": basket
        })
        text = "Mahsulot bittaga kamaydi xo'jayin"
        await call.answer(text=text)
        await call.message.edit_reply_markup(reply_markup=await user_product_buy_def(quantity, quantity * price))


@dp.callback_query_handler(text="show_basket")
async def show_product_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket')
    if basket:
        text = "Sizning savatingizda quyidagi mahsulotlar bor: \n\n"
        counter = 1
        total = 0
        for product in basket.values():
            text += f"<i><b>{counter}) {product['name']}\t| {product['quantity']} ta " \
                    f"\t| {product['price']}\t| {product['total']}\n</b></i>"
            counter += 1
            total += int(product['total'])

        text += f"\nJami: {total}"

        await call.message.answer(text=text, reply_markup=user_basket_menu)
    else:
        text = "Sizning savatingizda hech narsa mavjud emas. ❗️"
        await call.answer(text=text, show_alert=True)


@dp.callback_query_handler(text="clear_basket")
async def clear_basket_handler(call: CallbackQuery, state: FSMContext):
    await state.update_data({
        "basket": dict()
    })
    popup = "Savat tozalandi ❗️"
    await call.answer(text=popup, show_alert=True)
    text = "Sizning savatingizda quyidagi mahsulotlar bor: "
    await call.message.edit_text(text=text, reply_markup=user_basket_menu)


@dp.callback_query_handler(text="order_basket", state="user-stickers-state")
async def order_basket_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket')
    user = db_manager.get_user(call.message)
    order_id = get_random_id()
    if basket and user:
        text = "Sizning zakazingiz quyidagi ko'rinishda: \n"
        text += f"""
ID: {order_id}
FI: {user[2]}
TEL: {user[3]}
SANA: {call.message.date}
STATUS: WAITING

"""
        counter = 1
        total = 0
        for product in basket.values():
            text += f"<i><b>{counter}) {product['name']}\t| {product['quantity']} ta " \
                    f"\t| {product['price']}\t| {product['total']}\n</b></i>"
            counter += 1
            total += int(product['total'])
        text += f"\nJami: {total}"

        await state.update_data({
            "basket": dict()
        })
        new_order = db_manager.append_order(call.message, basket, order_id)
        if not new_order:
            admin_text = "Zakazlarni bazaga qo'shish joyida xatolik chiqdi"
            await dp.bot.send_message(text=admin_text, chat_id=ADMINS[0])

        await dp.bot.send_message(chat_id=ADMINS[0], text=text,
                                  reply_markup=await admin_order_decision_def(order_id, call.message.chat.id))
        await call.message.answer(text=text)
    else:
        text = "Sizning savatingizda hech narsa mavjud emas. ❗️"
        await call.answer(text=text, show_alert=True)


@dp.callback_query_handler(text="order_basket")
async def order_basket_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    basket = data.get('basket')
    user = db_manager.get_user(call.message)
    order_id = get_random_id()
    if basket and user:
        text = "Sizning zakazingiz quyidagi ko'rinishda: \n"
        text += f"""
ID: {order_id}
FI: {user[2]}
TEL: {user[3]}
SANA: {call.message.date}
STATUS: WAITING

"""
        counter = 1
        total = 0
        for product in basket.values():
            text += f"<i><b>{counter}) {product['name']}\t| {product['quantity']} ta " \
                    f"\t| {product['price']} so'm\t| {product['total']} so'm\n</b></i>"
            counter += 1
            total += product['total']
        text += f"\nJami: {total} so'm"

        await state.update_data({
            "basket": dict()
        })
        new_order = db_manager.append_order(call.message, basket, order_id)
        if not new_order:
            admin_text = "Zakazlarni bazaga qo'shish joyida xatolik chiqdi"
            await dp.bot.send_message(text=admin_text, chat_id=ADMINS[0])

        await dp.bot.send_message(chat_id=ADMINS[0], text=text,
                                  reply_markup=await admin_order_decision_def(order_id, call.message.chat.id))
        await call.message.answer(text=text)
    else:
        text = "Sizning savatingizda hech narsa mavjud emas. ❗️"
        await call.answer(text=text, show_alert=True)


@dp.message_handler(text="⬅️ Back", state="*")
async def user_product_back_menu(message: types.Message, state: FSMContext):
    text = "Welcom to main menu"
    await message.answer(text=text, reply_markup=user_product_menu)
    await state.finish()


@dp.message_handler(text="Back ⬅️", state="*")
async def user_main_menu_back(message: types.Message, state: FSMContext):
    text = "Welcom to main menu"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()
