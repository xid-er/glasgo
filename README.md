# GlasGO
A website for Glaswegians, by Glaswegians

Instruction to run GlasGo:

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