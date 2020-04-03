from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300, default='Any company')
    description = models.TextField(default='Any description')
    city = models.CharField(max_length=300, default='Any city')
    address = models.TextField(default='Somewhere in the world')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=300, default='Any vacancy')
    description = models.TextField(default='Any description')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }