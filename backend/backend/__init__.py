from rest_framework_jwt.utils import jwt_payload_handler as original_payload_handler

def jwt_payload_handler(user):
    payload = original_payload_handler(user)
    payload['isCandidate'] = True
    return payload
