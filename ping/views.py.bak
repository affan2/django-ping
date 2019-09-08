import json

from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .defaults import PING_DEFAULT_RESPONSE, PING_DEFAULT_CONTENT_TYPE
from .checks import checks
from .decorators import http_basic_auth


@csrf_exempt
@http_basic_auth
def status(request):
    """
    Returns a simple HttpResponse
    """

    response = "<h1>%s</h1>" % getattr(settings, 'PING_DEFAULT_RESPONSE', PING_DEFAULT_RESPONSE)
    content_type = getattr(settings, 'PING_DEFAULT_CONTENT_TYPE', PING_DEFAULT_CONTENT_TYPE)

    if request.GET.get('checks') == 'true':
        response_dict = checks(request)
        response += "<dl>"
        for key, value in sorted(response_dict.items()):
            response += "<dt>%s</dt>" % str(key)
            if isinstance(value, dict):
                value = ', '.join("%s: %s" % (k, v) for (k, v) in iter(value.items()))
            response += "<dd>%s</dd>" % str(value)
        response += "</dl>"

    if request.GET.get('fmt') == 'json':
        response_dict = checks(request)
        response = json.dumps(response_dict, sort_keys=True)
        content_type = 'application/json'

    return HttpResponse(response, content_type=content_type, status=200)
