# Copyright (c) 2011,  2012 Free Software Foundation                                                                                       
#     This program is free software: you can redistribute it and/or modify                                                                 
#     it under the terms of the GNU Affero General Public License as                                                                       
#     published by the Free Software Foundation, either version 3 of the                                                                    
#     License, or (at your option) any later version.                                                                                      
#     This program is distributed in the hope that it will be useful,                                                                      
#     but WITHOUT ANY WARRANTY; without even the implied warranty of                                                                       
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                                        
#     GNU Affero General Public License for more details.                                                                                  
#     You should have received a copy of the GNU Affero General Public License                                                             
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.                                                                
 



from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('gstudio.views.addreln',
                       url(r'^refreshrts/$','getrefreshrts',name='refats'),
                       url(r'^form/(\d+)/$','addrelnform',name = 'addrelfrm'),
                       url(r'^thread/(\d+)/$', 'addreln',name='addreln'),
                       url(r'^deleteRelation/(\d+)/$', 'deleteRelation',name='deleteRelation'),
                       )
