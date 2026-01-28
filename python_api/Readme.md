# REST API Documentation

A FastAPI-based REST API for managing users and missions. This API provides complete CRUD (Create, Read, Update, Delete) operations for both users and missions.

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Install dependencies:**
```bash
pip install requests
pip install fastapi uvicorn pydantic
```

2. **Run the server:**
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive Documentation
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## Base URL
```
http://localhost:8000
```

---

## Endpoints

### USERS

#### 1. Create User
**Endpoint:** `POST /users`

**Description:** Create a new user with name and job title.

**Required Parameters:**
| Parameter | Type   | Description               |
|-----------|--------|---------------------------|
| `name`    | string | The name of the user      |
| `job`     | string | The job title of the user |

**Optional Parameters:**
| Parameter     | Type   | Description                |
|---------------|--------|----------------------------|
| `description` | string | The description of the job |

**Request Example:**
```json
{
  "name": "John Doe",
  "job": "Software Engineer",
  "description": "Senior backend developer"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "name": "John Doe",
  "job": "Software Engineer",
  "description": "Senior backend developer"
}
```

---

#### 2. List All Users
**Endpoint:** `GET /users`

**Description:** Retrieve a list of all users in the system.

**Parameters:** None

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "job": "Software Engineer",
    "description": "Senior backend developer"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "job": "Project Manager",
    "description": null
  }
]
```

---

#### 3. Get User by ID
**Endpoint:** `GET /users/{id}`

**Description:** Retrieve a specific user by their ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the user |

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "John Doe",
  "job": "Software Engineer",
  "description": "Senior backend developer"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "User not found"
}
```

---

#### 4. Update User
**Endpoint:** `PUT /users/{id}`

**Description:** Update an existing user's information.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the user |

**Request Body:**
```json
{
  "name": "John Doe Updated",
  "job": "Lead Software Engineer",
  "description": "Senior backend developer with 10+ years experience"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "John Doe Updated",
  "job": "Lead Software Engineer",
  "description": "Senior backend developer with 10+ years experience"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "User not found"
}
```

---

#### 5. Delete User
**Endpoint:** `DELETE /users/{id}`

**Description:** Remove a user from the system.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the user |

**Response (200 OK):**
```json
{
  "message": "User deleted",
  "user": {
    "id": 1,
    "name": "John Doe",
    "job": "Software Engineer",
    "description": "Senior backend developer"
  }
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "User not found"
}
```

---

### MISSIONS

#### 1. Create Mission
**Endpoint:** `POST /missions`

**Description:** Create a new mission with title, status, reward, and assigned agent.

**Required Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | string | The title of the mission |
| `successfull` | boolean | Whether the mission was successful (true/false) |
| `reward` | number | The amount of the reward in EUR |
| `agent` | string | The name of the agent assigned to the mission |

**Optional Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `target` | string | The target of the mission |

**Request Example:**
```json
{
  "title": "Secure Database Access",
  "target": "Company X Servers",
  "successfull": true,
  "reward": 5000.50,
  "agent": "Agent Smith"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "title": "Secure Database Access",
  "target": "Company X Servers",
  "successfull": true,
  "reward": 5000.50,
  "agent": "Agent Smith"
}
```

---

#### 2. List All Missions
**Endpoint:** `GET /missions`

**Description:** Retrieve a list of all missions in the system.

**Parameters:** None

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Secure Database Access",
    "target": "Company X Servers",
    "successfull": true,
    "reward": 5000.50,
    "agent": "Agent Smith"
  },
  {
    "id": 2,
    "title": "Infiltrate Building",
    "target": "Downtown Tower",
    "successfull": false,
    "reward": 3000,
    "agent": "Agent Jones"
  }
]
```

---

#### 3. Get Mission by ID
**Endpoint:** `GET /missions/{id}`

**Description:** Retrieve a specific mission by its ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the mission |

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Secure Database Access",
  "target": "Company X Servers",
  "successfull": true,
  "reward": 5000.50,
  "agent": "Agent Smith"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Mission not found"
}
```

---

#### 4. Update Mission
**Endpoint:** `PUT /missions/{id}`

**Description:** Update an existing mission's information.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the mission |

**Request Body:**
```json
{
  "title": "Secure Database Access - Priority",
  "target": "Company X Servers",
  "successfull": true,
  "reward": 7500,
  "agent": "Agent Smith"
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Secure Database Access - Priority",
  "target": "Company X Servers",
  "successfull": true,
  "reward": 7500,
  "agent": "Agent Smith"
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Mission not found"
}
```

---

#### 5. Delete Mission
**Endpoint:** `DELETE /missions/{id}`

**Description:** Remove a mission from the system.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | integer | The unique identifier of the mission |

**Response (200 OK):**
```json
{
  "message": "Mission deleted",
  "mission": {
    "id": 1,
    "title": "Secure Database Access",
    "target": "Company X Servers",
    "successfull": true,
    "reward": 5000.50,
    "agent": "Agent Smith"
  }
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Mission not found"
}
```

---

## Testing with Postman

### Example Requests

#### Create User
```
POST http://localhost:8000/users
Content-Type: application/json

{
  "name": "Alice Johnson",
  "job": "Data Scientist",
  "description": "Machine learning specialist"
}
```

#### Get All Users
```
GET http://localhost:8000/users
```

#### Get User by ID
```
GET http://localhost:8000/users/1
```

#### Update User
```
PUT http://localhost:8000/users/1
Content-Type: application/json

{
  "name": "Alice Johnson",
  "job": "Senior Data Scientist",
  "description": "ML specialist with 5+ years experience"
}
```

#### Delete User
```
DELETE http://localhost:8000/users/1
```

#### Create Mission
```
POST http://localhost:8000/missions
Content-Type: application/json

{
  "title": "Extract Files",
  "target": "Server Room B",
  "successfull": true,
  "reward": 2500,
  "agent": "Agent Brown"
}
```

#### Get All Missions
```
GET http://localhost:8000/missions
```

#### Get Mission by ID
```
GET http://localhost:8000/missions/1
```

#### Update Mission
```
PUT http://localhost:8000/missions/1
Content-Type: application/json

{
  "title": "Extract Files - Critical",
  "target": "Server Room B",
  "successfull": false,
  "reward": 3000,
  "agent": "Agent Brown"
}
```

#### Delete Mission
```
DELETE http://localhost:8000/missions/1
```

---

## HTTP Status Codes

| Status Code | Description                             |
|-------------|-----------------------------------------|
| 200         | OK - Request successful                 |
| 201         | Created - Resource created successfully |
| 400         | Bad Request - Invalid parameters        |
| 404         | Not Found - Resource not found          |
| 500         | Internal Server Error                   |

---

## Data Models

### User Model
```python
{
  "id": int (auto-generated),
  "name": str (required),
  "job": str (required),
  "description": str (optional, can be null)
}
```

### Mission Model
```python
{
  "id": int (auto-generated),
  "title": str (required),
  "target": str (optional, can be null),
  "successfull": bool (required),
  "reward": float (required),
  "agent": str (required)
}
```

---

## Quick Start

1. **Run the server on the default localhost:**
```bash
uvicorn main:app --reload
```

2. **Access the API:**
   - API Base URL: `http://localhost:8000`
   - Swagger UI (Interactive Docs): `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

3. **Test with Postman:**
   - Open Postman
   - Create requests to any of the endpoints listed above
   - Use the Base URL `http://localhost:8000`

4. **Stop the server:**
```bash
Ctrl+C
```

---

## Notes

- **ID Auto-generation:** IDs are automatically generated for new users and missions.
- **In-Memory Storage:** Data is stored in memory and will be lost when the server restarts. For production use, consider implementing a database.
- **Validation:** FastAPI automatically validates request data according to the Pydantic models.
- **CORS:** Currently, CORS is not configured. For frontend integration, add CORS middleware to `main.py`. 