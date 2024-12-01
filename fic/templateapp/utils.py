from gigachat import GigaChat
import datetime
import json


def make_dict(result, name):
    try:
        start = result.find(name)
        step1 = result[start:]
        start = step1.find('{')
        step2 = step1[start:]
        start = step2.find('}')
        step3 = step2[:start + 1]
        dic = json.loads(step3)
    except Exception as e:
        dic = {}
    return dic


# def AIRequest(zakaz_user1, ispolnitel_user1):
#     TOKEN_GIGACHAT = 'NTViNzk2ZTYtM2M1Mi00MGQxLWI4MGUtOTMwMjhhNGZhMDVhOjA3NTMwZWRiLWU0MDktNDFmZS04MzNiLWEyY2U1OTgxNDhlMg=='
#
#     dogovor = {"номер договора": "", "дата договора": "", "сумма": "", "аванс %": "", "аванс сумма": "",
#                "окончательный расчёт %": "", "окончательный расчёт сумма число": "", "окончательный расчёт сумма буквенный": ""}
#     zakaz = {"компания": "", "фио полное": "", "фио краткое": "", "основание": "", "телефон": "", "почта": "", "должность": ""}
#     ispolnitel = {"компания": "", "фио полное": "", "фио краткое": "", "основание": "", "телефон": "", "почта": "", "должность": ""}
#
#     # print(zakaz_user1)
#     # print(ispolnitel_user1)
#     zakaz_user = zakaz_user1
#     ispolnitel_user = ispolnitel_user1
#
#     with GigaChat(credentials=TOKEN_GIGACHAT, scope="GIGACHAT_API_PERS", verify_ssl_certs=False) as giga:
#         current_date = datetime.date.today().strftime("%d.%m.%Y")
#         tekst = f"""Выступи в роли помощника по заполнению python-словарей "данные_договора", "данные_заказчика", "данные_исполнителя".
#         1. На основе предоставленного текста пользователя извлеки необходимые данные из этого текста и вставь их в указанные словари json в соответствующие поля.
#            Если значение для поля не найдено, то значение поля оставь пустым, а ключ оставь.
#            Имена словарей должный быть такими:
#            "данные_договора" = тут данные_договора,
#            "данные_заказчика" = тут данные_заказчика,
#            "данные_исполнителя" = тут данные_исполнителя
#            Покажи словари данные_договора, данные_заказчика, данные_исполнителя с заполнеными пользовательскими данными.
#         2. 'номер договора' может писаться как №договора, договор №.
#            в 'фио полное' определи фамилию, имя и отчество.
#            'фио краткое' делается из 'фио полное' так - сначала полностью пишется фамилия, потом первая буква имени, потом первая буква отчества.
#            например Иванов Николай Егорович = Иванов.Н.Е., Николай Егорович Иванов = Иванов.Н.Е.
#            в почте убери пробелы.
#            определи в тексте дату и преобразуй её в формат типа дд.мм.ггг.
#            там,где необходимо число напиши словами. например 30000 = тридцать тысяч
#            если аванс казан в %, пересчитай его в число и вставь в соответсвующее поле. например,  сумма = 100 аванс =20%, тогда аванс число = 20
#            определи окончательный расчёт. окончательный расчёт = сумма - аванс. например, сумма = 300, аванс число = 100, тогда окончательный расчёт = 200
#         3. Сегодняшняя дата = {current_date}.
#         4. **python-словари json**
#            данные договора "данные_договора" = {dogovor}
#            данные заказчика "данные_заказчика" = {zakaz}
#            данные исполнителя "данные_исполнителя" = {ispolnitel}
#         5. **Пользовательский ввод**
#            "данные заказчика" = {zakaz_user}
#            "данные исполнителя" = {ispolnitel_user}
#            данные договора либо в данных заказчика, либо в данных исполнителя.
#
#         """
#         response = giga.chat(tekst)
#         resp = response.choices[0].message.content
#         print(resp)
#         zakaz = make_dict(resp, "data_customer")
#         ispolnitel = make_dict(resp, "data_performer")
#         dogovor = make_dict(resp, "data_contract")
#
#         # zakaz = make_dict(resp, "данные_заказчика")
#         # ispolnitel = make_dict(resp, "данные_исполнителя")
#         # dogovor = make_dict(resp, "данные_договора")
#         #
#         if len(zakaz)==0:
#             zakaz = make_dict(resp, "данные_заказчика")
#         if len(ispolnitel)==0:
#             ispolnitel = make_dict(resp, "данные_исполнителя")
#         if len(dogovor)==0:
#             dogovor = make_dict(resp, "данные_договора")
#
#         #data_contract data_customer data_performer
#         result = {
#             "dogovor": dogovor,
#             "zakaz": zakaz,
#             "ispolnitel": ispolnitel
#         }
#         print('result  ',result)
#         return result
#
#
#

