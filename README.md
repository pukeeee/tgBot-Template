
# tgBotTemplate

## Overview
This repository contains a template for building a Telegram bot using Python. The structure is designed to be modular, scalable, and easy to extend. It includes handlers for both admin and user commands, middleware for additional processing, utilities for configuration, and a database layer for persistent storage. Perfect for developers looking to create feature-rich Telegram bots quickly and efficiently.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
  - [app/core](#appcore)
    - [app/middlewares](#appmiddlewares)
    - [app/utils](#apputils)
  - [app/handlers](#apphandlers)
    - [admin](#admin)
    - [user](#user)
  - [app/keyboards](#appkeyboards)
    - [admin](#admin-1)
    - [user](#user-1)
  - [l10n](#l10n)
  - [database](#database)
    - [requests](#requests)
  - [main.py](#mainpy)
- [Notes and Support](#notes-and-support)

---

## Installation
To get started with this template, follow these steps:

#### Local Execution
To run the bot locally:
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Start the bot:  
   ```bash
   python main.py
   ```

#### Docker Execution
1. Build the Docker image:  
   ```bash
   docker build -t my-telegram-bot .
   ```
2. Run the Docker container:  
   ```bash
   docker run --name telegram-bot-container my-telegram-bot
   ```

--- 

## Project Structure
```plaintext
tgBot-Template/
├── app/
│   ├── core/
│   │   ├── middlewares/
│   │   │   ├── __init__.py
│   │   │   ├── example.py
│   │   │   └── i10n_middleware.py
│   │   └── utils/
│   │       └── config.py
│   │
│   ├── handlers/
│   │   ├── admin/
│   │   │   ├── __init__.py
│   │   │   └── example.py
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   └── example.py
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── example.py
│   │
│   ├── keyboards/
│   │   ├── admin/
│   │   │   ├── __init__.py
│   │   │   └── example.py
│   │   └── user/
│   │       ├── __init__.py
│   │       └── example.py
│   │
│   └── l10n/
│       ├── en.ftl
│       └── l10n.py
│
├── database/
│   ├── models.py
│   ├── repository.py
│   └── requests/
│       ├── admin_requests.py
│       └── user_requests.py
│
├── .gitignore
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md 
```
---

### app/core
The `core` directory contains essential components that are used throughout the application. For instance, it may include initialization scripts or core functionalities.

### app/middlewares
Middleware functions can be defined in the `middlewares` directory. These functions are executed before the actual handler functions and can be used for tasks like logging, authentication, etc.
- `__init__.py`: Initialization script for the middleware package.
- `example.py`: An example middleware function.
- `i10n_middleware.py`: Middleware for determining the user's language.

### app/utils
Utility functions and configurations are stored in the `utils` directory.
- `config.py`: Configuration settings for the bot.
- `example.py`: Example utility function.

---

### app/handlers
Handlers are responsible for processing incoming messages and commands from Telegram users. They are organized into subdirectories based on the type of user (admin/user).

#### admin
Admin-specific handlers are placed in the `admin` directory.
- `__init__.py`: Initialization script for the admin handlers.
- `example.py`: Example admin command handler.

#### user
User-specific handlers are placed in the `user` directory.
- `__init__.py`: Initialization script for the user handlers.
- `example.py`: Example user command handler.

#### commands
Command handlers are placed in the commands directory. These handle specific commands for both admin and regular users.
- `__init__.py`: Initialization script for command handlers.
- `example.py`: Example command handler.

---

### app/keyboards
Keyboards define the layout of buttons that appear in the Telegram chat interface. They are also organized by user type.

#### admin
Admin-specific keyboards are placed in the `admin` directory.
- `__init__.py`: Initialization script for the admin keyboards.
- `example.py`: Example admin keyboard definition.

#### user
User-specific keyboards are placed in the `user` directory.
- `__init__.py`: Initialization script for the user keyboards.
- `example.py`: Example user keyboard definition.

---

### l10n
The `l10n` directory is used for localization, allowing the bot to support multiple languages. It includes a sample localization file en.ftl for English content.

---

### database
Database-related files are stored in the `database` directory.

#### requests
Requests to the database are organized in the `requests` subdirectory.
- `admin_requests.py`: Functions for making admin-related database requests.
- `user_requests.py`: Functions for making user-related database requests.
- `models.py`: Database models definitions.
- `repository.py`: Repository layer for database operations.

---

### main.py
The entry point of the application. This file initializes the bot and starts listening for incoming messages.

---

## Notes and Support
If you have any questions, suggestions, or encounter issues while using this bot, feel free to open an issue on the GitHub repository or contact the developer directly. Contributions and feedback are always welcome!
