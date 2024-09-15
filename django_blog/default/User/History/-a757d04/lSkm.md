Registration
Users can register with a username, email, and password

Login/Logout
Users log in with their username and password Sessions are automatically handled by Django.

Profile Management 
Users can view their profile and update info

Security
Forms have a CSRF token and passwords are hashed


Creating Post(Only for authenticated logged in users)
Only for authenticated logged in users 
Navigate to /post/new/.
Fill in the title and content fields in the form.
Submit the form to create a new post

Editing Post(author can edit)
Navigate to the specific post’s detail page (e.g., /post/<int:pk>/).
If you are the author, click the "Edit" link to navigate to the edit form (/post/<int:pk>/edit/).
Modify the title and content fields and submit the form

Deleting post(author can delete only)
Navigate to the post’s detail page.
If you are the author, click the "Delete" link, which will navigate to the delete confirmation page (/post/<int:pk>/delete/).
Confirm the deletion by submitting the form.