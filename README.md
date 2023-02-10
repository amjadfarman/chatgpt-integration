# App to show ChatGPT integration
This simple project is a Flask application that has got ChatGPT integrated with.
The project is designed and tested to run in Python 3.9. The package
requirements are listed in the `requirements.txt` file.

## Dependencies
This project needs the following environment variable set up before runnning it

```bash
CHATGPT_KEY=the_secret_key
```
Here `the_secret_key` is your personal key to communicate with API of the ChatGPT.
You will have to register at [OpenAI](https://platform.openai.com/overview)
to generate the key from
[OpenAI API Key](https://platform.openai.com/account/api-keys).

## How to run the project
Once you have installed and met all the requirements, the project can be run by
executing the following command from the project directory

```bash
flask run
```
## Note
This project is not designed to run in a production environment.
