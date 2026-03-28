import schemas
from passlib.context import CryptContext 
pwd_cnt = CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def bcrypt(password: str, request: schemas.User):
        safe_password = request.password[:72] 
        hashed_password = pwd_cnt.hash(safe_password)
        return hashed_password 
    
    def verify(hashed_password, plain_password):
        return pwd_cnt.verify(plain_password, hashed_password)



