# askQ

askQ is a Quora-inspired Question and Answer (Q&A) platform built using Django. The platform allows users to post questions, answer questions, search questions and like answers.

## Installation

To run the Capital Quiz(Backend) locally, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/Rushikesh8/askQ.git
```

2. Change into the project directory:

```shell
cd askQ
```

3. Setup Django Environment:
    - Create a virtual environment and activate it.
    - Install the required Python packages:

```shell
pip install -r requirements.txt
```

4. Create a .env file:
    - In the project root directory, create a file named .env.
    - Install the required Python packages:

```shell
SECRET_KEY=your-secret-key
DEBUG=True
```

5. Migrate:
    - In the project root directory, run

```shell
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
    - In the project root directory, run

```shell
python manage.py runserver
```