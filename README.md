#BanApp
Web app for anonymous voting on who to ban in League of Legends

###Heroku Commands

Load champions and update verison URLs

    heroku run python app/manage.py load_champions

TODO List:
- Recalc score every day from votes, cron job?
- Use Nginx to serve application on Heroku

Possible Improvements:
- Pull images down to local for gzip compression
- Champion images as sprite sheets -- see if we can get from API
- Bower for front end dependency management
