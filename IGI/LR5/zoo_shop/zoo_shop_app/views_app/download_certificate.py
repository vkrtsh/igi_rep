from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


def download_certificate(request):
    html_string = render_to_string('certificate.html', {})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'

    HTML(string=html_string).write_pdf(response)

    return response
