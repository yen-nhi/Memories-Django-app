from django.test import TestCase
from .models import Memory
from django.contrib.auth.models import User, AnonymousUser
from .bl import create_memory, fetch_memories

class MemoryCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', 'test@email.com', 'somepassword')
        self.anon_user = AnonymousUser()

    def test_create_memory(self):
        self.assertTrue(create_memory(self.user, 'Summer', 'Awsome', '13.756331', '100.501762'))
        self.assertFalse(create_memory(self.user, 'Summer', 'Awsome', '0', '0'))
        self.assertFalse(create_memory(self.anon_user, 'Summer', 'Awsome', '13.756331', '100.501762'))

    def clear_setup(self):
        self.user.delete()

class MemoriesFetchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', 'test@email.com', 'somepassword')
        self.anon_user = AnonymousUser
        self.memory1 = Memory.objects.create(user=self.user, name='Summer', comment='Awsome', location='PhuQuoc')
        self.memory2 = Memory.objects.create(user=self.user, name='Spring', comment='Charming', location='DaLat')
        self.memory3 = Memory.objects.create(user=self.user, name='Autumn', comment='Colorful', location='HaNoi')


    def test_memories_fetch(self):
        self.assertEqual(fetch_memories(user=self.user),
        [
        # {'username': 'tester', 'name': 'Summer', 'comment': 'Awsome', 'location': 'PhuQuoc'},
        # {'username': 'tester', 'name': 'Spring', 'comment': 'Charming', 'location': 'DaLat'},
        # {'username': 'tester', 'name': 'Autumn', 'comment': 'Colorful', 'location': 'HaNoi'}
        ])

        self.assertEqual(fetch_memories(user=self.anon_user), None)

    def clear_setup(self):
        self.user.delete()
        self.memory1.delete()
        self.memory2.delete()
        self.memory3.delete()
