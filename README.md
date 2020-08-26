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

參考文章(https://docs.djangoproject.com/en/3.1/topics/http/urls/)

基本寫法

      path('api/tutorials/', views.fristAPI)
      ## 使用api_view設定請求http方式
      @api_view(['GET', 'POST'])
      def fristAPI(request):
            return JsonResponse({'Msg': 'Your use method ' + request.method})
            
            
UR參數寫法

      ## 使用<型態:參數key>設定URL參數
      path('api/tutorials/<str:name>/', views.getPathParam)
      @api_view(['GET', 'POST'])
      def getPathParam(request, *args, **kwargs):
            ## 透過kwargs[參數key]取得URL參數
            return JsonResponse({'Msg': 'Your request parameter ' + kwargs['name']})
