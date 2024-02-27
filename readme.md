# Role-Based Authentication with Django Custom User Model

This Django application implements a custom user model to extend the superuser and registration process with additional role-based fields. It provides role-based authentication, where authentication tokens are generated upon successful login, and the role of the authenticated user is embedded in the token payload.

## Features

1. **Custom User Model**: Utilizes Django's custom user model to extend user attributes, facilitating role-based authentication and authorization.

2. **Role-Based Authentication**: Upon successful authentication, the system generates an authentication token. This token carries the user's role information in its payload.

3. **Stateless Authentication**: The role embedded within the authentication token enables stateless authentication in other microservices. This allows these services to define access and perform authentication based on the user's role without the need for additional database queries.

## Usage

To utilize this application, follow these steps:

1. Install the necessary dependencies mentioned in `requirements.txt`.
   
2. Configure the Django settings file (`settings.py`) to use the custom user model and specify authentication settings, including token expiration time, etc.

3. Implement the necessary endpoints for user registration, login, and token verification as per your application's requirements.

4. Ensure proper error handling and security measures, especially in handling authentication tokens and sensitive user information.

5. Use the role information embedded in the authentication token to define access and perform authentication in other microservices in your architecture.

## Example Code Snippet

```python
# Django View for User Authentication


