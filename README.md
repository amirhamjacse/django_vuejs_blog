```markdown
# Blog Project

This is a **Vue.js** blog project with a **Python** backend (using either **Django** or **Flask**) to serve the blog data via an API. The project features a simple blog where users can view a list of blog posts, read the full article, and view the truncated content on the homepage.

## Features

- Display a list of blog posts on the homepage.
- Show a truncated excerpt (first 6 words) of each post on the homepage.
- Read the full content of each post on a detailed page.
- Dynamic routing for each blog post using Vue Router.
- Fetch blog data from a Python-based API using **Axios**.

## Technologies Used

### Frontend:
- **Vue.js**: Frontend framework to build the application.
- **Vue Router**: Routing for handling page navigation.
- **Axios**: HTTP client for fetching blog data from an API.
- **Bootstrap**: For responsive layout and styling.

### Backend (Python):
- **Django** or **Flask** (depending on your choice): Backend framework for creating the API to serve blog data.
- **Django Rest Framework (DRF)** (for Django): A toolkit for building APIs in Django.
- **Flask-RESTful** (for Flask): Extension for Flask that adds support for quickly building REST APIs.

## Installation

### Prerequisites

Make sure you have the following installed:

- **Python 3.x** (Django or Flask backend)
- **Node.js** and **npm** (for the Vue.js frontend)
- **MySQL** or **PostgreSQL** (or any database of your choice)

### 1. Clone the repositories

Clone the frontend and backend repositories to your local machine.

```bash
# Clone the frontend Vue.js project
git clone https://github.com/your-username/blog-frontend.git
cd blog-frontend

# Clone the backend Python project (Django or Flask)
git clone https://github.com/your-username/blog-backend.git
cd blog-backend
```

### 2. Backend Setup (Python - Django or Flask)

#### Django Setup:

1. Navigate to the `blog-backend` folder:

   ```bash
   cd blog-backend
   ```

2. Create a Python virtual environment and activate it:

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies (Django and Django Rest Framework):

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Run migrations to create the necessary database tables:
     ```bash
     python manage.py migrate
     ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

   Your Django API will now be running at `http://127.0.0.1:8000/`.

#### Flask Setup:

1. Navigate to the `blog-backend` folder:

   ```bash
   cd blog-backend
   ```

2. Create a Python virtual environment and activate it:

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install the required dependencies (Flask and Flask-RESTful):

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask development server:
   ```bash
   python app.py
   ```

   Your Flask API will now be running at `http://127.0.0.1:5000/`.

### 3. Frontend Setup (Vue.js)

1. Navigate to the `blog-frontend` folder:

   ```bash
   cd blog-frontend
   ```

2. Install the required frontend dependencies:

   ```bash
   npm install
   ```

3. Start the Vue.js development server:

   ```bash
   npm run serve
   ```

   Your Vue.js application will now be running at `http://localhost:8080/`.

### 4. Update the API URL in the Frontend

Make sure to update the API URL in the `getBlogdata` method inside `Home.vue` (or wherever you're fetching blog data). For example, if your backend is running on Django at `http://127.0.0.1:8000/`, your API URL in the Vue app should look like this:

```javascript
const response = await axios.get('http://127.0.0.1:8000/blog/list/');
```

Or, if you are using Flask:

```javascript
const response = await axios.get('http://127.0.0.1:5000/blog/list/');
```

### Example API Response:

Here is an example of how the data should be returned from your API:

```json
{
  "results": [
    {
      "id": 1,
      "title": "Understanding Vue.js",
      "content": "Vue.js is a progressive JavaScript framework used for building user interfaces and single-page applications...",
      "image": "https://via.placeholder.com/400x200",
      "date": "October 10, 2024",
      "author": "John Doe"
    },
    {
      "id": 2,
      "title": "Exploring React.js",
      "content": "React.js is a popular JavaScript library for building fast and interactive user interfaces...",
      "image": "https://via.placeholder.com/400x200",
      "date": "October 12, 2024",
      "author": "Jane Smith"
    }
    // Additional posts...
  ]
}
```

### Blog Homepage Layout

The homepage will display a grid of blog posts (using Bootstrap cards), with a truncated excerpt (first 6 words) of each post. There will be a "Read More" button linking to the full post.

### Blog Post Detail Page

The blog post detail page will be accessible by navigating to `/post/:id`. For example:

```
http://localhost:8080/post/1
```

This page will show the full content of the selected blog post.

## Code Structure

### Frontend (Vue.js)

- `src/`
  - `components/` - Contains Vue components used in the project.
    - `Home.vue` - Displays the homepage with the list of blog posts.
    - `BlogDetail.vue` - Displays the full content of a blog post.
  - `router/` - Contains Vue Router configuration.
    - `index.js` - Defines routes for navigating between pages.
  - `assets/` - Store static files such as images, styles, etc.
  - `App.vue` - The root component of the Vue.js app.
  - `main.js` - The entry point for the Vue.js app.

### Backend (Python)

- `blog-backend/`
  - `manage.py` - Django management script for various operations.
  - `app.py` - Main entry point for the Flask app.
  - `blog/` - Folder containing models, views, and API logic for the blog.
  - `requirements.txt` - Python dependencies (Django, Flask, DRF, etc.).
  - `urls.py` (Django) - URL routing for your Django API.
  - `views.py` (Flask) - API routes and logic for your Flask API.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and create a pull request. Any contributions are welcome!

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add feature'`).
4. Push to your forked repository (`git push origin feature-name`).
5. Create a pull request from your forked repository to the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Vue.js for building the frontend.
- Django/Flask for the backend.
- Bootstrap for the responsive layout.
- Axios for making HTTP requests.

## Screenshoot

![Alt text](/screenshoot/1.png)
![Alt text](/screenshoot/3.png)
![Alt text](/screenshoot/2.png)
![Alt text](/screenshoot/4.png)

```


### Project Structure:

.
├── project
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── __pycache__
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── CONFIG
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── frontend
│   ├── eslint.config.js
│   ├── index.html
│   ├── jsconfig.json
│   ├── node_modules
│   ├── package.json
│   ├── package-lock.json
│   ├── public
│   ├── README.md
│   ├── src
│   └── vite.config.js
├── LICENSE
├── manage.py
├── README.md
└── requirements.txt

