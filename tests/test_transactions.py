from fastapi import status

def test_upload_file(test_client):

    response = test_client.post("/upload",files={"file": open("dummy_transactions.csv", "rb")})

    assert response.status_code == status.HTTP_200_OK

def test_upload_file_incorrect_type(test_client):

    response = test_client.post("/upload",files={"file": open("requirements.txt", "rb")})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_get_transaction_summary_user(test_client):

    response = test_client.get("/summary/42")

    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert body["user_id"] == 42
    assert body["count"] == 983
    assert body["min"] == 5.11
    assert body["max"] == 499.58
    assert body["mean"] == 259.83836215666327

def test_get_transaction_summary_user_not_found(test_client):

    response = test_client.get("/summary/99999")

    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["count"] == 0
    assert body["min"] is None
    assert body["max"] is None
    assert body["mean"] is None

def test_get_transaction_summary_user_and_range(test_client):
    response = test_client.get("/summary/42",params={"time_start": "2024-09-20", "time_end": "2024-10-20"})

    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert body["user_id"] == 42
    assert body["start"]== "2024-09-20T00:00:00"
    assert body["end"] == "2024-10-20T00:00:00"
    assert body["count"] == 69
    assert body["min"] == 5.11
    assert body["max"] == 495.49
    assert body["mean"] == 243.49478260869566

    assert response.status_code == status.HTTP_200_OK

def test_get_transaction_summary_user_not_found_and_range(test_client):

    response = test_client.get("/summary/99999",params={"time_start": "2024-09-20", "time_end": "2024-10-20"})

    assert response.status_code == status.HTTP_200_OK
    body = response.json()
    assert body["start"] == "2024-09-20T00:00:00"
    assert body["end"] == "2024-10-20T00:00:00"
    assert body["count"] == 0
    assert body["min"] is None
    assert body["max"] is None
    assert body["mean"] is None
