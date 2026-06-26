# To-Do List App

A simple command-line to-do list application built with Python. Tasks are saved to a local JSON file so your list persists between runs.

## Features

- View all tasks with their completion status
- Add new tasks
- Mark tasks as complete
- Delete tasks
- Data automatically saved to `todos.json`

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone this repository
   ```
   git clone https://github.com/aarukumawat2112-debug/todo-app.git
   ```
2. Navigate into the project folder
   ```
   cd todo-app
   ```
3. Run the app
   ```
   python app.py
   ```
   (use `python3 app.py` on Mac/Linux if needed)

## Usage

When you run the app, you'll see a menu:

```
======= TO-DO LIST APP =======
1. View tasks
2. Add task
3. Mark task complete
4. Delete task
5. Exit
===============================
```

Type the number of the option you want and press Enter.

## Project Structure

```
todo-app/
├── app.py          # Main application code
├── todos.json      # Auto-generated file storing your tasks
└── README.md       # This file
```

## License

Free to use and modify.
