from .models import add
from rest_framework .viewsets import ModelViewSet
from .serializers import data
# Create your views here.
class check(ModelViewSet):
    model=add
    queryset=add.objects.all()
    permission_classes=()
    serializer_class=data