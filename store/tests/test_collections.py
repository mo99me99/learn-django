from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestCreateCollection:

    #AAA (Arrange, Act, Assert)
    # @pytest.mark.skip
    # @pytest.mark.skip
    def test_if_user_is_ananymous_return_401(self):
        #Arrange

        #Act
        client = APIClient()
        response = client.post('/store/collections/',{'title':'a'})

        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_if_user_is_not_admin_return_403(self):
            #Arrange

            #Act
            client = APIClient()
            client.force_authenticate(user={})
            response = client.post('/store/collections/',{'title':'a'})

            #Assert
            assert response.status_code == status.HTTP_403_FORBIDDEN
