import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from zoo_shop_app.models import Client, Sales
from django.db.models import Sum


def sales_chart(request):
    clients = Client.objects.all()

    client_sales = {}
    for client in clients:
        sales_total = Sales.objects.filter(client=client).aggregate(total_sales=Sum('total_cost'))['total_sales']
        client_sales[client.name] = sales_total or 0

    client_names = list(client_sales.keys())
    sales_values = list(client_sales.values())

    plt.figure(figsize=(10, 6))
    plt.bar(client_names, sales_values)
    plt.xlabel('Clients')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Client')
    plt.xticks(rotation=45)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    context = {
        'graph': graph,
        'client_sales': client_sales
    }

    return render(request, 'sales_chart.html', context)
