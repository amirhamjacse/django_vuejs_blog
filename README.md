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
