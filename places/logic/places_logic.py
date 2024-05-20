from ..models import Place

def get_places():
    queryset = Place.objects.all()
    return (queryset)

def create_place(form):
    measurement = form.save()
    measurement.save()
    return ()