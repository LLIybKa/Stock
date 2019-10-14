from django.db import models

# Create your models here.

class categorya(models.Model):
  category_name = models.CharField(max_length=200)
  
  def __str__(self):
  	return self.category_name

class employee(models.Model):
  kod_sotrudnika = models.IntegerField()
  sotrudnik_name = models.CharField( max_length=200)
  sotrudnik_lastname = models.CharField(max_length=200)
  position = models.CharField(max_length=200)
  adres = models.CharField(max_length=200)

  def __str__(self):
  	return self.sotrudnik_name

class postavka(models.Model):
  kod_postavki = models.IntegerField()
  postavshik_name = models.CharField(max_length=200)
  adres = models.CharField(max_length=200)
  telephone = models.IntegerField()

  def __str__(self):
  	return self.postavshik_name

class sklad_item(models.Model):
  item = models.CharField(max_length=200)
  col_vo_sklad = models.IntegerField()
  price = models.FloatField()
  stock = models.IntegerField()
  category = models.ForeignKey(categorya, on_delete = models.CASCADE)
  employee = models.ForeignKey(employee, on_delete = models.CASCADE)
  postavka = models.ForeignKey(postavka, on_delete = models.CASCADE)

  def __str__(self):
  	return self.item