
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from gigachat import GigaChat
from templateapp.utils import make_dict
import datetime
import json


load_dotenv()




def AIRequest(zakaz_user, ispolnitel_user):
    TOKEN_GIGACHAT = os.getenv("TOKEN_GIGACHAT")
    current_date = datetime.date.today().strftime("%d.%m.%Y")
    adapter = {
        "dogovor.номер договора": "dogovor_number",
        "dogovor.дата договора": "dogovor_data",
        "dogovor.сумма": "summa",
        "dogovor.аванс %": "avans_procent",
        "dogovor.аванс сумма": "avans_summa",
        "dogovor.окончательный расчёт %": "postavans_procent",
        "dogovor.окончательный расчёт сумма число": "postavans_cifra",
        "dogovor.окончательный расчёт сумма буквенный": "postavans_bukva",
        "zakaz.компания": "zakaz_company",
        "zakaz.фио полное": "zakaz_fio_full",
        "zakaz.фио краткое": "zakaz_fio",
        "zakaz.основание": "zakaz_osnovaie",
        "zakaz.телефон": "zakaz_telefon",
        "zakaz.почта": "zakaz_email",
        "zakaz.должность": "zakaz_post",
        "ispolnitel.компания": "ispolnitel_company",
        "ispolnitel.фио полное": "ispolnitel_fio_full",
        "ispolnitel.фио краткое": "ispolnitel_fio",
        "ispolnitel.основание": "ispolnitel_osnovaie",
        "ispolnitel.телефон": "ispolnitel_telefon",
        "ispolnitel.почта": "ispolnitel_email",
        "ispolnitel.должность": "ispolnitel_post",
    }

    dogovor = {"номер договора": "", "дата договора": "", "сумма": "", "аванс %": "", "аванс сумма": "",
               "окончательный расчёт %": "", "окончательный расчёт сумма число": "",
               "окончательный расчёт сумма буквенный": ""}
    zakaz = {"компания": "", "фио полное": "", "фио краткое": "", "основание": "", "телефон": "",
             "почта": "", "должность": ""}
    ispolnitel = {"компания": "", "фио полное": "", "фио краткое": "", "основание": "", "телефон": "",
                  "почта": "", "должность": ""}

    promt = f"""Выступи в роли помощника по заполнению python-словарей "данные_договора", "данные_заказчика", "данные_исполнителя".
        1. На основе предоставленного текста пользователя извлеки необходимые данные из этого текста и вставь их в указанные словари json в соответствующие поля.
           Если значение для поля не найдено, то значение поля оставь пустым, а ключ оставь.
           Имена словарей должный быть такими:
           "данные_договора" = тут данные_договора,
           "данные_заказчика" = тут данные_заказчика,
           "данные_исполнителя" = тут данные_исполнителя
           Покажи словари данные_договора, данные_заказчика, данные_исполнителя с заполнеными пользовательскими данными.
        2. 'номер договора' может писаться как №договора, договор №.
           в 'фио полное' определи фамилию, имя и отчество.
           'фио краткое' делается из 'фио полное' так - сначала полностью пишется фамилия, потом первая буква имени, потом первая буква отчества.
           например Иванов Николай Егорович = Иванов.Н.Е., Николай Егорович Иванов = Иванов.Н.Е.
           в почте убери пробелы.
           определи в тексте дату и преобразуй её в формат типа дд.мм.ггг.
           там,где необходимо число напиши словами. например 30000 = тридцать тысяч
           если аванс казан в %, пересчитай его в число и вставь в соответсвующее поле. например,  сумма = 100 аванс =20%, тогда аванс число = 20
           определи окончательный расчёт. окончательный расчёт = сумма - аванс. например, сумма = 300, аванс число = 100, тогда окончательный расчёт = 200
        3. Сегодняшняя дата = {current_date}.
        4. **python-словари json**
           данные договора "данные_договора" = {dogovor}
           данные заказчика "данные_заказчика" = {zakaz}
           данные исполнителя "данные_исполнителя" = {ispolnitel}
        5. **Пользовательский ввод**
           "данные заказчика" = {zakaz_user}
           "данные исполнителя" = {ispolnitel_user}
           данные договора либо в данных заказчика, либо в данных исполнителя.

        """

    with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
        response = giga.chat(promt)
        resp = response.choices[0].message.content
        zakaz = make_dict(resp, "data_customer")
        ispolnitel = make_dict(resp, "data_performer")
        dogovor = make_dict(resp, "data_contract")

        if len(zakaz) == 0:
            zakaz = make_dict(resp, "данные_заказчика")
        if len(ispolnitel) == 0:
            ispolnitel = make_dict(resp, "данные_исполнителя")
        if len(dogovor) == 0:
            dogovor = make_dict(resp, "данные_договора")
        result = {}
        for key,value in dogovor.items():
            v = value.strip()
            try:
                date = datetime.datetime.strptime(v, "%d.%m.%Y").date()
                result[adapter.get(f'dogovor.{key}')] = date
                result[adapter.get(f'dogovor.{key}_day')] = date.day
                result[adapter.get(f'dogovor.{key}_month')] = date.month
                result[adapter.get(f'dogovor.{key}_year')] = date.year
            except Exception as e:
                if re.match("^\d+?\.\d+?$", v) is None and (len(v)==9 or len(v)==11 or len(v)==13):
                    result[adapter.get(f'dogovor.{key}')] = f'0{v}'
                else:
                    result[adapter.get(f'dogovor.{key}')] = v
        for key,value in zakaz.items():
            v = value.strip()
            try:
                date = datetime.datetime.strptime(v, "%d.%m.%Y").date()
                result[adapter.get(f'zakaz.{key}')] = date
                result[adapter.get(f'zakaz.{key}_day')] = date.day
                result[adapter.get(f'zakaz.{key}_month')] = date.month
                result[adapter.get(f'zakaz.{key}_year')] = date.year
            except Exception as e:
                if re.match("^\d+?\.\d+?$", v) is None and (len(v)==9 or len(v)==11 or len(v)==13):
                    result[adapter.get(f'zakaz.{key}')] = f'0{v}'
                else:
                    result[adapter.get(f'zakaz.{key}')] = v
        for key,value in ispolnitel.items():
            v = value.strip()
            try:
                date = datetime.datetime.strptime(v, "%d.%m.%Y").date()
                result[adapter.get(f'ispolnitel.{key}')] = date
                result[adapter.get(f'ispolnitel.{key}_day')] = date.day
                result[adapter.get(f'ispolnitel.{key}_month')] = date.month
                result[adapter.get(f'ispolnitel.{key}_year')] = date.year
            except Exception as e:
                if re.match("^\d+?\.\d+?$", v) is None and (len(v)==9 or len(v)==11 or len(v)==13):
                    result[adapter.get(f'ispolnitel.{key}')] = f'0{v}'
                else:
                    result[adapter.get(f'ispolnitel.{key}')] = v
        print(result)
        return result



