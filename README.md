# Memories Django application

Web-app following requirements of Saritasa interview test

Member: Nguyen Thi Yen Nhi
Time start: 07 Jan 2022
Time finish: 11 Jan 2022
Description: A web-app developed base on Django framework, allow user login with Facebook account, create and save their memories.
Languages: Python, HTML, CSS, Javascripts.
Tested: Nguyen Thi Yen Nhi

## Docker compose locally
```
cd tools
docker-compose build
SECRET_KEY=<secret key value> SOCIAL_AUTH_FACEBOOK_KEY=<facebook key value> SOCIAL_AUTH_FACEBOOK_SECRET=<facebook secret value>  docker-compose up
```