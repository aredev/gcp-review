# Review app

This application should connect to the same database as the one that performs the translate operation.

- Create a .env file that specifies the following set of keys
+ DB_NAME=
+ DB_USERNAME=
+ DB_UNIX
+ DB_PASSWORD=secret
+ SECRET_KEY=

- The secret key is used to set up a CSRF token. In order to generate a secret copy the output from the execution of the ```openssl rand -base64 32``` command
- Clone the repo in cloud shell
- Deploy it to App Engine
- See what happens!