from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views.crud import company_list, company_detail, vacancy_detail, vacancy_list, company_vacancies
from api.views.crud import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
from api.views.fbv import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail
from api.views.cbv import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails

# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('companies/', company_list),
#     path('companies/<int:company_id>/', company_detail),
#     path('vacancies/', vacancy_list),
#     path('vacancies/<int:vacancy_id>', vacancy_detail),
#     path('companies/<int:company_id>/vacancies/', company_vacancies)
# ]

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetails.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view())
]

