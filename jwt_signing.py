from datetime import datetime, timedelta
import jwt

header = {"alg":"HS256","typ":"JWT"}
payload = {"role":"sinewave_user"}
jwt_secret = "12345678901234567890123456789012"
token = jwt.encode(payload, jwt_secret, algorithm="HS256")
print(token)