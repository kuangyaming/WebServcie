Deploy:
=======
Login to a linux host w/ python3.x installed

cd ~   // cd to your home dir
git clone https://github.com/kuangyaming/WebServcie
cd WebServcie
python3.5 -m venv venv
source venv/bin/activate
pip3 install Flask
python3.5 webService.py


Run:
====
log onto another terminal session on the same linux host
curl -i http://localhost:5000/Fib/api/v1.0/3
curl -i http://localhost:5000/Fib/api/v1.0/5
curl -i http://localhost:5000/Fib/api/v1.0/10

