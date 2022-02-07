# Chat App Django

This app joins with other repos in my learning of Django, the app still needs to be polished to be "perfect" but many of the things are practically finished, I hope this project seems interesting to you and try to improve it.

# Requirements

Basic python knowledge and the pip requirements for this proyect:
```
pip install -r requirements.txt
```
# Usage

For run the server just:
```
python manage.py runserver
```
> This will be open the app on `127.0.0.1:8000`

Exmaple use of the Api:
```js
let getRooms = async () => {
let response = await fetch('http://127.0.0.1:8000/api/rooms/')
let rooms = await response.json()

for (let i = 0; rooms.length > i; i++) {
  let room = rooms[i]

  let row = `<div>
            <h3>${room.name}</h3>
            </div>`

  roomsContainer.innerHTML += row
  }
  }
```

# How it works

The app is designed for create, update and delete Rooms for chat whit other users, you can create and udpate your own user and manage your messages. In a few words you can use the database in CRUD methodology. You can host this app with some ways read about that... NOTE: When  you run the server create a [admin](https://www.geeksforgeeks.org/how-to-create-superuser-in-django/) user for manage the admin panel. 

# Contributing

Just open a pull request with the changes, and if they look good, I'll merge it.

# License
MIT
