# Portfolio Website – Built with FastAPI and HTML/CSS

### Project Structure
```
    static
        style
            style.css
       js
            index.js
    templates
        index.html
        login.html
    app
        alembic
        routers
            auth.py
            crud.py
            user.py
        config.py
        database.py
        main.py
        models.py
        oauth2.py
        schemas.py
        utils.py
    LICENSE
    requirements.txt
    .gitignore
    README.md
```

I developed a simple and secure ToDo application featuring a FastAPI backend with database integration and a login/signup system using HTML/CSS for the frontend.

### Key features

- **CRUD**Add, update, delete, and view tasks
- **User Authentication:** Login page with secure password handling
- **Database Integration** to persist user and task data
Intuitive and responsive design for a smooth user experience


### Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Setup your HTML file in templates folder
   ```
   create an index.html and login.html file in the templates folder
   ```

3. Start the application in development mode:
   ```
   uvicorn app.main:app --reload
   ```

4. Test the application by making requests to endpoints.


### Technologies Used:
- **Backend:** FastAPI (Python)

- **Frontend:** HTML, CSS

- **Database:** PostgreSQL (default) or any other FastAPI-compatible database

- **Authentication:** Secure login/signup flow using JWT tokens

- **Deployment:** Deployed on https://todo.a.7o7.cx for public access, with proper version control using Git.

### Database Setup
This app uses a PostgreSQL database by default. You can change the database settings in main.py to use other databases like MySQL. The database stores both user credentials and task data.

### API Endpoints
- **Authentication:**
POST /auth/login: Authenticate a user and issue a JWT.
POST /auth/signup: Register a new user.

- **Tasks:**
GET /tasks: Retrieve all tasks for the authenticated user.
POST /tasks: Create a new task.
PUT /tasks/{id}: Update an existing task by ID.
DELETE /tasks/{id}: Delete a task by ID.

### Usage
- **User Registration:** Register a new account on the login page.
- **Login:** Log in with your registered credentials.
- **Manage Tasks:** Add, update status of todo, or delete tasks associated with your account.

### Security
JWT Authentication: Protects user sessions with JSON Web Tokens.
Password Hashing: User passwords are securely hashed before storing in the database.

### Future Enhancements
Password Reset: Add a password recovery option.
Task Sorting and Filtering: Allow users to organize tasks by priority or due date.
Collaborative Tasks: Share tasks with other registered users.


For detailed information, refer to the following resources:

- FastAPI documentation: https://fastapi.tiangolo.com/

### Contact Me:
If you have any questions or would like to collaborate, please feel free to reach out to me through:
- **Email:** abdulkid151@gmail.com
- **LinkedIn Profile:** https://www.linkedin.com/in/abdulhakeem-raji-097619279