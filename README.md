# Random Notes

A simple Flask web application where people leave anonymous notes and receive a random note written by someone else.

## How It Works

1. A visitor writes and submits a note.
2. Their note is added to the note pool.
3. The application randomly selects a note from the pool.
4. The selected note is shown to the visitor.
5. If there are **4 or more notes**, the displayed note is removed from the pool.
6. If there are **fewer than 4 notes**, no notes are removed.

This keeps a small pool of notes available even when there aren't many users.

## Features

* 📝 Leave notes through a simple web interface
* 🎲 Receive a randomly selected note
* 💾 SQLite database for persistent storage
* 🔄 Notes are consumed only when the pool contains at least 4 notes
* 🌐 Built with Flask
* 📱 Simple responsive interface

## Project Structure

```text
random-notes/
├── app.py
├── notes.db
└── templates/
    ├── index.html
    └── note.html
```

`notes.db` is created automatically when the application is first started.

## Requirements

* Python 3.8+
* Flask

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/random-notes.git
cd random-notes
```

Install Flask:

```bash
pip install flask
```

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the address in your browser and leave a note.

## Note Pool Logic

The application intentionally does not consume notes while fewer than 4 notes exist.

For example:

```text
Pool: A B C
User submits: D

Pool becomes:
A B C D

Random note shown:
B

Pool becomes:
A C D
```

Because there were 4 notes, the displayed note is removed.

If the pool only contains three notes:

```text
A B C
```

a visitor can still receive a random note, but it remains in the pool.

This prevents the note pool from being completely depleted when the site has few users.

## Database

The application uses SQLite.

Each note is stored with:

* An automatically generated ID
* The note's content

The database is created automatically:

```text
notes.db
```

## Technologies

* **Python**
* **Flask**
* **SQLite**
* **HTML**
* **CSS**

## Future Ideas

Possible improvements include:

* Anonymous usernames or nicknames
* Note timestamps
* Preventing users from immediately receiving their own note
* Reporting inappropriate notes
* Note moderation
* Rate limiting
* A note counter
* AJAX-based submission without page reloads
* PostgreSQL support for production deployment
* Deployment to a public hosting service

## License

This project is open source. Add your preferred license here, such as MIT.
