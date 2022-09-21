from rest_framework.viewsets import GenericViewSet, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.collisions.api.serializers import *


class CollisionsForDayViewSet(generics.ListAPIView):
    """
        Accidentes por fecha, Formato de consulta: /collision/collisions_for_day/01%2F01%2F2015/  para fecha 01/01/2015 en script
    """
    serializer_class = CollisionSerializer

    def get_queryset(self, fecha=None):
        if fecha:
            try:
                collision_crashes = self.get_serializer().Meta.model.objects.filter(crash_date=fecha)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return collision_crashes

    def list(self, request, fecha):
        collisions_crashes = self.get_queryset(fecha)
        data = self.get_serializer(collisions_crashes, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class CollisionsForBoroYearViewSet(generics.ListAPIView):
    """
        Accidentes por barrio y año
    """
    serializer_class = CollisionSerializer

    def get_queryset(self, boro=None, year=None):
        if boro and year:
            try:
                collision_crashes = self.get_serializer().Meta.model.objects.filter(borough=boro, year=year)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return collision_crashes

    def list(self, request, boro, year):
        collisions_crashes = self.get_queryset(boro, year)
        data = self.get_serializer(collisions_crashes, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class CollisionsForBoroYearMonthViewSet(generics.ListAPIView):
    """
        Accidentes por barrio, año y mes
    """
    serializer_class = CollisionSerializer

    def get_queryset(self, boro=None, year=None, month=None):
        if boro and year and month:
            try:
                collision_crashes = self.get_serializer().Meta.model.objects.filter(borough=boro, year=year, month=month)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return collision_crashes

    def list(self, request, boro, year, month):
        collisions_crashes = self.get_queryset(boro, year, month)
        data = self.get_serializer(collisions_crashes, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class TimeCrashPercViewSet(generics.ListAPIView):
    """
        Accidentes por hora total dataset
    """
    serializer_class = TimeCrashPercSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class ZoneCrashViewSet(generics.ListAPIView):
    """
        Accidentes por zona total dataset
    """
    serializer_class = ZoneCrashSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class PublicDamageViewSet(generics.ListAPIView):
    """
        Cantidad de daños a propiedad pública
    """
    serializer_class = PublicDamageSerializer

    def get_queryset(self, year=None):
        if year:
            try:
                queryset = self.get_serializer().Meta.model.objects.filter(year=year)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return queryset

    def list(self, request, year):
        queryset = self.get_queryset(year)
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class LicenceStatesViewSet(generics.ListAPIView):
    """
        Accidentes asociados a cada estado que otorga la licencia
    """
    serializer_class = LicenceStateSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class FactorBySexViewSet(generics.ListAPIView):
    """
        Accidentes asociados por género
    """
    serializer_class = FactorBySexSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class DataMonthlyByTypeViewSet(generics.ListAPIView):
    """
        Accidentes asociados por tipo
    """
    serializer_class = DataMonthlyByTypeSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class DataMonthlyByStatusViewSet(generics.ListAPIView):
    """
        Estado de personas accidentadas
    """
    serializer_class = DataMonthlyByStatusSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class DataMonthlyBySexViewSet(generics.ListAPIView):
    """

    """
    serializer_class = DataMonthlyBySexSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class DataMonthlyByInjuryViewSet(generics.ListAPIView):
    """
        Tipo de lesiones
    """
    serializer_class = DataMonthlyByInjurySerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class YearMonthCrashCountViewSet(generics.ListAPIView):
    """
        Cantidad de accidentes por año
    """
    serializer_class = YearMonthCrashCountSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class DayCrashPercViewSet(generics.ListAPIView):
    """
        Porcentaje de accidentes por día
    """
    serializer_class = DayCrashPercSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)


class LicenceViewSet(generics.ListAPIView):
    """
        Licencias por estado
    """
    serializer_class = LicenceSerializer

    def get_queryset(self):
        try:
            queryset = self.get_serializer().Meta.model.objects.all()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset, many=True).data
        return Response({'data': data}, status=status.HTTP_200_OK)
