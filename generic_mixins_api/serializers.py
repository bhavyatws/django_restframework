from rest_framework import serializers
from api.models import Student
#Validators
def starts_with_r(value):
    if value[0].lower()!='r':
        raise serializers.ValidationError('Name must be start with r')

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()#by default id it will not so passing explicitly
    name=serializers.CharField(max_length=100,validators=([starts_with_r]))
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    #Field Level Validation
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value
    #Object Level Validation
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=="rohit" and ct.lower()!="ranchi":
            raise serializers.ValidationError('City must be ranchi')
        return data

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.roll)
        instance.roll=validated_data.get('roll',instance.roll)
        print(instance.city)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

