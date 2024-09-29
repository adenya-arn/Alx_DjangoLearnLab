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


GET/api/posts/ Listing all posts

[
  {
    "id": 1,
    "author": "user1",
    "title": "First Post",
    "content": "This is the first post.",
    "created_at": "2024-09-27T10:00:00Z",
    "updated_at": "2024-09-27T10:00:00Z",
    "comments": []
  }
]


POST/api/posts/  Creating a post

{
  "title": "New Post",
  "content": "This is a new post."
}


