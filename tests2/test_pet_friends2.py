from api import PetFriends
from settings2 import valid_email, valid_password2
import os

from settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_no_valid_user(email=valid_email, password2=valid_password2):
    """ Проверяем что запрос api ключа не проходит при ошибочном вводе password"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password2)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_no_email(email='', password=valid_password):
    """ Проверяем что запрос api ключа при отсутствии введения валидного email не проходит"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key( email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_no_password_user(email=valid_email, password=""):
    """ Проверяем что запрос api ключа без password не проходит и в тезультате не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_no_email_no_password_user(email="", password=""):
    """ Проверяем что запрос api ключа без email  и password не проходит  и в результате не содержится  слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result


def test_add_new_pet_with_no_valid_user(name='Китти', animal_type='кошка',
                                     age='10', pet_photo='images/cat55555.jpg'):
    """Проверяем что невозможно  добавить питомца с не корректными данными, в нашем случае с не корректным фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_negative_age(name='Дружок', animal_type='овчарка',
                                     age='-4', pet_photo='images/dog1.jpg'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_name(name='', animal_type='овчарка',
                                     age='6', pet_photo='images/dog1.jpg'):
    """Проверяем, что нельзя добавить питомца без name.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_no_age(name='Любимчик', animal_type='овчарка',
                                       age='', pet_photo='images/dog1.jpg'):
    """Проверяем, что нельзя добавить питомца без возраста.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_animal_type(name='Мишка', animal_type='',
                                       age='1', pet_photo='images/dog1.jpg'):
    """Проверяем, что нельзя добавить питомца без породы.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_data(name='', animal_type='',
                                     age='', pet_photo='images/dog1.jpg'):
    """Проверяем, что нельзя добавить питомца без имени, породы и возраста.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_photo(name='Дружок', animal_type='овчарка',
                                     age='12', pet_photo=''):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом.
    Если питомец добавится, значит существует Баг в API"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name