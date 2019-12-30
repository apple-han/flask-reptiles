import datetime
import random

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def create_uuid():
    d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    n = random.randint(0, 1000)
    if n <= 10:
        n = str(0) + str(n)
    onlyNum = str(d) + str(n)
    return onlyNum
