import json
import yaml

from .forms import GuiForm
from django.shortcuts import render


def render_obj(obj):
    from collections import Mapping, Iterable
    import types
    if isinstance(obj, types.StringTypes):
        return obj
    elif isinstance(obj, Mapping):
        string = "<table style='border-color:#ccc;border-width:1px;border-style:solid'>"
        for key, value in obj.iteritems():
            string += "<tr><td style='border-color:#ccc;border-width:1px;border-style:solid'><strong>{}</strong></td><td style='border-color:#ccc;border-width:1px;border-style:solid'>{}</td></tr>".format(
                key, render_obj(value))
        string += "</table>"
        return string
    elif isinstance(obj, Iterable):
        string = "<table class='table stable-striped'>"
        for value in obj:
            string += "<tr><td style='border-color:#ccc;border-width:1px;border-style:solid'>{}</td></tr>".format(render_obj(value))
        string += "</table>"
        return string
    else:
        return str(obj)


def gui(request):
    """Renders the gui page"""
    gform = GuiForm()
    return render(request, 'gui.html', {'form': gform})


def detail(request):
    """View for test details"""
    source_data = request.POST.get('source_data', None)
    source_type = request.POST.get('source_type', 'JSON')
    if source_type == 'YAML':
        ss = yaml.safe_load(source_data)
    else:
        ss = json.loads(source_data)
    return render(request, 'detail.html',
                  {'data': render_obj(ss)})
