# TreeCity
# Team TreeCity

**Propose:** Who takes care of the trees of our planet? Even if legally the citizen is not responsible for environmental preservation, especially urban, it can and should be shared. We are a team with the objective of uniting three important spheres with focus on preservation, being the community, public and private with a single mission: to save the trees of our planet. Our solution condemns public power, empowers the image of private initiative and, more importantly, we create a common sense of social and environmental responsibility in the community. 

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

