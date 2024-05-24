from rest_framework.test import APIClient
from rest_framework import status

class TestCreateCollection:
    #AAA (Arrange, Act, Assert)

    def test_if_user_is_ananymous_return_401(self):
        #Arrange

        #Act
        client = APIClient()
        response = client.post('/store/collections/',{'title':'a'})

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

