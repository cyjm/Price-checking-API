import uuid
from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that email/password(from the site forms) combo is valid or not.
        Checks that email exists, and that the password associated to that email is correct.
        :param email: user's email
        :param password: a sha512 hashed password
        :return: True if valid
        """
        user_data = Database.find_one("users", {"email":email}) #Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            # Tell user that their email doesn't exist in db'
            raise UserErrors.UserDontExistError('This email does not match any existing one in our database.')

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user that their password is wrong
            raise UserErrors.IncorrectPasswordError('Password you provided is incorrect.')

        return True