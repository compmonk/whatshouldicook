# whatshouldicook

This is a voice based recipe search engine website. We can find recipes based on the ingredients we have.

## Setup
```
git clone https://github.com/compmonk/whatshouldicook.git
cd whatshouldicook
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
sudo apt-get install -y $(grep -vE "^\s*#" packages.txt  | tr "\n" " ")
pip install -r requirements.txt
bower install
python whatshouldicook/whatshouldicook/manage.py runserver
```



## To run
```
source venv/bin/activate
python whatshouldicook/whatshouldicook/manage.py runserver
```
