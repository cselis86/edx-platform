"""
Display all installed xblocks in Studio
TODO: Grant access permission only to studio admin (not course staff)

"""
from edxmako.shortcuts import render_to_string, render_to_response

from .component import _advanced_component_types

def installed_xblocks(request):
	advanced_component_types = _advanced_component_types()
	return render_to_response('xblock_manager_installed_xblocks.html', {
                'advanced_component_types': advanced_component_types
            })
