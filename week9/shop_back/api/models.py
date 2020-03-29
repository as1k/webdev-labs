from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category = models.IntegerField()

    def to_json(self):
        return {
            'id':self.id,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'category':self.category
        }

class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name
        }