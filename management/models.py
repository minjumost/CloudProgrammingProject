from django.db import models

# product 속성이 Beverage모델을 참조하면 후에 음료가 삭제됐을 때(시즌음료) 정보를 남길 수 없으므로 관계형으로 만들지 않음
class Sales(models.Model):
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    product = models.CharField(max_length=50)
    price = models.IntegerField()
