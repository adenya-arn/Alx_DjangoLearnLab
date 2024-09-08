Author model represents an author who can have multiple books.
The name field stores the author's name


Book model represents a book with a title, publication year,
and a foreign key linking to an Author.


BookSerializer - Serializes all fields of the Book model.
Includes custom validation for publication_year to ensure it is not in the future


Author Serializer - Serializes the name field of the Author model and uses a nested BookSerializer to serialize related books dynamically


BookListView - This lists all books or creates a new book for authenticated users only

BookDetailView - Retrieves, updates or deletes a book it's set only to allow authenticated users only.


BookListView    List all books or create a new book.
                - Filtering by title, author, and publication_year.
                - Searching by title and author.
                - Ordering by title and publication_year


BookFilter      FilterSet for filtering Book model instances.
                - title: Case-insensitive search.
                - author: Case-insensitive search.
                - publication_year: Exact match.   