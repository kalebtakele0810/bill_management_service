from django_seed import Seed
from django.contrib.auth.models import User

seeder = Seed.seeder()

from base.models import User
user = User.objects.create_user(username='test',
                                 email='test@kacha.et',
                                 password='test')

seeder.add_entity(User, user)