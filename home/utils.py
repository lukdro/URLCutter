import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):    
    the_id = "".join(random.choice(chars) for x in range(size))
    # try:
    #     order = Order.objects.get(order_id=the_id)
    #     id_generator()
    # except Order.DoesNotExist:
    #     return the_id
    return the_id

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)