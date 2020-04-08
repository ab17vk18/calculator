from django.shortcuts import render, redirect
from django.views import generic, View
from . forms import CalcForm
from django.http import Http404, HttpResponse

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "calculator/index.html"

    def get(self, request, *args, **kwargs):
        context = {'works':'success'}
        return render(request, self.template_name, context)

class CalcView(View):
    template_name = "calculator/calculator.html"

    def get(self, request):
        form = CalcForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        if request.method == 'POST':
            form = CalcForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data['a']
                b = form.cleaned_data['b']

                if a == None or b == None:
                    result = ''
                    str_rep = ''

                elif 'Addition' in request.POST:
                    result = a + b
                    str_rep = str(a) + ' + ' + str(b) + ' = '

                elif 'Subtraction' in request.POST:
                    result = a- b
                    str_rep = str(a) + ' - ' + str(b) + ' = '

                elif 'Multiplication' in request.POST:
                    result = a * b
                    str_rep = str(a) + ' * ' + str(b) + ' = '

                elif 'Division' in request.POST:
                    result = a / b
                    str_rep = str(a) + ' / ' + str(b) + ' = '

                context = {'form': CalcForm(), 'str_rep': str_rep, 'result': result}
                return render(request, self.template_name, context)

            else:
                raise Http404

        else:
            context = {'form': CalcForm(), 'result': None}
            return render(request, self.template_name, context)
