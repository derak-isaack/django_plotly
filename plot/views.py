from django.shortcuts import render
import plotly.express as px
from plot.models import Sales
from plot.forms import DateForm
from datetime import date
import csv
from django.conf import settings
import pandas as pd



def chart(request):
    total=Sales.objects.all()
    start= request.GET.get('start')
    end = request.GET.get('end')
    datafile = settings.BASE_DIR / 'Data' / 'SalesForCourse_quizz_table.csv'
    df=pd.read_csv(datafile)
   

    if start:
        total= total.filter(date__gte=start)
    if end:
        total= total.filter(date__lte=end)


    fig = px.line(
        df,
        x = "date",
        y = [t.revenue for t in total],
        title='Supermarket sales',
        labels = {'x':'date', 'y':'revenue'},
    )
    fig.update_layout(title={
        'font_size':22,
        'xanchor':'center',
        'x':0.5,
    }
    )
    chart = fig.to_html()

    context = {'chart':chart, 'form':DateForm()}
    return render(request, 'core/chart.html', context)



# Create your views here.
