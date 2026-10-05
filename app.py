from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__)

DATABASE = "notes.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note", "").strip()

        if not note:
            return redirect(url_for("index"))

        conn = get_db()

        # Add the new note
        conn.execute(
            "INSERT INTO notes (content) VALUES (?)",
            (note,)
        )
        conn.commit()

        # Get all notes
        notes = conn.execute(
            "SELECT id, content FROM notes"
        ).fetchall()

        if notes:
            # Pick a random note
            selected = random.choice(notes)

            # Only remove the note if there are at least 4 notes
            if len(notes) >= 4:
                conn.execute(
                    "DELETE FROM notes WHERE id = ?",
                    (selected["id"],)
                )
                conn.commit()

        else:
            selected = None

        conn.close()

        return render_template(
            "note.html",
            note=selected["content"] if selected else None
        )

    return render_template("index.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
