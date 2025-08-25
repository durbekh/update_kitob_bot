import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from tugma import menyu25, uzb_tarix, uzb_hikoya, uzb_bolalar
from bot_token import TOKEN

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
    await callback.message.answer_photo(
        photo="https://m.media-amazon.com/images/I/51V7W9Z6CQL.jpg",
        caption="Amir Temur tarixi",
    )


@dp.callback_query(F.data == "jaloliddin")
async def jaloliddin(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=c59b0f03288eb3453af5ca185971be1560c7d77e-5236906-images-thumbs&n=13",
        caption="Jaloliddin Manguberdi",
    )


@dp.callback_query(F.data == "navoiy")
async def navoiy(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://m.media-amazon.com/images/I/51RwpWqv9pL.jpg",
        caption="Alisher Navoiy asarlari",
    )


@dp.callback_query(F.data == "bobur")
async def bobur(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=33669092a689bf77a2a892644d67d95efa380c4b-12485500-images-thumbs&n=13",
        caption="Zahiriddin Bobur",
    )


@dp.callback_query(F.data == "qodiriy")
async def qodiriy(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=5834a3efba7ae5ae3ed865c9fc78e16a4a4bd405-10534637-images-thumbs&n=13",
        caption="Abdulla Qodiriy",
    )


@dp.callback_query(F.data == "oybek")
async def oybek(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=8d07d4332cf672ae5161afc68302b1c1228e4f91-5161098-images-thumbs&n=13",
        caption="Oybek ",
    )


@dp.callback_query(F.data == "cholpon")
async def cholpon(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=a6fb260a289f33bac2add26cecccdc3840b8f3ce-5483025-images-thumbs&n=13",
        caption="Cholpon ",
    )


@dp.callback_query(F.data == "olimjon")
async def olimjon(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=cb6d8490e266269c759f43d82aad3932e02e3801-5875850-images-thumbs&n=13",
        caption="Hamid Olimjon",
    )


@dp.callback_query(F.data == "oripov")
async def oripov(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=0af80a99a86e6af5865b86dbef4230cb7dcc9327-4958364-images-thumbs&n=13",
        caption="Abdulla Oripov ",
    )


@dp.callback_query(F.data == "vohidov")
async def vohidov(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=d3c1c10ae6b078d9fb966d391273221d14fa8c22-5344395-images-thumbs&n=13",
        caption="Erkin Vohidov ",
    )


@dp.callback_query(F.data == "shum_bola")
async def shum_bola(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://book.uz/images/books/shum_bola.jpg",
        caption="Shum bola – G‘afur G‘ulom",
    )


@dp.callback_query(F.data == "qutlug_qon")
async def qutlug_qon(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=b3a7a42812a3ae8be8376d23db58c3bf2f114efc-12521528-images-thumbs&n=13",
        caption="Qutlug‘ qon ",
    )


@dp.callback_query(F.data == "bahor")
async def bahor(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=4be41949f0cd243dc1ef6fb5f67f912af2827e2d-4452791-images-thumbs&n=13",
        caption="Bahor qaytmaydi ",
    )


@dp.callback_query(F.data == "sarob")
async def sarob(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=3274b7164d9466f81973b455d57d624cc774c504-4079319-images-thumbs&n=13",
        caption="Sarob",
    )


@dp.callback_query(F.data == "chayon")
async def chayon(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=fc03a558a61a2b57ea3e51771a6d0be357d448e8-5870145-images-thumbs&n=13",
        caption="Mehrobdan chayon",
    )


@dp.callback_query(F.data == "kecha")
async def kecha(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=d1957fce26fe4ffc7d041f701b5e618e640112c1-5486408-images-thumbs&n=13",
        caption="Kecha va kunduz",
    )


@dp.callback_query(F.data == "xazinasi")
async def xazinasi(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=7ca0ef589975fa1967b5eacd339920079766d45e-8189861-images-thumbs&n=13",
        caption="Ulug'bek xazinasi",
    )


@dp.callback_query(F.data == "otkan")
async def otkan(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=b5efb6a8f81ed2a2dcfd0c9c38fcb06fe9923aca-6906583-images-thumbs&n=13",
        caption="O'tgan kunlar",
    )


@dp.callback_query(F.data == "tuzuklari")
async def tuzuklari(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=4c1f47b93f9fc8ecc36a9c55254990c16928c7ed-5026383-images-thumbs&n=13",
        caption="Temur tuzuklari",
    )


@dp.callback_query(F.data == "sariq_dev")
async def sariq_dev(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=fc4f29d0942ed4ac13f6533f281993c9ec8cba1c-13016216-images-thumbs&n=13",
        caption="Sariq Devni minib ",
    )


@dp.callback_query(F.data == "zumrad")
async def zumrad(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=1d5aed3c600e67d3a39a8e52316f3af74563a928-4382526-images-thumbs&n=13",
        caption="Zumrad va Qimmat",
    )


@dp.callback_query(F.data == "boy")
async def boy(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=ec303b880f577602aa2e0e32fcf4a24a6d57b068-8253350-images-thumbs&n=13",
        caption="boy va kambag'al",
    )


@dp.callback_query(F.data == "baliqcha")
async def baliqcha(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://olcha.uz/oz/product/view/oltin-baliqcha.jpg",
        caption="Oltin baliqcha",
    )


@dp.callback_query(F.data == "alpomish")
async def alp(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=757e6ef2f1ad2234cc3e1e72538d3e57c4288264-16321498-images-thumbs&n=13",
        caption="Alpomish",
    )


@dp.callback_query(F.data == "goroqli")
async def goroqli(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=a15930faefa33802dfba93340682cd5dd54fc386-5192563-images-thumbs&n=13",
        caption="Goro'g'li",
    )


@dp.callback_query(F.data == "rustam")
async def rustam(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=4ed1fe91ca542d3d2b9fd3c356aef76e94e21f09-4902992-images-thumbs&n=13",
        caption="Uddabron shogird",
    )


@dp.callback_query(F.data == "ochkoz_bola")
async def qoravoy(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=0e79f7d5dd34fb52434ec54b62addc8788cb6c15-4559743-images-thumbs&n=13",
        caption="ochkoz_bola",
    )


@dp.callback_query(F.data == "qizil_qalpoqcha")
async def oqila(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=55c8c9371e4b9424d75efd0670f3253b8b7ae1b2-5887571-images-thumbs&n=13",
        caption="Qizil qalpoqcha",
    )


@dp.callback_query(F.data == "sholgom")
async def boychechak(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=96ab0117c58b4137f78213113403ef9403184afc-4575484-images-thumbs&n=13",
        caption="Sholg'om",
    )


@dp.callback_query(F.data == "ur_toqmoq")
async def yodgor(callback: CallbackQuery):
    await callback.message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=36e38c5332a2096616be7c9b326c71e285e2411b-10142109-images-thumbs&n=13",
        caption="Ur to'qmoq",
    )


@dp.callback_query(F.data == "ortga")
async def ortga(callback: CallbackQuery):
    await callback.message.answer("Menyu:", reply_markup=menyu25)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtadi!")
