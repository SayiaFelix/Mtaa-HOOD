from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# class ProfileTestClass(TestCase):

#     def setUp(self):
#         self.user = User.objects.create(id = 1, username='cherry')
#         self.profile = Profile.objects.create(user = self.user,bio = 'love her',contact= 43966606,email='jay@gmail')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile,Profile))

#     def test_save_profile(self):
#         self.assertTrue(isinstance(self.profile,Profile))

#     def test_get_profile(self):
#         self.profile.save()
#         profile = Profile.get_profile()
#         self.assertTrue(len(profile) > 0)

#     def test_search_profile(self):
#         self.profile.save()
#         profile = Profile.search_profile('cherry')
#         self.assertTrue(len(profile) > 0)
    

class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class and it's behaviours
    '''
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_user = User(username = "cherry", email = "cherry@gmail.com", password = "awesomebouy",)
        self.new_user.save()

        self.new_neigh = Hood(hood_name = "umoja")
        self.new_neigh.save()

        self.new_profile = Profile(user = self.new_user, neighbourhood = self.new_neigh, email = "cherry@gmail.com", bio = "I love her")

    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()

class HoodClass(TestCase):
    def setUp(self):
        self.umoja = Hood(hood_name = 'umoja',   occupants_count = '10')

    def test_instance(self):
        self.assertTrue(isinstance(self.umoja, Hood))

    def tearDown(self):
        Hood.objects.all().delete()

    def test_save_method(self):
        self.umoja.create_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.umoja.delete_hood('umoja')
        hood = Hood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_find_neighbourhood(self):
        self.umoja.create_hood()
        fetched_hood = Hood.find_hood("umoja")
        self.assertNotEqual(fetched_hood, self.umoja)

class healthservicesTestClass(TestCase):
    def setUp(self):
        self.surgery = healthservices(healthservices = 'Surgery')

    def test_instance(self):
        self.assertTrue(isinstance(self.surgery, healthservices))

    def tearDown(self):
        healthservices.objects.all().delete()

    def test_save_method(self):
        self.surgery.save_healthservices()
        health = healthservices.objects.all()
        self.assertTrue(len(health) > 0)

    def test_delete_method(self):
        self.surgery.delete_healthservices('surgery')
        health = healthservices.objects.all()
        self.assertTrue(len(health) == 0)

