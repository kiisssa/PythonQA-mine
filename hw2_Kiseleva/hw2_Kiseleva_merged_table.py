import csv
import pytest
import json

with open('users.json', 'r') as user_file:   #open json as a file
    users = list(   #making dictionary from json
        json.loads(
            user_file.read()
        )
    )

with open('books-39204-271043.csv', 'r') as booksFile:     #open csv as a file
    books = list(               #making dictionary from csv
        csv.DictReader(booksFile)    #only reading csv, special method
    )

preformatUsers = list()  #creating third list, where commoin list users+books are supposed to be displayed

for userIndex, user in enumerate(users):   #start cycle for users. counting users with enumerate method. itering users
    book = books[userIndex] if len(books) >= userIndex else []   #counting books. userIndex is corresponding to book index. counting number of books
                                                                   #if the number of books is less than users answering []
    preformatBook = {                   #writing the example of json file for book how it would be look like
        'title': book['Title'],
        'author': book['Author'],
        'height': book['Height']
    } if isinstance(book, dict) else []    #compare if book is dict

    preformatUser = {                   #writing the example of json file for user
        'name': user['name'],
        'gender': user['gender'],
        'address': user['address'],
        'books': preformatBook      #attaching json file for book with user
    }

    preformatUsers.append(preformatUser)   #attaching users in one list

with open('mergedUsersAndBooks.json', 'w') as mergedFile:    #creating and opening final list of users+books
    json.dump(preformatUsers, mergedFile)    #making json file
