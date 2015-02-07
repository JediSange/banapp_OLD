from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from ipware.ip import get_real_ip, get_ip
from models import Champion, Vote

def home(request):
  champions = Champion.objects.order_by('-score', 'name')

  params = {}
  params['champions'] = champions
  return render_to_response('partials/list.html', params)
 
def vote(request, **data):
  ip = get_real_ip(request)
  if ip is not None:
    # we have a real, public ip address for user
    print ip
  else:
    ip = get_ip(request)
    print ip
    # we don't have a real, public ip address for user
  print 'here'
  return JsonResponse({'result': 'success'})
