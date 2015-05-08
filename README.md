# Fart
This open source MITM HTTP proxy security tool is an open source pen testing and security auditing tool

# Installing
Install dependancies for mitmproxy, in ubuntu/debian
`apt-get install libxml2-dev libxslt1-dev python-dev libgd-dev libffi-dev`

Make sure you are running a version of pyopenssl >=0.14
Create a virtual env and then run
`python setup.py develop`

# Running
`cd` into root directory of project and run
`pserve development.ini`
