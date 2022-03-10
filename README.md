<h1 align="center"><a href="#" alt="cookin">Cookin'</a> 🧑‍🍳📓💟</h1>

<h2>Contents</h2>

- [1. About 💻](#1-about-)
- [2. Application's links 🔗](#2-applications-links-)
- [3. General Functionalities ⚙️](#3-general-functionalities-️)
- [4. Technologies 🧰](#4-technologies-)
  - [4.1 Requisites ☑️](#41-requisites-️)
- [5. Developers' Team 🧑‍💻](#5-developers-team-)
- [6. Terms of Use 📜](#6-terms-of-use-)

<a name="about"></a>

## 1. About 💻

**_Cookin' affective recipes_** is an application that focuses on creating and/or sharing affective recipes that the user can access anytime, like a private book of recipes.

The registered user is allowed to consult, to rate and to save as favorite other users' recipes once these recipes are shared with others. User can also add to favorite his own recipes but can only rate others' recipes.

This API was developed in order to storage the recipes' data as well as the registered users' data and to allow users to log in the app in order to enjoy all the application's features described above.

All routes require Bearer token authentication (except register and login). Access token can be obtained in login successful response.

This API contains 6 routes and 18 endpoints. For more detailed information about the API and its endpoints, please consult API Documentation in Application links section.

🎓 Project developed as Capstone of Q3 back end module of the Fullstack Developer Course of [Kenzie Academy Brasil](https://kenzie.com.br/v2/).

<a name="links"></a>

## 2. Application's links 🔗

- <a name="API documentation" href="https://documenter.getpostman.com/view/19787362/UVksLDvG" target="_blank">API Documentation</a>
- <a name="API deploy in Heroku" href="https://cookin-api-capstone.herokuapp.com/" target="_blank">API Deploy in Heroku</a>

## 3. General Functionalities ⚙️

- [x] Once registered in Cookin' app and signed in, users can:
  - [x] update their name, gender or profile photo;
  - [x] create new recipes of their own and keep them private;
  - [x] update recipe's data, like title, ingredients, instructions, category, preparation time, difficulty, portion size and recipe image;
  - [x] consult their own private recipes, shared recipes in Cookin' community and recipes added to favorites;
  - [x] consult users of the Cookin' community info;
  - [x] choose whether to share private recipes with the Cookin' community;
  - [x] add recipes to favorites, their own recipes or shared recipes by other users from Cookin' community;
  - [x] rate shared recipes from Cookin' community;
  - [x] filter recipes by title, category, difficulty, preparation time and portion size;

<a name="technologies"></a>

## 4. Technologies 🧰

- <a name="python" href="https://docs.python.org/3/" target="_blank">Python</a>
- <a name="flask" href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank">Flask</a>
- <a name="python.env" href="https://pypi.org/project/python-dotenv/" target="_blank">python-dotenv</a>
- <a name="flask-jwt" href="https://flask-jwt-extended.readthedocs.io/en/stable/" target="_blank">Flask-jwt-extended</a>
- <a name="flask=sql" href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/" target="_blank">Flask SQLAlchemy</a>
- <a name="postgreSQL" href="https://www.postgresql.org/docs/" target="_blank">PostgreSQL</a>
- <a name="flask-m" href="https://flask-migrate.readthedocs.io/en/latest/" target="_blank">Flask Migrate</a>
- <a name="marshmallow" href="https://marshmallow.readthedocs.io/en/stable/index.html" target="_blank">Marshmallow</a>

<a name="requisites"></a>

### 4.1 Requisites ☑️

- Python above version 3.9.6;
- Package manager <a name="pip" href="https://pip.pypa.io/en/stable/" target="_blank">PIP</a>;
- PostgreSQL database;

<a name="teamdev"></a>

## 5. Developers' Team 🧑‍💻

<table>
  <tr>
    <td align="center"><a href="https://github.com/emilyregolao" title="GitHub"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/85745693?v=4" alt="avatar" width="100px;" alt=""/><br /><sub><b>Emily Regolão</b></sub></a><br /><a href="https://www.linkedin.com/in/emilypregolao/" title="Linkedin"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/larissakoliveira" title="GitHub"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/82476805?v=4" width="100px;" alt=""/><br /><sub><b>Larissa Oliveira</b></sub></a><br /><a href="https://www.linkedin.com/in/larissakoliveira/" title="Linkedin"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/LucasGasque" title="GitHub"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/75370906?v=4" width="100px;" alt=""/><br /><sub><b>Lucas Gasque</b></sub></a><br /><a href="https://www.linkedin.com/in/lucasgasque/" title="Linkedin"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/raissalst" title="GitHub"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/85745938?v=4" width="100px;" alt=""/><br /><sub><b>Raissa Toledo</b></sub></a><br /><a href="https://www.linkedin.com/in/raissalstoledo/" title="Linkedin"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a></td>
    <td align="center"><a href="https://github.com/rbressanelli" title="GitHub"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/79763201?s=96&v=4" alt="avatar" width="100px;" alt=""/><br /><sub><b>Roberto Bressanelli</b></sub></a><br /><a href="https://www.linkedin.com/in/robertobressanelli/" title="Linkedin"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white"></a></td>
  </tr>
</table>

<a name="terms"></a>

## 6. Terms of Use 📜

This is an Open Source project for educational and non-commercial purposes.

**License type**: <a name="gpl" href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank">GPL</a>
