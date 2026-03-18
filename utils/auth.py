from fastapi import Header, HTTPException

from fastapi import Header

def verify_token(authorization: str = Header(None)):
    print("HEADER RECEIVED:", authorization)
    return authorization