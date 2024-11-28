from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboard import *
from texts import *
import matplotlib.pyplot as plt
from config import *

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer("Привет, я тест бот.", reply_markup=kb)

class TempState(StatesGroup):
    phlegmatic = State()
    choleric = State()
    sanguine = State()
    melancholic = State()
    number_v = State()
    name_user = State()

@dp.message_handler(text='Начать тестирование', state="*")
async def v_1(message: Message, state: FSMContext):
    await state.update_data(number_v=1)
    await state.update_data(choleric=0)
    await state.update_data(phlegmatic=0)
    await state.update_data(sanguine=0)
    await state.update_data(melancholic=0)
    await state.update_data(name_user=message.from_user.username)
    await message.answer(f'{block_choleric[1]}', reply_markup=kb_in)

@dp.callback_query_handler(text=('response_yes', 'response_no'), state="*")
async def v_n(callback: types.callback_query, state):
    data = await state.get_data()
    await state.update_data(number_v=data["number_v"] + 1)
    data = await state.get_data()
    print(f'НОМЕР ВОПРОСА {data["number_v"]} ')
    if callback.data == 'response_yes' and data["number_v"] <= 5:
        data = await state.get_data()
        await state.update_data(choleric=data['choleric'] + 1)
    if callback.data == 'response_yes' and 5 < data["number_v"] <= 10:
        data = await state.get_data()
        await state.update_data(phlegmatic=data['phlegmatic'] + 1)
    if callback.data == 'response_yes' and 10 < data["number_v"] <= 15:
        data = await state.get_data()
        await state.update_data(sanguine=data['sanguine'] + 1)
    if callback.data == 'response_yes' and 15 < data["number_v"] <= 20:
        data = await state.get_data()
        await state.update_data(melancholic=data['melancholic'] + 1)
    if data['number_v'] < 5:
        await callback.message.answer(f'{block_choleric[data["number_v"]]}', reply_markup=kb_in)
    if 5 <= data["number_v"] < 10:
        await callback.message.answer(f'{block_phlegmatic[data["number_v"]]}', reply_markup=kb_in)
    if 10 <= data["number_v"] < 15:
        await callback.message.answer(f'{block_sanguine[data["number_v"]]}', reply_markup=kb_in)
    if 15 <= data["number_v"] <= 20:
        await callback.message.answer(f'{block_melancholic[data["number_v"]]}', reply_markup=kb_in)
    if data["number_v"] == 21:
        await state.finish()
        pr = data['melancholic'] + data['sanguine'] + data['phlegmatic'] + data['choleric']
        print(f'Всего положительных ответов {pr}')
        values = [x for x in data.values() if x != data['name_user'] if x != data['number_v'] if x != 0]
        keys = [x for x in data.keys() if x != 'name_user' if x != 'number_v' if data[f'{x}'] != 0]
        plt.pie(values,labels=keys)
        plt.savefig(f'{data["name_user"]}_itog.jpg')
        with open(f'{data["name_user"]}_itog.jpg', 'rb') as img:
            await callback.message.answer_photo(img)
        await callback.message.answer(f'Вы флегматик на {data["phlegmatic"] / pr * 100}%\n'
                                      f'Вы Холерик на {data["choleric"] / pr * 100}%\n'
                                      f'Вы Сангвиник на {data["sanguine"] / pr * 100}%\n'
                                      f'Вы Меланхолик на {data["melancholic"] / pr * 100}%\n')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

