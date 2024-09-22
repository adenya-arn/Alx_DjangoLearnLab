Register
Endpoint: /api/register
Method: POST

{
  "username": "your_username",
  "email": "your_email@example.com",
  "password": "your_password"
}
Returns token successful registration


Login
Endpoint: /api/login
Method: POST

{
  "username": "your_username",
  "password": "your_password"
}
Returns token successful login if unsuccessfl returns error details