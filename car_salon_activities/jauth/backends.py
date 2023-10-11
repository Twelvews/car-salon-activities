"""
backends.py: File, containing JWT backends for a jauth app.
"""


from typing import ClassVar
from datetime import datetime, timedelta
from jwt import InvalidTokenError, ExpiredSignatureError, decode, encode
from django.conf import settings


class TokenBackend:
    """
    TokenBackend: Provides low-level functions for JWT token.

    Raises:
        ValueError: Raises when token type is not provided.
    """

    token_invalid_error: ClassVar[type[InvalidTokenError]] = InvalidTokenError
    token_expired_error: ClassVar[type[ExpiredSignatureError]] = ExpiredSignatureError

    @classmethod
    def generate_token(cls, *, type: str, user_id: int) -> str:
        match type:
            case 'access':
                lifetime = timedelta(minutes=settings.JWT_TOKEN['ACCESS_TOKEN_LIFETIME_MINUTES'])
            case 'refresh':
                lifetime = timedelta(days=settings.JWT_TOKEN['REFRESH_TOKEN_LIFETIME_DAYS'])
            case _:
                raise ValueError('Unexpected type of token: must be access or refresh')

        expiry_token_date = datetime.now() + lifetime

        payload = {
            'sub': user_id,
            'exp': int(expiry_token_date.strftime('%s')),
        }

        return encode(payload, settings.SECRET_KEY, settings.JWT_TOKEN['ENCODE_ALG'])

    @classmethod
    def get_payload_by_token(cls, *, token: str) -> dict:
        payload = decode(token, settings.SECRET_KEY, settings.JWT_TOKEN['DECODE_ALGS'])
        return payload