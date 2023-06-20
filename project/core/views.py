from django.http import HttpResponse


def home(request):
    raise ValueError()
    return HttpResponse('<html><body><h1>First app django</h1><p>A palavra paciência procede do latim pati, que significa padecer. A virtude da paciência é, de fato, “a arte de padecer”. Quando está vitalizada pela graça do Espírito Santo, pode-se definir como “a arte se sofrer com fé, esperança e amor”, sobretudo com amor.</p></body></html>', content_type='text/html')
