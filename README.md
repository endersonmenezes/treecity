# TreeCity
# Team TreeCity

**Propose:** Who takes care of the trees of our planet? Legally we may not be responsible for them in most cases, but we can do more, because they are responsible for us. We are a team with the purpose of uniting three spheres present in our community, with a common mission: to save the trees of our planet.

**Develop:** (System + Landing Page) designed and prepared to be developed in Python using a Framework (Django) with direct deploy in Heroku.

We are from :heart: *Maringá*

# How To

1. Create a *.env* archive
```python
SECRET_KEY=
DEBUG =
DISABLE_COLLECTSTATIC=
```
2. Install the requirements.txt **use venv in your ide or manually [See this](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
```
pip install -r requirements.txt
```
3. Make initial migrations and migrate to database if you want test in local server
```
python manage.py makemigrations
python manage.py migrate
```
4. If you go deploy on your Heroku ACC just fork this project and change the step 3 for step 4, before install the Heroku CLI and update
```
heroku login
heroku config:push -a *yourappname*
heroku config // for test config
heroku run python manage.py migrate
```
# Next Step

**The system is still not functional, only the development and deploy environment was created and model. And an initial database model with some modifications within DjangoAdmin were performed.**

# About Us

Jean Carlo - Tarik - Enderson Menezes - Bruno Garcia

![tree city](https://i.imgur.com/Z5T7PsE.png)

On NasaSpaceApps -> [Link](https://2018.spaceappschallenge.org/challenges/what-world-needs-now/health-makes-wealth/teams/treecity/project)

On Web -> [Link](http://treecity.ml)

