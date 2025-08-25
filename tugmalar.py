from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

menyu25 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="hikoya")],
        [KeyboardButton(text="tarix")],
        [KeyboardButton(text="bolalar")],
    ],
    resize_keyboard=True,
)

uzb_tarix = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Amir Temur tarixi", callback_data="amir_temur"),
            InlineKeyboardButton(
                text="Jaloliddin Manguberdi", callback_data="jaloliddin"
            ),
        ],
        [
            InlineKeyboardButton(text="Alisher Navoiy", callback_data="navoiy"),
            InlineKeyboardButton(text="Zahiriddin Bobur", callback_data="bobur"),
        ],
        [
            InlineKeyboardButton(text="Abdulla Qodiriy", callback_data="qodiriy"),
            InlineKeyboardButton(text="Oybek", callback_data="oybek"),
        ],
        [
            InlineKeyboardButton(text="Cho‘lpon", callback_data="cholpon"),
            InlineKeyboardButton(text="Hamid Olimjon", callback_data="olimjon"),
        ],
        [
            InlineKeyboardButton(text="Abdulla Oripov", callback_data="oripov"),
            InlineKeyboardButton(text="Erkin Vohidov", callback_data="vohidov"),
        ],
        [InlineKeyboardButton(text="Ortga", callback_data="ortga")],
    ]
)

uzb_hikoya = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Shum bola", callback_data="shum_bola"),
            InlineKeyboardButton(text="Qutlug‘ qon", callback_data="qutlug_qon"),
        ],
        [
            InlineKeyboardButton(text="Bahor qaytmaydi", callback_data="bahor"),
            InlineKeyboardButton(text="Sarob", callback_data="sarob"),
        ],
        [
            InlineKeyboardButton(text="Mehrobdan chayon", callback_data="chayon"),
            InlineKeyboardButton(text="Kecha va kunduz", callback_data="kecha"),
        ],
        [
            InlineKeyboardButton(text="Ulug‘bek xazinasi", callback_data="xazinasi"),
            InlineKeyboardButton(text="O‘tkan kunlar", callback_data="otkan"),
        ],
        [
            InlineKeyboardButton(text="Temur tuzuklari", callback_data="tuzuklari"),
            InlineKeyboardButton(text="Sariq devni minib", callback_data="sariq_dev"),
        ],
        [InlineKeyboardButton(text="Ortga", callback_data="ortga")],
    ]
)

uzb_bolalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zumrad va Qimmat", callback_data="zumrad"),
            InlineKeyboardButton(text="Boy va kambag‘al", callback_data="boy"),
        ],
        [
            InlineKeyboardButton(text="Oltin baliqcha", callback_data="baliqcha"),
            InlineKeyboardButton(text="Alpomish", callback_data="alp"),
        ],
        [
            InlineKeyboardButton(text="Go‘ro‘g‘li", callback_data="goroqli"),
            InlineKeyboardButton(text="Rustam", callback_data="rustam"),
        ],
        [
            InlineKeyboardButton(text="Ochkoz bola", callback_data="ochkoz_bola"),
            InlineKeyboardButton(
                text="Qizil alpoqcha", callback_data="qizil_qalpoqcha"
            ),
        ],
        [
            InlineKeyboardButton(text="Sholg'om", callback_data="sholgom"),
            InlineKeyboardButton(text="Ur toqmoq", callback_data="ur_toqmoq"),
        ],
        [InlineKeyboardButton(text="Ortga", callback_data="ortga")],
    ]
)
