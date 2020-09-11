# django-tutorial

## 開發環境

參考文章(https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c)

安裝 Django

      pip3 install django
      
測試Django是否安裝

      python3 -m django --version
      
建立資料夾

      mkdir mysite
      cd mysite
      
初始化專案
  
      django-admin startproject mysite
      
啟動服務

      cd mysite
      python manage.py runserver 


## 處理請求

參考文章(https://bezkoder.com/django-rest-api/)

參考文章(https://docs.djangoproject.com/en/3.1/topics/http/urls/)

基本寫法

```python
      path('api/tutorials/', views.fristAPI)
      ## 使用api_view設定請求http方式
      @api_view(['GET', 'POST'])
      def fristAPI(request):
            return JsonResponse({'Msg': 'Your use method ' + request.method})
```    
            
URL參數寫法

```python
      ## 使用<型態:參數key>設定URL參數
      path('api/tutorials/<str:name>/', views.getPathParam)
      @api_view(['GET', 'POST'])
      def getPathParam(request, *args, **kwargs):
            ## 透過kwargs[參數key]取得URL參數
            return JsonResponse({'Msg': 'Your request parameter ' + kwargs['name']})
```          
            
## 建立Models

在model

```python
class Employee(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, blank=True)
    email_id = models.CharField(max_length=256)
    phone_num = models.CharField(max_length=16)
    employee_gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    employee_address = models.TextField()
    employee_job = models.ManyToManyField('AvailableJobs', blank=1)
    date_f_birth = models.DateField()


class AvailableJobs(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
```

執行下列指令

      python manage.py makemigrations
      python manage.py showmigrations
      python manage.py migrate
      
建立管理員帳號

      python manage.py createsuperuser
      
SQLite Tools(https://sqlitebrowser.org/dl/)

## 執行結果

      python manage.py runserver

http://127.0.0.1:8000/employee/all

![Display all employees](https://github.com/Shon0221/django-tutorial/blob/master/image/all.jpg)


http://127.0.0.1:8000/employee/detail/2

![Display employee detail](https://github.com/Shon0221/django-tutorial/blob/master/image/detail.jpg)
