# HandyBot 🤖

A Telegram bot built with **Python** and **aiogram**, designed to automate order management and provide a convenient interface for users and administrators. The project follows a modular architecture, making it easy to maintain and extend.

## ✨ Features

* User-friendly Telegram interface
* Order creation and management
* SQLite database integration
* FSM (Finite State Machine) support for multi-step dialogs
* Admin functionality
* Docker support for easy deployment
* Environment-based configuration
* Modular project structure

## 🛠 Tech Stack

* Python 3.11+
* aiogram
* SQLite
* Docker & Docker Compose
* asyncio
* python-dotenv

## 📂 Project Structure

```
.
├── app/
│   ├── database/
│   ├── filters/
│   ├── handlers/
│   ├── keyboards/
│   ├── middlewares/
│   ├── services/
│   ├── states/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── run.py
```

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/goatzillla/HandyBot.git
cd HandyBot
```

### Create environment variables

Create a `.env` file based on `.env.example`.

Example:

```env
BOT_TOKEN=your_bot_token
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the bot

```bash
python run.py
```

## 🐳 Running with Docker

Build and start the application:

```bash
docker compose up --build
```

## 📌 Environment Variables

| Variable    | Description               |
| ----------- | ------------------------- |
| `BOT_TOKEN` | Telegram Bot API token    |

## 📈 Future Improvements

* PostgreSQL support
* Redis caching
* Localization (multi-language support)
* Unit and integration tests
* CI/CD pipeline
* Web admin panel

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

Feel free to fork the repository and submit a pull request.

## 📄 License

This project is distributed under the MIT License.