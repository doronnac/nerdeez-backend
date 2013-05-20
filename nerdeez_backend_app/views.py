'''
Created on Feb 2, 2013
will create the views for the server app
@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from django.shortcuts import render_to_response
from django.template import RequestContext

#===============================================================================
# end imports
#===============================================================================

    
def porthole(request):
    '''
    used for cross domain requests
    '''
    return render_to_response('porthole.html', locals(), context_instance=RequestContext(request))

def proxy(request):
    '''
    used for cross domain requests
    '''
    return render_to_response('proxy.html', locals(), context_instance=RequestContext(request))