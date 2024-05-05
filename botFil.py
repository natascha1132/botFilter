from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter
from aiogram.types import Message


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7057532692:AAHwUixvbpFE5Zu3mcDAWIXAlkzIhvbQcvo'


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Список с ID администраторов бота. !!!Замените на ваш!!!
hello: list[str] = ['Hello', 'Привет']




# Собственный фильтр, проверяющий юзера на админа
class IsHello(BaseFilter):
    def __init__(self, hello: list[str]) -> None:
        self.hello = hello


    async def __call__(self, message: Message) -> hello:
        return message.text in self.hello




# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsHello(hello))
async def answer(message: Message):
    await message.answer(text='Дарова')




# Этот хэндлер будет срабатывать, если апдейт не от админа
@dp.message()
async def answer_if_not_admins_update(message: Message):
    await message.answer(text='Ты не поздоровался!')




if __name__ == '__main__':
    dp.run_polling(bot)
