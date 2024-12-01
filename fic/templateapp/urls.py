
from django.urls import path, include


from .views import (Dashboard, DogovorAB, DogovorVozmezdie,
                    test_celery,
                    work_provision_edit, work_provision_fill,change_action)

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('dogovor_ab/', DogovorAB.as_view(), name='dogovor_ab'),
    path('dogovor_uslugi/', DogovorVozmezdie.as_view(), name='dogovor_uslugi'),

    path('api_test/', test_celery, name="start_filling"),
    path('provision-service-edit/',work_provision_edit, name='provision-service-edit'),
    path('provision-service-fill/',work_provision_fill, name='provision-service-fill'),
    path('change-action/',change_action, name='change-action'),
]

