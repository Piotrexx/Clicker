from django.db.models import Q
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserModelSerializer, PlanetModelSerializer
from .models import User, Planet
from rest_framework.response import Response
from django.db.utils import IntegrityError
from rest_framework.status import HTTP_403_FORBIDDEN,HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, \
    HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND

class ClickerViewSet(GenericViewSet):
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except IntegrityError:
            return Response("Użytkownik o takim numerze telefony lub emailu już istnieje", status=HTTP_403_FORBIDDEN)

        return Response(serializer.data, status=HTTP_201_CREATED)

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def leadboard(self, request):
        return Response(self.serializer_class(User.objects.all()).data, status=HTTP_200_OK)

    @action(detail=False, methods=['patch'])
    def buy_upgrade(self, request):
        price = request.user.ship_upgrade * 1000
        if request.user.money < price:
            return Response("Nie stać cię na kupno ulepszenia statku", status=HTTP_403_FORBIDDEN)
        
        request.user.ship_upgrade += 1
        request.user.money -= price
        request.user.save()

        return Response("Pomyślnie kupiono ulepszenie", status=HTTP_200_OK)
