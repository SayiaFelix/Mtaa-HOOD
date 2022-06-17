from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# class ProfileTestClass(TestCase):
#     '''
#     Test case for the Profile class and it's behaviours
#     '''
#     def setUp(self):
#         '''
#         Method that will run before any test case under this class
#         '''
#         self.new_user = User(username = "cherry", email = "cherry@gmail.com", password = "dontbelittleyourself",)
#         self.new_user.save()

#         self.new_neigh = Hood(neighbourhood_name = "umoja")
#         self.new_neigh.save()

#         self.new_profile = Profile(username = self.new_user, neighbourhood = self.new_neigh, name = "bilal rock", email = "bilal@gmail.com", bio = "I see myself here")

#     def test_instance(self):
#         '''
#         Test to confirm that the object is being instantiated correctly
#         '''
#         self.assertTrue(isinstance(self.new_profile, Profile))

#     def tearDown(self):
#         Profile.objects.all().delete()

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'love her',contact= 43966606,email='jay@gmail')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_search_profile(self):
        self.profile.save()
        profile = Profile.search_profile('cherry')
        self.assertTrue(len(profile) > 0)
    

