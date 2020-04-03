from api.models import Company, Vacancy

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_all_companies(request):
    if request.method == 'GET':
        try:
            companies = Company.objects.all()
            companies_json = [c.to_json() for c in companies]
            return JsonResponse(companies_json, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        return JsonResponse({'data': 'company post request'})
    elif request.method == 'PUT':
        return JsonResponse({'data': 'company put request'})
    elif request.method == 'PATCH':
        return JsonResponse({'data': 'company patch request'})
    elif request.method == 'DELETE':
        return JsonResponse({'data': 'company delete request'})


@csrf_exempt
def get_company(request, company_id):
    if request.method == 'GET':
        try:
            company = Company.objects.get(id=company_id)
            return JsonResponse(company.to_json())
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


@csrf_exempt
def get_all_vacancies(request):
    if request.method == 'GET':
        try:
            vacancies = Vacancy.objects.all()
            vacancies_json = [v.to_json() for v in vacancies]
            return JsonResponse(vacancies_json, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        pass


@csrf_exempt
def get_vacancy(request, vacancy_id):
    if request.method == 'GET':
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
            return JsonResponse(vacancy.to_json())
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        pass


@csrf_exempt
def get_vacancies_by_company(request, company_id):
    if request.method == 'GET':
        try:
            # company = Company.objects.get(id=company_id)
            # vacancies = company.vacancies.all()
            vacancies = Vacancy.objects.filter(company_id=company_id)
            vacancies_json = [v.to_json() for v in vacancies]
            return JsonResponse(vacancies_json, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        pass


@csrf_exempt
def get_top_ten(request):
    if request.method == 'GET':
        try:
            vacancies = Vacancy.objects.all().order_by('-salary')
            vacancies_json = [v.to_json() for v in vacancies[:10]]
            return JsonResponse(vacancies_json, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'POST':
        pass