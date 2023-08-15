from django.contrib.auth.base_user import BaseUserManager

class EmployeeManager(BaseUserManager):
    """
    Employee model manager where  is the unique identifiers.
    """

    def create_user(self, email, username, group = 1, password = None, **extra_fields):
        """
        Create and save a employee data [username, email, group and hashed password].
        """
        account = self.model(username=username, email = email,
        group = group, **extra_fields)
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, username, password = None, **extra_fields):
        """
        Create and save  super user for hr employee.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username = username, email=email,
        group = 0,password = password, **extra_fields)