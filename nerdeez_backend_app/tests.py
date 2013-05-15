'''
Created on May 14, 2013
tests file for REST server
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.test import ResourceTestCase
from nerdeez_backend_app.models import University

#===============================================================================
# end imports
#===============================================================================

#===============================================================================
# begin constants
#===============================================================================

UNIVERSITY_URL = '/api/v1/university/'
CURRENT_FORMAT = 'json'

#===============================================================================
# end constants
#===============================================================================

#===============================================================================
# begin testing
#===============================================================================


class UniversityResourceTest(ResourceTestCase):
    fixtures=['universities']
    
    def test_university_interaction(self):
        '''
        test1: test that 'get' works. curl http://localhost:8000/api/v1/
        test2: test that 'post' works. curl
        
        '''
        
        #test that get works
        print University.objects.all()
        resp = self.api_client.get(UNIVERSITY_URL, format=CURRENT_FORMAT)
        self.assertHttpOK(resp)
        obj = self.deserialize(resp)
        self.assertEqual(obj['objects'][0]['title'], 'Namek', 'Failed to assertTitle')
        
        #test that post works
        resp = self.api_client.post(UNIVERSITY_URL, format=CURRENT_FORMAT, data={'title':'technion','description':"A really good place to study",'image':'technionimg','website':'www.technion.ac.il'})
        self.assertHttpCreated(resp)
        
        #test that the user can't update any of the universities data
        resp = self.api_client.put(UNIVERSITY_URL + '1/', furmat=CURRENT_FORMAT, data={'title': "UGOTHACKED"})
        self.assertHttpMethodNotAllowed(resp)
        
        #test that the user can't delete any university / university data
        resp = self.api_client.delete(UNIVERSITY_URL + '1/', format=CURRENT_FORMAT)
        self.assertHttpMethodNotAllowed(resp)
        
#===============================================================================
# end testing
#===============================================================================
