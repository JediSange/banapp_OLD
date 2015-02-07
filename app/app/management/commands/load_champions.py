from app.models import Champion
from app.settings import API_BASE, API_KEY, API_STATIC_URL
from django.core.management.base import NoArgsCommand
import json, time, urllib2

class Command(NoArgsCommand):
  help = "Pulls champions down from the Riot API"
  
  def handle_noargs(self, **options):
    # Handle fetching champions from Riot
    url = API_BASE + '/api/lol/na/v1.2/champion?api_key=' + API_KEY
    response = urllib2.urlopen(url).read()
    champions = json.loads(response)['champions']

    for champion in champions:
      # Build champion URL, Including image data
      champion_url = API_BASE + '/api/lol/static-data/na/v1.2/champion/'
      champion_url += str(champion['id'])
      champion_url += '?champData=image,tags&api_key=' + API_KEY

      # Get data about champion from Riot API
      response = urllib2.urlopen(champion_url).read()
      champion_info = json.loads(response)
      print champion_info
      print champion_info['name']

      # Build the object, save to DB
      toAdd = Champion()
      toAdd.champion_id = champion['id']
      toAdd.name = champion_info['name']
      toAdd.image_url = API_STATIC_URL + champion_info['image']['full']
      toAdd.tags = [tag.lower() for tag in champion_info['tags']]
      toAdd.score = 0
      toAdd.save()
    