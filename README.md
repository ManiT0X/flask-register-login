# Flask User Authentication Example  
This is an example project that demonstrates how to implement user authentication in Flask using a database to store user information and login attempts.
The project provides a simple register and login form for users to create and authenticate their accounts.  
  
![Flask-Registration](https://user-images.githubusercontent.com/120915619/232897107-b75d8ad9-2ab8-4201-b377-660831db90b9.png)  
![Flask-Login](https://user-images.githubusercontent.com/120915619/232897099-5ad4ac7d-d7f1-4068-9b80-5b00ee3d009f.png)  
![Profile](https://user-images.githubusercontent.com/120915619/232897114-2f730e69-bd2c-4b99-bc4e-211a2d528ab1.png)  
  
## Requirements
To run this project, you will need the following installed on your system:

- Python 3  
- Flask  
- SQLAlchemy  

## Database Schema  
The database used in this project has two tables:  
- users: The users table stores user information such as the username, password, and email address.  
- log: The log table stores information about each login attempt, including the username, timestamp, and success status.
