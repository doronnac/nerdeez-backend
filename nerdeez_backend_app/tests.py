'''
Created on May 14, 2013
tests file for models.py
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

from tastypie.test import ResourceTestCase
from nerdeez_backend_app.models import University

class UniversityResourceTest(ResourceTestCase):
    fixtures=['universities']
    def setup(self):
        super(UniversityResourceTest, self).setup()
    
    def test_university_creation(self):
        
        #check that get and post commands work
        print University.objects.all()
        resp = self.api_client.get('/api/v1/university/', format='json')
        self.assertHttpOK(resp)
        obj = self.deserialize(resp)
        self.assertEqual(obj['objects'][0]['title'], 'Namek', 'Failed to assertTitle')
        
        resp = self.api_client.post('/api/v1/university/', format='json', data={'title':'technion','description':'A really good place to study','image':'technionimg','website':'www.technion.ac.il'})
        self.assertHttpCreated(resp)
        