from passlib.context import CryptContext

pwt_contect = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return pwt_contect.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(plain_password):
        return pwt_contect.hash(plain_password)