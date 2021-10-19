# UrbanCompanyNITK
## How to run the project
- The project is hosted at [here](https://urbancompany-nitk.herokuapp.com/)

## How to run the project locally
1. Create a virtual environment and activate it.
2. `pip3 install -r requirements.txt`
3. Create a database named `UCDB` locally using mysql
4. In the file /UrbanCompanyNITK/settings.py in line 84 change the mysql password of databse to your mysql password
5. Run the following in your terminal
```
python3 manage.py migrate
source .env
python3 manage.py runserver
```
6. Go to localhost:8000 in your browser.
