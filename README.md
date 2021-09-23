# UrbanCompanyNITK

## How to run the project
1. Create a virtual environment and activate it.
2. `pip3 install -r requirements.txt`
3. Create a database named `UCDB` locally using mysql
4. Run the following in your terminal
```
cd UC/UrbanCompanyNITK/
python3 manage.py migrate
python3 manage.py runserver
```
5. Go to localhost:8000 in your browser.
