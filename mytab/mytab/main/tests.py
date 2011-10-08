"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from mytab.main.models import *
import unittest

class Test_initialTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        
        House.objects.all.delete()
        Appartment.objects.all.delete()
        Habitant.objects.all.delete()
        
        House.objects.create(address="Kuohikatu 5", real_estate_agent='Vasara', number_of_appartments=30, number_of_stairs=3)
        House.objects.create(address="Kuohikatu 10", real_estate_agent='Vasara', number_of_appartments=20, number_of_stairs=2)
        
        Appartment.objects.create(house="Kuohikatu 5", stair="A", number=1, number_of_habitants=3, number_of_keys=4)
        Appartment.objects.create(house="Kuohikatu 5", stair="A", number=2, number_of_habitants=2, number_of_keys=3)
        Appartment.objects.create(house="Kuohikatu 5", stair="A", number=3, number_of_habitants=1, number_of_keys=3)
        
        Habitant.objects.create(first_name="Erkki", last_name="Latvala", ss="123456-1234", house="Kuohikatu 5", appartment="")
        Habitant.objects.create(first_name="Matti", last_name="Latvala", ss="123456-5422", house="Kuohikatu 5", appartment="")
        Habitant.objects.create(first_name="Pekka", last_name="Latvala", ss="010196-845J", house="Kuohikatu 5", appartment="")
        
        Habitant.objects.create(first_name="Erkki", last_name="Latvala", ss="150353-1234")
        
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
