'''
Created on May 14, 2013
tests file for models.py
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

#------------------------------------------------------------------------------ begin imports

from tastypie.test import ResourceTestCase
from nerdeez_backend_app.models import University

#------------------------------------------------------------------------------ end imports


#------------------------------------------------------------------------------ begin constants

university_url = '/api/v1/university/'
current_format = 'json'

#------------------------------------------------------------------------------ end constants

#------------------------------------------------------------------------------ begin testing

class UniversityResourceTest(ResourceTestCase):
    fixtures=['universities']
    def setup(self):
        super(UniversityResourceTest, self).setup()
    
    def test_university_creation(self):
        
        #test that get works
        print University.objects.all()
        resp = self.api_client.get(university_url, format=current_format)
        self.assertHttpOK(resp)
        obj = self.deserialize(resp)
        self.assertEqual(obj['objects'][0]['title'], 'Namek', 'Failed to assertTitle')
        
        resp = self.api_client.post(university_url, format=current_format, data={'title':'technion','description':"A really good place to study",'image':'technionimg','website':'www.technion.ac.il'})
        self.assertHttpCreated(resp)
        
        #test that the user can't update any of the universities data
        resp = self.api_client.put(university_url + '1/', current_format, data={'title': "UGOTHACKED"})
        self.assertHttpMethodNotAllowed(resp)
        
        #test that the user can't delete any university / university data
        resp = self.api_client.delete(university_url + '1/', current_format)
        self.assertHttpMethodNotAllowed(resp)
        
#------------------------------------------------------------------------------ end testing
