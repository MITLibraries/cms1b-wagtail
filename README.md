# Wagtail evaluation application

This is an evaluation repository for using Wagtail for the Libraries' website.

## Getting started

```
git clone https://github.com/MITLibraries/cms1b-wagtail mysite
cd mysite
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

More information about [Wagtail](https://wagtail.io/) can be found at wagtail.io.

## Deploying

This project is intended to be deployed to an AWS Lambda [along these lines](https://gist.github.com/nealtodd/45e230bcfe809d76596a4af3540112d5) using [Zappa](https://www.zappa.io/). It assumes you have the relevant credentials already present.

```
git clone https://github.com/MITLibraries/cms1b-wagtail mysite
virtualenv -p python3 wgtl
source wgtl/bin/activate
cd mysite
pip install -r requirements.txt
zappa update
```
