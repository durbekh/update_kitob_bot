import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from kitob import TOKEN, menyu25, uzb_tarix, uzb_hikoya, uzb_bolalar

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum! Kitob janrini tanlang:", reply_markup=menyu25
    )


@dp.message(F.text == "hikoya")
async def handler_hikoya(message: Message):
    await message.answer("Hikoya kitoblari:", reply_markup=uzb_hikoya)


@dp.message(F.text == "tarix")
async def handler_tarix(message: Message):
    await message.answer("Tarixiy kitoblar:", reply_markup=uzb_tarix)


@dp.message(F.text == "bolalar")
async def handler_bolalar(message: Message):
    await message.answer("Bolalar kitoblari:", reply_markup=uzb_bolalar)


@dp.callback_query(F.data == "amir_temur")
async def amir_temur(callback: CallbackQuery):
    await callback.message.answer("Amir Temur tarixi")


@dp.callback_query(F.data == "jaloliddin")
async def jaloliddin(callback: CallbackQuery):
    await callback.message.answer("Jaloliddin Manguberdi")


@dp.callback_query(F.data == "navoiy")
async def navoiy(callback: CallbackQuery):
    await callback.message.answer("Alisher Navoiy")


@dp.callback_query(F.data == "bobur")
async def bobur(callback: CallbackQuery):
    await callback.message.answer("Zahiriddin Bobur")


@dp.callback_query(F.data == "qodiriy")
async def qodiriy(callback: CallbackQuery):
    await callback.message.answer("Abdulla Qodiriy")


@dp.callback_query(F.data == "oybek")
async def oybek(callback: CallbackQuery):
    await callback.message.answer("Oybek")


@dp.callback_query(F.data == "cholpon")
async def cholpon(callback: CallbackQuery):
    await callback.message.answer("Cho‘lpon")


@dp.callback_query(F.data == "olimjon")
async def olimjon(callback: CallbackQuery):
    await callback.message.answer("Hamid Olimjon")


@dp.callback_query(F.data == "oripov")
async def oripov(callback: CallbackQuery):
    await callback.message.answer("Abdulla Oripov")


@dp.callback_query(F.data == "vohidov")
async def vohidov(callback: CallbackQuery):
    await callback.message.answer("Erkin Vohidov")


@dp.callback_query(F.data == "shum_bola")
async def shum_bola(callback: CallbackQuery):
    await callback.message.answer("Shum bola")


@dp.callback_query(F.data == "qutlug_qon")
async def qutlug_qon(callback: CallbackQuery):
    await callback.message.answer("Qutlug‘ qon")


@dp.callback_query(F.data == "bahor")
async def bahor(callback: CallbackQuery):
    await callback.message.answer("Bahor qaytmaydi")


@dp.callback_query(F.data == "sarob")
async def sarob(callback: CallbackQuery):
    await callback.message.answer("Sarob")


@dp.callback_query(F.data == "chayon")
async def chayon(callback: CallbackQuery):
    await callback.message.answer("Mehrobdan chayon")


@dp.callback_query(F.data == "kecha")
async def kecha(callback: CallbackQuery):
    await callback.message.answer("Kecha va kunduz")


@dp.callback_query(F.data == "xazinasi")
async def xazinasi(callback: CallbackQuery):
    await callback.message.answer("Ulug‘bek xazinasi")


@dp.callback_query(F.data == "otkan")
async def otkan(callback: CallbackQuery):
    await callback.message.answer("O‘tkan kunlar")


@dp.callback_query(F.data == "tuzuklari")
async def tuzuklari(callback: CallbackQuery):
    await callback.message.answer("Temur tuzuklari")


@dp.callback_query(F.data == "sariq_dev")
async def sariq_dev(callback: CallbackQuery):
    await callback.message.answer("Sariq devni minib")


@dp.callback_query(F.data == "zumrad")
async def zumrad(callback: CallbackQuery):
    await callback.message.answer("Zumrad va Qimmat")


@dp.callback_query(F.data == "boy")
async def boy(callback: CallbackQuery):
    await callback.message.answer("Boy ila kambag‘al")


@dp.callback_query(F.data == "baliqcha")
async def baliqcha(callback: CallbackQuery):
    await callback.message.answer("Oltin baliqcha")


@dp.callback_query(F.data == "alp")
async def alp(callback: CallbackQuery):
    await callback.message.answer("Alpomish")


@dp.callback_query(F.data == "goroqli")
async def goroqli(callback: CallbackQuery):
    await callback.message.answer("Go‘ro‘g‘li")


@dp.callback_query(F.data == "rustam")
async def rustam(callback: CallbackQuery):
    await callback.message.answer("Rustam")


@dp.callback_query(F.data == "qoravoy")
async def qoravoy(callback: CallbackQuery):
    await callback.message.answer("Qoravoy")


@dp.callback_query(F.data == "oqila")
async def oqila(callback: CallbackQuery):
    await callback.message.answer("Oqila qiz")


@dp.callback_query(F.data == "boychechak")
async def boychechak(callback: CallbackQuery):
    await callback.message.answer("Boychechak")


@dp.callback_query(F.data == "yodgor")
async def yodgor(callback: CallbackQuery):
    await callback.message.answer("Yodgor ertaklari")


@dp.callback_query(F.data == "ortga")
async def ortga(callback: CallbackQuery):
    await callback.message.answer("Bosh menyuga qaytdingiz:", reply_markup=menyu25)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtadi!")
