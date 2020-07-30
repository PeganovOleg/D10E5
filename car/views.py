from django.shortcuts import render

from django.db.models import Q
from django.views.generic import TemplateView

from car.models import Car


class CarsView(TemplateView):
    template_name = "index.html"
    

    def get_context_data(self, **kwargs):
        query=Q()
        count2 = Car.objects.all().count()
        x=[]
        for key2 in range(count2):
            #key3=key2+1
            k=Car.objects.get(pk=key2+1)
            x.append(k)
           # print(x)
 
        params = self.request.GET
        print(params)
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                sch=1
                query &= Q(**{key: value})
                
        
        return ({"cars": x,"cars1": Car.objects.filter(query),"cars3": query})

       



   


