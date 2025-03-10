
# tgBotTemplate

## Overview
This repository contains a template for building a Telegram bot using Python. The structure is designed to be modular, scalable, and easy to extend. It includes handlers for both admin and user commands, middleware for additional processing, utilities for configuration, and a database layer for persistent storage.

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
  - [i18n](#i18n)
  - [database](#database)
    - [requests](#requests)
  - [main.py](#mainpy)
- [Usage](#usage)

## Installation
To get started with this template, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/pukeeee/tgBot-Template.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

### app/core
The `core` directory contains essential components that are used throughout the application. For instance, it may include initialization scripts or core functionalities.

### app/middlewares
Middleware functions can be defined in the `middlewares` directory. These functions are executed before the actual handler functions and can be used for tasks like logging, authentication, etc.
- `__init__.py`: Initialization script for the middleware package.
- `example.py`: An example middleware function.

### app/utils
Utility functions and configurations are stored in the `utils` directory.
- `config.py`: Configuration settings for the bot.
- `example.py`: Example utility function.

### app/handlers
Handlers are responsible for processing incoming messages and commands from Telegram users. They are organized into subdirectories based on the type of user (admin/user).

#### admin
Admin-specific handlers are placed in the `admin` directory.
- `__init__.py`: Initialization script for the admin handlers.
- `commands/__init__.py`: Initialization script for admin commands.
- `commands/example.py`: Example admin command handler.

#### user
User-specific handlers are placed in the `user` directory.
- `__init__.py`: Initialization script for the user handlers.
- `commands/__init__.py`: Initialization script for user commands.
- `commands/example.py`: Example user command handler.

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

### i18n
The `i18n` directory is used for internationalization, allowing the bot to support multiple languages.

### database
Database-related files are stored in the `database` directory.

#### requests
Requests to the database are organized in the `requests` subdirectory.
- `admin_requests.py`: Functions for making admin-related database requests.
- `user_requests.py`: Functions for making user-related database requests.
- `models.py`: Database models definitions.
- `repository.py`: Repository layer for database operations.

### main.py
The entry point of the application. This file initializes the bot and starts listening for incoming messages.

## Usage
To run the bot, simply execute the `main.py` script:
```bash
python main.py
```
