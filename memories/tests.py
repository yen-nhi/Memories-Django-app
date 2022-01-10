from django.test import TestCase
from .models import Memory
from django.contrib.auth.models import User, AnonymousUser
from .bl import create_memory, fetch_memories

class MemoryCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', 'test@email.com', 'somepassword')
        self.anon_user = AnonymousUser()

    def test_1(self):
        self.assertTrue(create_memory(self.user, 'Summer', 'Awsome', '13.756331', '100.501762'))
    
    def test_2(self):
        self.assertFalse(create_memory(self.user, 'Summer', 'Awsome', '-33.772535', '-118.959057'))
    
    def test_3(self):
        self.assertFalse(create_memory(self.anon_user, 'Summer', 'Awsome', '13.756331', '100.501762'))

    def tearDown(self):
        self.user.delete()

class MemoriesFetchTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('tester', 'test@email.com', 'somepassword')
        self.anon_user = AnonymousUser()
        self.memory1 = Memory.objects.create(user=self.user, name='Summer', comment='Awsome', location='PhuQuoc')
        self.memory2 = Memory.objects.create(user=self.user, name='Spring', comment='Charming', location='DaLat')
        self.memory3 = Memory.objects.create(user=self.user, name='Autumn', comment='Colorful', location='HaNoi')

    def test_1(self):
        raw = fetch_memories(user=self.user)
        memories = [item.serialize() for item in raw]
        transform = []
        for memory in memories:
            transform.append(sorted(memory.values()))
        keys = list(memory.keys())
        transform = sorted(transform)
        expect = sorted([sorted(['tester', 'Summer', 'Awsome', 'PhuQuoc']), 
                         sorted(['tester', 'Spring', 'Charming', 'DaLat']),
                         sorted(['tester', 'Autumn', 'Colorful', 'HaNoi'])
                        ])
        self.assertEqual(transform, expect)
        self.assertEqual(keys, ['username', 'name', 'comment', 'location'])

    def test_2(self):
        self.assertEqual(fetch_memories(user=self.anon_user), None)

    def tearDown(self):
        self.user.delete()
        self.memory1.delete()
        self.memory2.delete()
        self.memory3.delete()
