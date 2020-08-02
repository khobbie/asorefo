from database.mysql_db import conn
# ApiKeyRequestModel
from models.generate_key import ApiKeyRequestModel
# UUID
import uuid
# SECRET HASHING
import secrets


# CEATE API CONSUMER
def create_api_consumer(user):
    x_api_key = uuid.uuid5(uuid.NAMESPACE_DNS, "kite.com")
    x_api_key = '{}'.format(x_api_key)
    x_api_secret = secrets.token_hex(6)
    password = secrets.token_hex(6)
    cur.callproc("create_api_consumer", (user.first_name, user.last_name,
                                         user.first_name, user.email, None, password, x_api_key, x_api_secret))
    conn.commit()
    return {'password': password, 'x-api-key': x_api_key, 'x-api-secret': x_api_secret}
