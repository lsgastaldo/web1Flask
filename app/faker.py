from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker

from . import db
from .models import User, News

def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        user = User(
            username=fake.user_name(),
            name=fake.first_name(),
            lastname=fake.last_name(),
            email=fake.email(),
            aboutme=fake.text(),
            password='123'
        )
        db.session.add(user)
        try:
            db.session.commit()
            i+=1
        except IntegrityError:
            db.session.rollback()

def news(count=50):
    fake = Faker()
    for i in range(count):
        news = News(
            title='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            index_body='Etiam a arcu nec augue venenatis fermentum rutrum non ante. Aenean bibendum urna turpis, placerat rutrum nulla facilisis aliquet. Fusce posuere, eros tempus egestas lobortis, leo eros porta est, sed semper lacus dolor eget tortor. Aenean rutrum dui nec neque sollicitudin, a interdum massa cursus. Nullam pulvinar iaculis commodo. Duis nec vestibulum risus, id iaculis turpis. Sed ullamcorper lacinia neque, at iaculis velit dignissim eget. Donec eget mi ultricies, ultricies nibh sit amet, suscipit lacus.',
            body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a arcu nec augue venenatis fermentum rutrum non ante. Aenean bibendum urna turpis, placerat rutrum nulla facilisis aliquet. Fusce posuere, eros tempus egestas lobortis, leo eros porta est, sed semper lacus dolor eget tortor. Aenean rutrum dui nec neque sollicitudin, a interdum massa cursus. Nullam pulvinar iaculis commodo. Duis nec vestibulum risus, id iaculis turpis. Sed ullamcorper lacinia neque, at iaculis velit dignissim eget. Donec eget mi ultricies, ultricies nibh sit amet, suscipit lacus.Morbi ac nunc non velit suscipit facilisis. Nulla facilisi. Duis laoreet consequat dui, a tristique sem ullamcorper quis. Vestibulum ligula sem, scelerisque id libero sed, facilisis dignissim est. Maecenas at enim accumsan, sodales augue a, molestie nulla. Nullam tincidunt dolor sed suscipit semper. Suspendisse fermentum dignissim bibendum.In magna diam, facilisis ac dignissim vitae, sagittis sit amet mi. Aliquam vel ex varius, fringilla magna sit amet, finibus dui. Cras pharetra ante id pharetra mattis. Duis bibendum eu mi eget convallis. Pellentesque vel rutrum magna, et vulputate metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent nec elementum ipsum. Suspendisse condimentum a nisi a rhoncus. Donec vulputate massa in diam tempus, eu sollicitudin mauris consectetur.Donec iaculis, massa at porta viverra, justo quam ultricies quam, vel tincidunt nisl nulla sit amet augue. Maecenas quis ante et est rutrum mollis sed eget purus. Vivamus vitae lorem sem. Aenean vel cursus mauris. Proin magna libero, condimentum in elementum finibus, accumsan quis urna. Etiam imperdiet, nisl eget rutrum efficitur, tortor dui tincidunt ligula, ac molestie neque tortor sed quam. Morbi scelerisque elit eget ex consequat varius. Nam dictum nunc et mi porttitor, sit amet pellentesque orci facilisis. Integer lobortis maximus justo tristique lacinia. Aliquam erat volutpat.Sed eu velit sem. Sed quis neque nec purus fringilla egestas. Morbi ac massa quis leo congue ultricies. Integer sed felis ac nulla eleifend sodales. Suspendisse id nisl ultrices, aliquet ipsum eget, eleifend felis. Suspendisse et sem non nulla vehicula sollicitudin eget eget ante. Aenean pulvinar cursus sem, quis ornare dui tempus et. Curabitur sit amet metus ac odio euismod lobortis et bibendum arcu. Curabitur elit tellus, tempus eget suscipit vitae, consequat congue velit. Nulla sit amet elementum odio, sed dapibus nisl. Aliquam vulputate lectus eu placerat varius.',
            img='/static/images/imgnoticias2.jpg',
            author_id=i
        )
        db.session.add(news)
    db.session.commit()
