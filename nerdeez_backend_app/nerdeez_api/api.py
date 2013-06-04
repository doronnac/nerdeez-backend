
'''
Created on May 13, 2013
the rest api is defined here
@author: Doron Nachshon
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from nerdeez_backend_app.models import University

#===============================================================================
# end imports
#===============================================================================


#===============================================================================
# begin security resource
#===============================================================================



#===============================================================================
# end security resource
#===============================================================================


#===============================================================================
# begin rest resources
#===============================================================================



class NerdeezResource(ModelResource):
    '''
    abstract class with common attribute common to all my rest models
    '''
    class Meta:
        allowed_methods = ['get']
        always_return_data = True
        authentication = Authentication()
        authorization = Authorization()

  
#===============================================================================
# begin model resources
#===============================================================================


class UniversityResource(NerdeezResource):
    '''
    the rest api for the university model is defined here
    '''
    class Meta(NerdeezResource.Meta):
        allowed_methods= ['get', 'post', 'delete'] #put and delete enabled FOR TESTING ONLY!!
        queryset = University.objects.all()


#===============================================================================
# end model resources
#===============================================================================

#===============================================================================
# end rest resources
#===============================================================================