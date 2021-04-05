![Image text](https://github.com/xid-er/glasgo/blob/main/static/images/g-logo.png)

# GlasGO relevant packages
![Image text](https://img.shields.io/badge/django-2.2.17-green.svg)
![Image text](https://img.shields.io/badge/pillow-8.1.0-yellow.svg)
![Image text](https://img.shields.io/badge/requests-blue.svg)
![Image text](https://img.shields.io/badge/coverage-blue.svg)

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