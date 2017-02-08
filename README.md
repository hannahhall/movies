# Movie Search
Quickly find a movie's streaming URL


## To Install
1. Clone or fork repo
2. Install python packages `pip install -r requirements.txt`
3. Must have API key from Guidebox, get one [here](https://api.guidebox.com/docs/key)
4. To add API key to project: `echo 'key = ##YOUR_API_KEY##' > v1/api_key.py`
5. To run the app first run migrations `python manage.py migrate` then start the django server `python manage.py runserver`
6. Open `http://127.0.0.1:8000/` in the browser
