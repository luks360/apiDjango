from api.models import User

class Tests(): 
    def test_allUsers():
        users = User.objects.all()
        assert users == {}

    def test_specificUser():
        user = User.objects.filter(id=44)
        assert user == {
            "id": 44,
            "name": "Lucas Santos",
            "email": "santoslucasantos796@gmail.com",
            "password": None
        }

    