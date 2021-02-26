from rest_framework import serializers
from .models import Configuracion
from .models import Perfil

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ('dolares_por_kilometros','valor_comida','direccion_fija',
        'no_comidas_por_semana','no_de_comida_por_dia')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ('nombre','peso_inicio','peso_meta','id_cliente')

