from tkinter import PanedWindow

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML
import json

# Create your views here.


def generate_pdf_view(request):


    if request.method == 'POST':
        result_str = request.POST.get('result_str', None)
        my_dict = json.loads(result_str)
        contract_number = request.POST.get('contractNumber', None)  # доступ по ключу contractNumber
        day = request.POST.get('day', None)
        month = request.POST.get('mounth', None)  # обратите внимание на опечатку в 'month'
        year = request.POST.get('year', None)
        organiz_zakaz = request.POST.get('organz_zakaz', None)
        mount_notarial = request.POST.get('mount_notarial', None)
        year_notarial = request.POST.get('year_notarial', None)
        prepaid_expense = request.POST.get('prepaid_expense', None)
        sum_prepaid_expense = request.POST.get('sum_prepaid_expense', None)
        sum_text_prepaid_expense = request.POST.get('sum_text_prepaid_expense', None)
        telephone_number_executor = request.POST.get('telephone-number-executor', None)
        email_number_executor = request.POST.get('email-number-executor', None)
        telephone_number_zac = request.POST.get('telephone-number-zac', None)
        email_number_zac = request.POST.get('email_number_zac', None)
        name_face_executor = request.POST.get('name_face_executor', None)
        telephone_face_executor = request.POST.get('telephone-face_executor', None)
        email_face_executor = request.POST.get('email-face_executor', None)
        post_organz_zac = request.POST.get('post_organz_zac', None)

        # Так как 'name_organz_zac' и другие поля имеют массивы значений, используем метод getlist
        name_organz_zac = request.POST.getlist('name_organz_zac')
        face_organz_zac = request.POST.getlist('face_organz_zac')
        number_notarial = request.POST.get('number_notarial', None)
        day_notarial = request.POST.get('day_notarial', None)
        html_template = render_to_string('templateapp/provision-of-services-edit.html', {
            "contract_number":contract_number,
            "day":day,
            "month":month,
            "year":year,
            "organiz_zakaz":organiz_zakaz,
            "name_organz_zac" : name_organz_zac,
            "face_organz_zac" : face_organz_zac,
            "number_notarial" : number_notarial,
            "day_notarial" : day_notarial,
            "mount_notarial" : mount_notarial,
            "year_notarial" : year_notarial,
            "prepaid_expense": prepaid_expense,
            "sum_prepaid_expense": sum_prepaid_expense,
            "sum_text_prepaid_expense": sum_text_prepaid_expense,
            "telephone_number_executor": telephone_number_executor,
            "email_number_executor" : email_number_executor,
            "telephone_number_zac" : telephone_number_zac,
            "email_number_zac": email_number_zac,
            "name_face_executor": name_face_executor,
            "telephone_face_executor": telephone_face_executor,
            "email_face_executor": email_face_executor,
            "post_organz_zac" : post_organz_zac ,
            "result_str": result_str,
            "zakaz_email": my_dict.get('zakaz_email'),
            "zakaz_fio":  my_dict.get('zakaz_fio'),

        })

        html = HTML(string=html_template)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="template.pdf"'

        return response

    elif request.method == 'GET':

        html_template = render_to_string('templateapp/provision-of-services-edit.html')
        html = HTML(string=html_template)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="template.pdf"'
        return response



