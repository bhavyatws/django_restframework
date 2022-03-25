
from rest_framework import serializers
from .models import Student_Table
#Validators
# def starts_with_r(value):
#     if value[0].lower()!='r':
#         raise serializers.ValidationError('Name must be start with r')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student_Table
        fields=['id','name','roll','city']
        # read_only_fields=['name']#now we cannot update name
    #field level validation
    def validate_roll(self, value):#function_name=> validate_fieldname
        if value>=200:
            raise serializers.ValidationError("Seat Full")
        return value
