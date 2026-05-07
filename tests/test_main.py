# ===== IMPORTS AND SETUP =====
# pytest: A testing framework for Python
# TestClient: Allows us to test FastAPI applications without running a real server
# sys & Path: Used to add the python_api directory to the import path

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add parent directory to path to import main
# This allows us to import the 'main' module from python_api/ directory
sys.path.insert(0, str(Path(__file__).parent.parent / "python_api"))

import main

# Create a test client for our FastAPI application
# This client simulates making HTTP requests without a live server
client = TestClient(main.app)


# ===== FIXTURES =====
# Fixtures are reusable setup/teardown functions that run before/after each test
# The autouse=True means this fixture runs automatically before EVERY test

@pytest.fixture(autouse=True)
def reset_db():
    """
    Reset the in-memory database before each test to ensure tests don't interfere with each other.
    
    Why this is important:
    - Each test should start with a clean state
    - Without this, test A might add data that affects test B
    - This ensures test isolation and predictable results
    """
    # Clear all existing data from the databases
    main.users_db.clear()
    main.missions_db.clear()
    
    # Reset the ID counters to their initial values
    # This ensures IDs start at 1 for each test
    main.next_user_id = 1
    main.next_mission_id = 1
    
    # yield: Pass control to the test, then run cleanup after the test finishes
    yield


# ===== USER ENDPOINT TESTS =====

def test_create_list_get_user():
    """
    Test the complete CRUD workflow for users: CREATE -> LIST -> GET
    
    This test verifies:
    1. Creating a new user returns status 200 (success)
    2. The created user gets an auto-generated ID
    3. We can list all users and get a list with 1 item
    4. We can retrieve a specific user by ID
    """
    # Step 1: Create a user with POST /users
    payload = {"name": "Alice", "job": "Engineer", "description": "Tests"}
    r = client.post("/users", json=payload)
    assert r.status_code == 200  # Verify the request succeeded
    
    # Parse the response and verify the returned user data
    user = r.json()
    assert user["id"] == 1  # First user should have ID 1
    assert user["name"] == "Alice"  # Verify the name was stored correctly

    # Step 2: List all users with GET /users
    r = client.get("/users")
    assert r.status_code == 200
    users = r.json()
    assert isinstance(users, list)  # Response should be a list
    assert len(users) == 1  # We created 1 user, so should have 1 in the list

    # Step 3: Get a specific user by ID with GET /users/1
    r = client.get("/users/1")
    assert r.status_code == 200
    got = r.json()
    assert got["name"] == "Alice"  # Verify we got the same user back

def test_update_and_delete_user():
    """
    Test UPDATE and DELETE operations for users.
    
    This test verifies:
    1. Creating a user works
    2. Updating an existing user changes their data
    3. Deleting a user removes them from the database
    4. Trying to get a deleted user returns 404 (not found)
    """
    # Step 1: Create a user
    payload = {"job": "Tester"}
    r = client.post("/users", json=payload)
    assert r.status_code == 200, "User creation should succeed, but {r.status_code} was returned. {r.text}" 

    # Step 2: Update the user with PUT /users/1
    update = {"name": "Bobby", "job": "Senior Tester", "description": "Updated"}
    r = client.put("/users/1", json=update)
    assert r.status_code == 200  # Update should succeed
    u = r.json()
    assert u["id"] == 1  # ID should remain the same
    assert u["name"] == "Bobby"  # Name should be updated

    # Step 3: Delete the user with DELETE /users/1
    r = client.delete("/users/1")
    assert r.status_code == 200
    data = r.json()
    assert data["message"] == "User deleted"  # Verify success message

    # Step 4: Verify the user is gone - GET /users/1 should now return 404
    r = client.get("/users/1")
    assert r.status_code == 404  # 404 = Not Found


def test_user_not_found():
    """
    Test error handling when requesting a non-existent user.
    
    This test verifies:
    - The API properly returns 404 when a user doesn't exist
    - The error response includes a 'detail' field with error information
    """
    # Try to get a user that doesn't exist (ID 999)
    r = client.get("/users/999")
    assert r.status_code == 404  # Should return 404 Not Found
    body = r.json()
    assert "detail" in body  # Error response should include 'message' field


# ===== MISSION ENDPOINT TESTS =====

def test_create_list_get_mission():
    """
    Test the complete CRUD workflow for missions: CREATE -> LIST -> GET
    
    Similar to test_create_list_get_user but for missions.
    """
    # Step 1: Create a mission with POST /missions
    payload = {"title": "Rescue", "target": "Site A", "successfull": False, "reward": 100.0, "agent": "Agent007"}
    r = client.post("/missions", json=payload)
    assert r.status_code == 200  # Verify the request succeeded
    
    mission = r.json()
    assert mission["id"] == 1  # First mission should have ID 1
    assert mission["title"] == "Rescue"

    # Step 2: List all missions with GET /missions
    r = client.get("/missions")
    assert r.status_code == 200
    missions = r.json()
    assert isinstance(missions, list)
    assert len(missions) == 1  # We created 1 mission

    # Step 3: Get a specific mission by ID with GET /missions/1
    r = client.get("/missions/1")
    assert r.status_code == 200
    got = r.json()
    assert got["agent"] == "Agent007"


def test_update_and_delete_mission():
    """
    Test UPDATE and DELETE operations for missions.
    
    Similar to test_update_and_delete_user but for missions.
    """
    # Step 1: Create a mission
    payload = {"title": "Recon", "successfull": True, "reward": 50.0, "agent": "AgentX"}
    r = client.post("/missions", json=payload)
    assert r.status_code == 200

    # Step 2: Update the mission with PUT /missions/1
    update = {"title": "Recon Updated", "successfull": True, "reward": 75.0, "agent": "AgentX"}
    r = client.put("/missions/1", json=update)
    assert r.status_code == 200
    m = r.json()
    assert m["id"] == 1
    assert m["title"] == "Recon Updated"

    # Step 3: Delete the mission with DELETE /missions/1
    r = client.delete("/missions/1")
    assert r.status_code == 200
    data = r.json()
    assert data["message"] == "Mission deleted"

    # Step 4: Verify the mission is gone
    r = client.get("/missions/1")
    assert r.status_code == 404


# ===== VALIDATION/ERROR HANDLING TESTS =====

def test_422_on_missing_required_field():
    """
    Test validation: API should reject incomplete data with 422 (Unprocessable Entity).
    
    This test verifies:
    - The API validates required fields
    - Missing required fields (like 'job') causes a 422 error
    - The error response includes a helpful message from our middleware
    
    Learning point: Always validate user input on the server side!
    """
    # Try to create a user without the required 'job' field
    payload = {"name": "NoJob"}  # Missing 'job' field!
    r = client.post("/users", json=payload)
    
    # Should return 422 (Unprocessable Entity) because the request is incomplete
    assert r.status_code == 422
    body = r.json()
    
    # Our middleware provides a helpful error message
    assert "message" in body


# ===== MAIN EXECUTION =====
# This block allows the file to be run directly with: python test_main.py

if __name__ == "__main__":
    import pytest

    # Run pytest with:
    # -q: quiet mode (less verbose output)
    # -p no:warnings: disable pytest warnings for cleaner output
    rc = pytest.main(["-q", "-p", "no:warnings"])
    
    # Print results to show if tests passed or failed
    if rc == 0:
        print("✓ All tests passed!")
    else:
        print(f"✗ Tests failed (exit code {rc})")
    
    raise SystemExit(rc)
