from fastapi.testclient import TestClient
from performance_test import api  

client = TestClient(api)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


def test_add_ticket():
    ticket_data = {
        "id": 1,
        "flight_name": "Air Asia",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Singapore"
    }
    response = client.post("/ticket", json=ticket_data)
    assert response.status_code == 200
    assert response.json() == ticket_data


def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    tickets = response.json()
    assert isinstance(tickets, list)
    assert len(tickets) > 0  

