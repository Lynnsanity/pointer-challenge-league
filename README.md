pointerchallengeleague.com
--------------------------

A website I've made for my very first own personal client.
Uses nicegui python framework and can be deployed into a container.

### Pre-Reqs:

* You need a python virtual environment that has nicegui installed.

That's pretty much it lol.

### To run locally:
```sh
# clone down this repo and go into dir
git clone https://github.com/Lynnsanity/pointer-challenge-league && cd pointer-challenge-league
# start the local environment
python3 -m venv env && source env/bin/activate

# set up env variables needed for login
export AUTH_USER=whatever-you-want
export AUTH_PASS=whatever-you-want
export STORAGE_SECRET=whatever-you-want

# install nicegui
pip install nicegui

# start:
python3 main.py
```
A browser window should open http://localhost:8080 showing PCL website.

### Make a Docker/Podman Build

```sh
# edit the VERSION file to whatever version you want to bump to then:
make release
```

### K8s

New image tag gets put into k8s/pcl-deployment.yml image and gets applied like:

`kubectl -n pcl apply -f pcl-deployment.yml`


