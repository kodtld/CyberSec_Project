class RemoveHeaders(object):
   def __init__(self, get_response):
     self.get_response = get_response
   def __call__(self, request):
     response = self.get_response(request)
     response['Server'] = "Not shown"
     return response