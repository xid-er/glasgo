![Image text](https://github.com/xid-er/glasgo/blob/main/static/images/GlasGo-logo.jpeg)

# GlasGO relevant packages
![Image text](https://img.shields.io/badge/django-2.2.17-brightgreen.svg)
![Image text](https://img.shields.io/badge/pillow-8.1.2-green.svg)
![Image text](https://img.shields.io/badge/cffi-1.14.5-yellowgreen.svg)
![Image text](https://img.shields.io/badge/docker-4.3.1-yellow.svg)
![Image text](https://img.shields.io/badge/gitdb-4.0.5-orange.svg)
![Image text](https://img.shields.io/badge/idna-2.10-red.svg)
![Image text](https://img.shields.io/badge/pycparser-2.20-lightgrey.svg)
![Image text](https://img.shields.io/badge/pykwalify-1.7.0-blue.svg)
![Image text](https://img.shields.io/badge/requests-2.25.1-pink.svg)
![Image text](https://img.shields.io/badge/semver-2.13.0-brightgreen.svg)
![Image text](https://img.shields.io/badge/sqlparse-0.4.1-yellow.svg)
![Image text](https://img.shields.io/badge/urllib3-1.26.4-green.svg)

# Introduction to GlasGo
It is a website for Glaswegians, by Glaswegians.  

“GlasGo” is a social media web app that allows users to promote and share events in the Greater Glasgow area and engage with event promoters and organizers, as well as with each other. By providing users with a forum to post, “like” and comment on social life-related posts - be they text posts, link posts that can link to event organiser websites, or image posts as promotion for an upcoming event – GlasGo would aim to promote user engagement with local community organisers, businesses, and local government. The main page of GlasGo will be a feed page that can be sorted by most recent posts or most popular (those with most upvotes/likes in the last 7-10 days) and will be the primary page for user interaction. Anyone will be able to access the GlasGo site to view posts, but to post or interact with posts, users must first sign up and/or login. Users can also add categories to their posts to allow users to filter posts by the types they are interested in, such as “events” and “cool spots”, “shots of Glasgow” and others.

# Instruction to run GlasGo:

1 - cloning the project from Github:git clone https://github.com/xid-er/glasgo

2 - change the directory into glasgo that contaning manage.py file

3 - enter the following command on the terminal  
        conda activate glasgo  
        pip install -r requirements.txt  
			  python manage.py makemigrations  
			  python manage.py migrate  
		    python populate_glasgo.py  
		    python manage.py runserver  
		    
4 - enter 127.0.0.1:8000 into URL of browser  

# Developer of GlasGo
Kārlis Siders       2467273S@student.gla.ac.uk  
Lewis McGlinchey    2259138M@student.gla.ac.uk  
Simona Holubkova    2483856H@student.gla.ac.uk  
Yanling Liu         2451921L@student.gla.ac.uk  
