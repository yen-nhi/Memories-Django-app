FROM python:3.8
WORKDIR /myapp
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY manage.py ./
COPY memories ./memories
COPY memoriesproject ./memoriesproject
ARG SECRET_KEY=SECRET_KEY
ARG SOCIAL_AUTH_FACEBOOK_KEY=SOCIAL_AUTH_FACEBOOK_KEY
ARG SOCIAL_AUTH_FACEBOOK_SECRET=SOCIAL_AUTH_FACEBOOK_SECRET
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
