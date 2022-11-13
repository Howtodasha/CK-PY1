import random
import string
from random import sample
def get_random_password() -> str:
    
    n = 8
    password = ""
    words_ = string.ascii_letters + string.digits
    pass_ = "".join(sample(words_, n))
    return pass_
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
