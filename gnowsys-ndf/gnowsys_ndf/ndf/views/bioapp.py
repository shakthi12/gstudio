''' -- imports from python libraries -- '''
# import os -- Keep such imports here
import json
from difflib import HtmlDiff

''' -- imports from installed packages -- '''
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.defaultfilters import slugify

from django_mongokit import get_database

try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId


''' -- imports from application folders/files -- '''
from gnowsys_ndf.settings import GAPPS

from gnowsys_ndf.ndf.models import Node, GSystemType, GSystem
from gnowsys_ndf.ndf.models import HistoryManager
from gnowsys_ndf.ndf.rcslib import RCS
from gnowsys_ndf.ndf.org2any import org2html
from gnowsys_ndf.ndf.views.methods import get_node_common_fields,create_grelation_list
from gnowsys_ndf.ndf.management.commands.data_entry import create_gattribute
from gnowsys_ndf.ndf.views.methods import get_node_metadata, set_all_urls


#######################################################################################################################################

db = get_database()

collection = db[Node.collection_name]
gst_bioapp = collection.Node.one({'_type': u'GSystemType', 'name': GAPPS[16]})
history_manager = HistoryManager()
rcs = RCS()
app = collection.Node.one({'_type': u'GSystemType', 'name': GAPPS[16]})

#######################################################################################################################################
#                                                                            V I E W S   D E F I N E D   F O R   G A P P -- ' P A G E '
#######################################################################################################################################

def bioapp(request, group_id, app_id=None):
        
        
        
 return render_to_response("ndf/bioapp_list.html",
                                  {'groupid':group_id,
                                   'group_id':group_id
                                  }, 
                                  context_instance=RequestContext(request))
      

