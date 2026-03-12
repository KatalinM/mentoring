import pytest

@pytest.fixture(autouse=True)
def clear_db():
    """
    Clear the in-memory database before each test to ensure tests don't interfere with each other.
    
    Why this is important:
    - Each test should start with a clean state
    - Without this, test A might add data that affects test B
    - This "autouse=True" ensures test isolation and predictable results
    """
    # Clear all existing data from the databases
    main.users_db.clear()
    main.missions_db.clear()
    
    # Reset the ID counters to their initial values
    # This ensures IDs start at 1 for each test
    main.next_user_id = 1
    main.next_mission_id = 1
    
@pytest.fixture 
def create_user():
    """
    Create a user and return its data for use in tests.
    
    This fixture can be used in any test that requires a user to already exist.
    It creates a user with known data and returns the created user object.
    """
    payload = {"name": "Bob", "job": "Tester", "description": "Test user", "id": 12345}
    r = client.post("/users", json=payload)
    assert r.status_code == 200  # Verify the request succeeded
    print("User created successfully with ID:", r.json()["id"])
    return r.json()  # Return the created user data for use in tests

def created_user_saved(create_user):
    """
    Here the create_user() method is used like a parameter, which means that the fixture 
    will be executed before this test runs, and the returned value from the fixture will be 
    passed to this test as the create_user argument.

    Verify that the user created by the create_user fixture is saved in the database.
    This test checks that the user returned by the create_user fixture can be retrieved
    from the list of users, confirming that it was successfully saved.
    """
    # Get the list of all users
    r = client.get("/users")
    users = r.json()
    # here we could list the users with print("Current users in database:", users)
    
    # Check if the created user is in the list of users
    for user in users:
        if user["id"] == create_user["id"]: # Check if the user ID matches the previously created user's 12345 ID
            print(f"User with ID {create_user['id']} found in database.")
            return True  # User found, test passes
    print(f"User with ID {create_user['id']} not found in database.")
    return False  # User not found, test fails