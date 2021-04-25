# Library-Management-
Library management system

Heroku deployed website url :
https://redlib.herokuapp.com/

To run on local machine setup virtual environment and then inside the git folder do :

`pip install -r requirements.txt`

# Facebook Test User login credentials:

LoginID: lrittrmrpl_1618655789@tfbnw.net

Password: qwerty@1234

# Admin Login credentials:

Username : admin

Password : admin

# Dummy User Login Credentials:

There are 5 users with 

Username: useri where i in useri is from 1 to 5.

Password for all users is same qwerty@1234.

# SignUp:
Do try this for Google, Github and the normal Signup. Also do provide a real email as verification links will be sent. For facebook it will not work for any account as facebook only allows test users to login.

Also I would suggest to try to login using social on the deployed site only as i had changed the secret keys.

On Heroku I have uploaded one book but you will have to upload the image for the book again using edit book after login as there is some bug with the media files and each time the dyno is deactivated (which is 30 min for free account on heroku) it deletes the media files. I tried to install cloudinary but it created more errors so i reverted back
