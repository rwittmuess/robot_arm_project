from fastapi.testclient import TestClient
from app.api import router  # Correctly importing the router object
import numpy as np

client = TestClient(router)

def test_move_robot_valid_data():
    """Test with valid target angles and speed."""
    response = client.post("/move", json={"target_angles": [45, 30, 0, 0, 0, 0], "speed": 10.0})
    assert response.status_code == 200
    assert "frames" in response.json()
    assert "step_time" in response.json()

def test_move_robot_with_default_speed():
    """Test when speed is not specified (should use default speed)."""
    response = client.post("/move", json={"target_angles": [45, 30, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert "frames" in response.json()
    assert "step_time" in response.json()
    assert response.json()["step_time"] == 0.05  # Default step_time when speed is not provided

def test_move_robot_with_zero_angles():
    """Test when target_angles is a list of zero angles."""
    response = client.post("/move", json={"target_angles": [0, 0, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert "frames" in response.json()
    assert "step_time" in response.json()

def test_move_robot_boundary_angles():
    """Test boundary values for angles."""
    response = client.post("/move", json={"target_angles": [180, -180, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert "frames" in response.json()
    assert "step_time" in response.json()

    response = client.post("/move", json={"target_angles": [-180, 180, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert "frames" in response.json()
    assert "step_time" in response.json()

def test_move_robot_invalid_angles():
    """Test with invalid angles that should be capped, not rejected."""
    # Test if angles greater than 180 are capped to -180 (!!!) this is necessary becuase the robot arm has a range of -180 to 180 and overflowing would indicate the tendency to the opposite direction
    response = client.post("/move", json={"target_angles": [200, 0, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert response.json()["frames"]  # Ensure frames are returned
    
    assert response.json()["frames"][0][0] == -180

    response = client.post("/move", json={"target_angles": [-200, 0, 0, 0, 0, 0]})
    assert response.status_code == 200
    assert response.json()["frames"]  # Ensure frames are returned

    assert response.json()["frames"][0][0] == 180