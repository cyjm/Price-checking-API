from passlib.hash import pbkdf2_sha512

class Utils(object):

    @staticmethod
    def hash_password(password):
        """
        hashes a password using pbkdf2_sha512
        :param password: the sha512 password from the login/register form
        :return: a sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        checks that the password the user sent matches with the one in db
        the database password is encrypted more than the user's password at this point
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if password match
        """
        return pbkdf2_sha512.verify(password, hashed_password)