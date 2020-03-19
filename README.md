# 726-project
SFU Machine Learning Frisson Group

###Required:
Python 3.6
Other dependencies installed in venv

##Setup (Linux):
```
git clone git@github.com:djlrevic/726-project.git
cd 726-project
python3 -m venv venv  # create virtual environment in venv folder
./venv/Scripts/activate  # enter virtual environment
pip3 install -r requirements.txt
pip3 install git+ssh://git@github.com/mgedmin/python-midi.git@python3#egg=python-midi

curl -O https://storage.googleapis.com/magentadata/datasets/maestro/v2.0.0/maestro-v2.0.0-midi.zip
unzip maestro-v2.0.0-midi.zip && rm maestro-v2.0.0-midi.zip
```
