
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from gigachat import GigaChat
from templateapp.utils import make_dict
import datetime
import json


load_dotenv()

current_date = datetime.date.today().strftime("%d.%m.%Y")


def AIRequest(query):
    TOKEN_GIGACHAT = os.getenv("TOKEN_GIGACHAT")
    adapter = {
        "Номер договора": "dogovor_number",
        "Дата договора": "dogovor_data",
        # "Дата договора": "dogovor_data_day",
        # "Дата договора": "dogovor_data_month",
        # "Дата договора": "dogovor_data_year",
        "Фамилия Имя Отчество": "name",
        "Должность": "post",
        "Компания": "company",
        "Основание": "osnovanie",
        "Юридический адрес": "adres_jurist",
        "Почтовый адрес": "adres_postale",
        "ИНН": "inn",
        "КПП": "kpp",
        "ОГРН": "ogrn",
        "Расчетный счёт": "current_account",
        "Почта": "email",
    }

    template = {
        "Номер договора": "",
        "Дата договора": "",
        "Фамилия Имя Отчество": "",
        "Должность": "",
        "Компания": "",
        "Основание": "",
        "Юридический адрес": "",
        "Почтовый адрес": "",
        "ИНН": "",
        "КПП": "",
        "ОГРН": "",
        "Расчетный счёт": "",
        "Почта": "",
    }

    promt = f"""
    Выступи в роли помощника по заполнению destination {template}. 
    1. есть source {query}
    2. В source дата может быть в любом формате. например, 21 февраля 2000 года, 02-11-2021г
       Ввыяви дату, переведи её к виду дд.мм.гггг и вставь в Дата договора
    3. Если в source только 1 адрес, то вставь его и Юридический адрес, и в Почтовый адрес. 
       если в source 2 адреса, то определи, какой из них относится к Юридический адрес, а какой к Почтовый адрес.
    4. ИНН содержит только цифры. ИНН может содержать 10,12 или 14 цифр. если ИНН 9, 11 или 13 цифр, то к ИНН добавь 0
       например 123456789 должно выглядеть как 0123456789
    5. КПП содержит только цифры. КПП содержит 9 цифр. если КПП 8 цифр, то к КПП добавь 0
       например 12345678 должно выглядеть как 012345678
    6. Почта - это email. если в email есть пробелы, то убери их.
       например, dfsf @ grts .tr должно стать dfsf@grts.tr
    7. Заполни значения в словаре destination данными из source. значение должно соответствовать смыслу ключа. и покажи этот destination
    """

    with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
        response = giga.chat(promt)
        resp = response.choices[0].message.content
        destination = make_dict(resp, "destination")
        result = {}
        for key,value in destination.items():
            v = value.strip()
            try:
                date = datetime.datetime.strptime(v, "%d.%m.%Y").date()
                result[adapter.get(key)] = date
                result[f'{adapter.get(key)}_day'] = date.day
                result[f'{adapter.get(key)}_month'] = date.month
                result[f'{adapter.get(key)}_year'] = date.year
            except Exception as e:
                if re.match("^\d+?\.\d+?$", v) is None and (len(v)==9 or len(v)==11 or len(v)==13):
                    result[adapter.get(key)] = f'0{v}'
                else:
                    result[adapter.get(key)] = v
        #print(result)
        return result




