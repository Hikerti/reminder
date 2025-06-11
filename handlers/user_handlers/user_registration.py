from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()

class RegistrationState(StatesGroup):
    name_user = State()
    surname_user = State()
    age_user = State()
    login_user = State()
    password_user = State()

@router.message(Command(commands='registration'))
async def user_registration(message: Message, state: FSMContext):
    await state.set_state(RegistrationState.name_user)
    await message.answer('Привет! \n\nВведи данные пользователя, нажми далее, чтобы продолжить регистрацию');

@router.message(RegistrationState.name_user)
async def create_name_user(message: Message, state: FSMContext): 
    if len(message.text) < 2:
        await message.answer('Имя слишком короткое введите корректный текст')
        return
    
    await state.update_data(name_user=message.text, username=message.from_user.username, tg_id=message.from_user.id)
    await state.set_state(RegistrationState.surname_user)
    await message.answer('Имя введено правильно, введите фамилию')

@router.message(RegistrationState.surname_user)
async def create_surname_user(message: Message, state: FSMContext):
    if len(message.text) < 2:
        await message.answer('Фамилия слишком короткое введите корректный текст')
        return
    
    await state.update_data(surname_user=message.text)
    await state.set_state(RegistrationState.age_user)
    await message.answer('Фамилия введено правильно, введите возрост');

@router.message(RegistrationState.age_user)
async def create_age_user(message: Message, state: FSMContext):
    if (message.text.isdigit() == False):
        await message.answer('Введите корректный возрост!\n\nВозрост должен быть угазан только цифрами')
        return
    
    if (int(message.text) < 12 or int(message.text) > 100):
        await message.answer('Введите корректный возрост!\n\nВозрост пользователя не может быть меньше 12 и не больше 100')
        return;

    age = int(message.text)
    
    await state.update_data(age_user=age)
    await state.set_state(RegistrationState.login_user)
    await message.answer('Возрост введено правильно, введите логин');

@router.message(RegistrationState.login_user)
async def create_login_user(message: Message, state: FSMContext):
    if (len(message.text) < 6):
        await message.answer('Данное поле должно быть длинной более 6 символов.') 
    
    await state.update_data(login_user=message.text)
    await state.set_state(RegistrationState.password_user)
    await message.answer('Логин введено правильно, введите пароль');

@router.message(RegistrationState.password_user)
async def create_password_user(message: Message, state: FSMContext):
    if len(message.text) < 8:
        await message.answer('Фамилия слишком короткое введите корректный текст')
        return
    
    await state.update_data(password_user=message.text)
    
    data = await state.get_data()
    text = (
        f"Проверьте введённые данные:\n\n"
        f"👤 Имя: {data['name_user']}\n"
        f"👥 Фамилия: {data['surname_user']}\n"
        f"🎂 Возраст: {data['age_user']}\n"
        f"🔐 Логин: {data['login_user']}\n"
        f"🛡️ Пароль: {'*' * len(data['password_user'])}\n\n"
        "Вы подтверждаете регистрацию?"
    )

    keybords = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Отправить', callback_data='confirm_registration')],
        [InlineKeyboardButton(text='Отмена', callback_data='cancel_registration')]
    ])

    await message.answer(text, reply_markup=keybords)

@router.callback_query(lambda c: c.data in ['confirm_registration', 'cancel_registration'])
async def process_callback_registration(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'confirm_registration':
        data = await state.get_data()

        await callback.message.edit_text(f'Регистрация прошла успешно! {data}')
        
    else: 
        await callback.message.edit_text('Регистрация отменена')
    
    await state.clear
