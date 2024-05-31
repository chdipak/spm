from itsdangerous import URLSafeTimedSerializer
from keys import secret_key
def token(data,salt):
    serializer=URLSafeTimedSerializer(secret_key)
    var1=serializer.dumps(data,salt=salt)
    return var1
    
