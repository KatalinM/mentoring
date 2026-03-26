# py_api_wSQLite

## About this project

`py_api_wSQLite` is a small Python REST API example that uses SQLite as its datastore.

It demonstrates a basic entity model for:
- **Agents** (entities that can perform work)
- **Missions** (tasks assigned to agents)

The repo includes:
- `py_api_wSQLite/main.py` - API application entrypoint
- `py_api_wSQLite/crud/agent_crud.py` and `mission_crud.py` - CRUD operations for agents + missions
- `py_api_wSQLite/data_models/agent.py` and `mission.py` - data model classes
- `py_api_wSQLite/routers/agent_router.py` and `mission_router.py` - HTTP route definitions
- `py_api_wSQLite/sqlite_db/*` - database setup and queries

## 🚀 Features

- Create, read, update, delete agents
- Create, read, update, delete missions
- Basic relationship: missions can be assigned to agents
- SQLite persistence (local file database)

## 🛠️ Run locally

1. First run the main.py for init your first couple entry

```powershell
cd ~\py_api_wSQLite
python main
```

2. Simply run the main.py for init the db and start the app

```powershell
cd ~\py_api_wSQLite
python main
```

3. Open Postman at `http://127.0.0.1:8000` (or port shown in logs).

## 🔍 API Endpoints (example patterns)

Assuming base URL `http://127.0.0.1:8000`.

# not every endpoint is ready at this time
Agents
- `GET /agents` - list all agents
- `GET /agents/{agent_id}` - get a single agent
- `POST /agents` - create agent
- `PUT /agents/{agent_id}` - update agent
- `DELETE /agents/{agent_id}` - remove agent

Missions
- `GET /missions` - list all missions
- `GET /missions/{mission_id}` - get a single mission
- `POST /missions` - create mission
- `PUT /missions/{mission_id}` - update mission
- `DELETE /missions/{mission_id}` - remove mission

> Confirm the exact route paths in `py_api_wSQLite/routers/*.py` and use JSON bodies accordingly.

## 📌 Notes

- If database file is created in the local folder, inspect it with `sqlite viewer` - you can install the VS Code plugin
    SQLite Viewer


Enjoy building agent/mission workflows with SQLite!
