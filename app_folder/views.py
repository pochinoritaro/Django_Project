from django.shortcuts import render
from django.views import View
from .models import SampleDB


class SampleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/page01.html')

    def post(self, request, *args, **kwargs):
        input_data = request.POST['input_data']
        result = SampleDB.objects.filter(sample1=input_data)
        result_sample1 = result[0].sample1
        result_sample2 = result[0].sample2
        context = {'result_sample1': result_sample1,
                   'result_sample2': result_sample2}
        return render(request, 'app_folder/page02.html', context=context,)


top_page = SampleView.as_view()
