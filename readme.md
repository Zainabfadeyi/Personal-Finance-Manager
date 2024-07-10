# Finance Manager App

## Summary

The Finance Manager App is a comprehensive tool designed to help users manage their personal finances with ease and precision. It offers a wide range of functionalities, from tracking expenses and savings to setting and monitoring budgets. The app provides detailed analytics and insights, enabling users to make informed financial decisions and achieve their savings goals.

## Functionalities

### User Management
- **Registration and Authentication**: Users can easily register and log in to access their financial data securely.
- **Profile Management**: Users can view and update their personal information, ensuring their account remains up-to-date.

### Expense Tracking
- **Add and Manage Expenses**: Users can record and categorize their expenses, making it easy to track where their money is going.
- **Expense Analysis**: The app provides detailed reports on spending patterns, helping users identify areas for cost reduction.

### Savings Tracker
- **Savings Goals**: Users can set savings goals and monitor their progress, encouraging consistent saving habits.
- **Savings Insights**: Gain insights into savings trends over time, helping users adjust their strategies as needed.

### Budget Management
- **Budget Setting**: Users can create budgets for different categories, ensuring they stay within their spending limits.
- **Budget Tracking**: The app alerts users when they are close to exceeding their budgets, promoting disciplined spending.

### Analytics and Insights
- **Financial Overview**: Users receive a comprehensive overview of their finances, including expenses, savings, and budgets.
- **Custom Reports**: Generate custom reports to understand financial health better and make informed decisions.

### Security and Performance
- **Secure Transactions**: All data transactions are encrypted, ensuring user data is secure.
- **Optimized Performance**: The app is designed for fast, efficient operation, minimizing load times and improving user experience.

## Usage
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Just-Mike4/Personal-Finance-Manager.git
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Prepare the Database:**
    - Make migrations to create the database schema:
        - For Windows:
            ```bash
            python manage.py makemigrations
            ```
        - For macOS:
            ```bash
            python3 manage.py makemigrations
            ```
    - Apply the migrations to the database:
        - For Windows:
            ```bash
            python manage.py migrate
            ```
        - For macOS:
            ```bash
            python3 manage.py migrate
            ```
            
4. **Run the Server:**
    - For Windows:
        ```bash
        python manage.py runserver
        ```
    - For macOS:
        ```bash
        python3 manage.py runserver
        ```

## API Documentation
### API Endpoint for Seamless Interaction
Explore and interact with the application through the API, providing easy access to various functionalities.
- **Register User Endpoint:** `/api/auth/register` (Method: POST)
- **User Login Endpoint:** `/api/auth/login` (Method: POST)
- **Refresh Token Endpoint:**  `/api/auth/refresh` (Method: POST)
- **Expense Category Endpoint:**  `/api/expense-category/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Expense Endpoint:**  `/api/expense/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Savings Endpoint:**  `/api/saving/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Budget Endpoint:**  `/api/budget/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Account Endpoint:**  `/api/account/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Transaction Endpoint:**  `/api/transaction/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Goal Endpoint:**  `/api/goal/` (Method: GET,POST,PUT,PATCH,DELETE)
- **Notification Endpoint:**  `/api/notification/` (Method: GET,POST,PUT,PATCH,DELETE)

The API documentation is available at the following endpoints:

- **Register User:**
    - Endpoint: `/api/auth/register`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "email": "",
            "password1": "",
            "password2": ""
        }
        ```

    - Response Body: 
    ``` json
        {
            "refresh": "",
            "access": "",
        }
    ```

- **User Login:**
    - Endpoint: `/api/auth/login`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "username": "",
            "password": ""
        }
        ```
    - Response Body: 
    ``` json
        {
            "refresh": "",
            "access": "",
            "user": {
                "username": "",
                "email": ""
            }
        }
    ```

- **Refresh Token:**
    - Endpoint: `/api/auth/refresh`
    - Method: `POST`
    - Request Body:
        ```json
        {
            "refresh": "",
        }
        ```

    - Response Body: 
    ```json
        {
            "access": "",
        }
    ```

- **Expense Category:**
    - Endpoint: `/api/expense-category/`
    - Method: `GET`

    - Response Body: 
    ```json
        [
            {
                "id": "",
                "name": ""
            }
        ]
    ```

    - Method: `POST`
    - Request Body:
        ```json
        {
            "name": "",
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "name":"",
        }
    ```

- **Expense Endpoint:** 
    - Endpoint: `/api/expense/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "amount": "",
                "description": "",
                "date": "",
                "created_at": "",
                "category": "",
            }
        ]
    ```


    - Method: `POST` 
    - Request Body:
        ```json
        {
            "amount": "",
            "description": "",
            "date": "YYYY-MM-DD",
            "category": "primary key",
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "amount": "",
            "description": "",
            "date": "",
            "created_at": "",
            "category": "",
        }
    ```

- **Savings Endpoint:**  
    - Endpoint: `/api/saving/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "amount": "",
                "description": "",
                "date": "",
                "created_at": ""
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
            "amount": "",
            "date": "",
            "description": "",
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "amount": "",
            "description": "",
            "date": "",
            "created_at": ""
        }
    ```

- **Budget Endpoint:**  
    - Endpoint: `/api/budget/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "amount": "",
                "start_date": "",
                "end_date": "",
                "created_at": "",
                "category": ""
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
            "amount": "",
            "start_date": "",
            "end_date": "",
            "category": "PK",
        }
        ```

    - Response Body: 
    ```json
        {
             "id": "",
            "amount": "",
            "start_date": "",
            "end_date": "",
            "created_at": "",
            "category": ""
        }
    ```

- **Account Endpoint:** 
    - Endpoint:  `/api/account/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "name": "",
                "account_type": "",
                "balance": "",
                "created_at": ""
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
            "name":"",
            "account_type":"", 
            "balance":"optional,can be edited", 
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "name": "",
            "account_type": "",
            "balance": "",
            "created_at": ""
        }
    ```

- **Transaction Endpoint:**  
    - Endpoint: `/api/transaction/`
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "transaction_type": "",
                "category": "PK",
                "amount": "",
                "description": "",
                "transaction_date": "",
                "created_at": "",
                "account": "PK"
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
        "transaction_type": "",
        "category": "",
        "amount": "",
        "description": "",
        "transaction_date": "",
        "account": ""
        }
        ```

    - Response Body: 
    ```json
        {
        "id": "",
        "transaction_type": "",
        "category": "PK",
        "amount": "",
        "description": "",
        "transaction_date": "",
        "created_at": "",
        "account": "PK"
        }
    ```

- **Goal Endpoint:**  
    - Endpoint: `/api/goal/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "name": "",
                "target_amount": "",
                "current_amount": "",
                "due_date": "",
                "created_at": ""
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
            "name": "",
            "target_amount":"",
            "due_date":""
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "name": "",
            "target_amount": "",
            "current_amount": "",
            "due_date": "",
            "created_at": ""
        }
    ```

- **Notification Endpoint:**  
    - Endpoint: `/api/notification/` 
    - Method: `GET` 
    - Response Body: 
    ```json
        [
            {
                "id": "",
                "message": "",
                "is_read": "boolean",
                "created_at": ""
            }
        ]
    ```

    - Method: `POST` 
    - Request Body:
        ```json
        {
        "message":""
        }
        ```

    - Response Body: 
    ```json
        {
            "id": "",
            "message": "",
            "is_read": "boolean",
            "created_at": ""
        }
    ```

## Considerations

To ensure the app's reliability and security, several key considerations are addressed, including secure authentication, data validation, comprehensive error handling, data encryption, and performance optimization.

---

The Finance Manager App is your personal finance assistant, helping you keep track of your finances and make smarter financial decisions.