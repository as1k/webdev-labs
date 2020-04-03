from django.urls import path
from api.views import get_all_companies, get_company, get_vacancy, get_all_vacancies, get_vacancies_by_company, \
    get_top_ten

urlpatterns = [
    path('companies/', get_all_companies),
    path('companies/<int:company_id>/', get_company),
    path('companies/<int:company_id>/vacancies/', get_vacancies_by_company),
    path('vacancies/', get_all_vacancies),
    path('vacancies/<int:vacancy_id>/', get_vacancy),
    path('vacancies/top_ten/', get_top_ten),
]