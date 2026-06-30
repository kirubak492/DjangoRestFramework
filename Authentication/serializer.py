from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data= super().validate(attrs) #validate call the authentication
        
        data.update({
            "username":self.user.username
        })

        return data