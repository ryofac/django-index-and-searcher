# Django Project: Indexer and Searcher

This project is a Django application based on [the indexer implementation activity](https://github.com/ryofac/patro-search) from the Analysis and Systems Development course for the Internet Programming 1 discipline.

It consists of a simple system for indexing and searching data on HTML websites, with an editable configuration file (`config.json`) that can only be modified when the application is initialized.

## Requirements

- Python 3.x
- Django 3.x or higher
- Other requirements specified in the `requirements.txt` file

## Initial Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ryofac/django-index-and-searcher.git
    cd django-index-and-searcher
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the database:**
    Adjust database settings in the `settings.py` file as needed.

4.  **Migrate the database:**
    ```bash
    python manage.py migrate
    ```

5.  **Edit the configuration file:**
    The `config.json` file is editable only when the application is initialized. Ensure that the necessary settings are correct before starting the application.

## How to Build

This project includes a `run.sh` script to build the application. Follow the steps below to use it:

1.  **Give execute permission to the script:**
    ```bash
    chmod +x run.sh
    ```

2.  **Execute the script:**
    ```bash
    ./run.sh
    ```

    The `run.sh` script will build the application and configure the environment as needed.

## Running the Project

To start the development server, use the command:

```bash
python manage.py runserver
```

The project will be available at `http://127.0.0.1:8000/`.

## Project Structure
-   **`buscador/`**: Directory containing the search logic.
-   **`buscador/indexer.py`**: File containing the indexing logic.
-   **`config/config.json`**: Configuration file, editable only at initialization.
-   **`run.sh`**: Script to build the project.
