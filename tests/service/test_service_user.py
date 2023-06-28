from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        # Setup
        name = "Kátia"
        job = "Engenheira"
        service = ServiceUser()
        expected_result = "User added"

        # Adding user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_add_user_invalid_name(self):
        # Setup
        name = None
        job = "Psicologo"
        service = ServiceUser()
        expected_result = "Invalid User"

        # Trying to add user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_add_user_invalid_job(self):
        # Setup
        name = "Kurenai"
        job = None
        service = ServiceUser()
        expected_result = "Invalid User"

        # Trying to add user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_add_user_invalid_name_character(self):
        # Setup
        name = 123456
        job = "Psicologo"
        service = ServiceUser()
        expected_result = "Invalid User"

        # Trying to add user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_add_user_invalid_job_character(self):
        # Setup
        name = "Naruto"
        job = 15874
        service = ServiceUser()
        expected_result = "Invalid User"

        # Trying to add user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_add_existing_user(self):
        # Setup
        name = "Gabriel"
        job = "Front end"
        service = ServiceUser()

        # Adding user
        service.add_user(name, job)

        expected_result = "User already exists"

        # Trying to add user
        result = service.add_user(name, job)

        assert result == expected_result

    def test_update_user_success(self):
        # Setup
        name = "Sakura Haruno"
        job = "Chunnin"
        service = ServiceUser()

        # Adding user
        service.add_user(name, job)

        # Updating user
        expected_result = "Job was updated"
        result = service.update_user(name, "Jounin")

        assert result == expected_result

    def test_update_user_invalid(self):
        # Setup
        name = "Sakura Haruno"
        service = ServiceUser()

        # Trying to update user
        expected_result = "User Name not found"
        result = service.update_user(name, "Jounin")

        assert result == expected_result

    def test_delete_user_success(self):
        # setup
        name = "Sasuke Uchiha"
        job = "Akatsuki"
        service = ServiceUser()

        # Adding user
        service.add_user(name, job)

        # Deleting user
        expected_result = "User was removed"
        result = service.delete_user(name)

        assert result == expected_result

    def test_delete_user_invalid(self):
        # setup
        name = "Rock lee"
        service = ServiceUser()

        # Trying to delete user
        expected_result = "User Name not found"
        result = service.delete_user(name)

        assert result == expected_result

    def test_list_name_for_job_success(self):
        # Setup
        users = {
            "Naruto": "Hokage",
            "Sakura": "Chunnin",
            "Hinata": "Chunnin",
            "Rock lee": "Chunnin",
            "Neji": "Jounin",
            "Shikamaru": "Jounin"
        }

        # Adding users
        service = ServiceUser()
        for n, j in users.items():
            service.add_user(name=n, job=j)
        expected_result = ['Sakura', 'Hinata', 'Rock lee']

        # Looking for job
        result = service.list_name_for_job("Chunnin")

        assert result == expected_result

    def test_list_name_for_job_empty(self):
        # setup
        users = {
            "Naruto": "Hokage",
            "Sakura": "Chunnin",
            "Hinata": "Chunnin",
            "Rock lee": "Chunnin",
            "Neji": "Jounin",
            "Shikamaru": "Jounin"
        }

        # Adding users
        service = ServiceUser()
        for n, j in users.items():
            service.add_user(name=n, job=j)
        expected_result = []

        # Looking for job
        result = service.list_name_for_job("Gennin")

        assert result == expected_result

    def test_check_user_success(self):
        # Setup
        name = "Nagato"
        job = "Mercenary"

        # Adding user
        service = ServiceUser()
        service.add_user(name, job)

        # Looking for name
        expected_result = "Nagato"
        result = service.check_user(name)

        assert result.name == expected_result

    def test_check_user_not_exist(self):
        # Setup
        name = "Pain"
        service = ServiceUser()

        # Looking for name
        result = service.check_user(name)

        assert result is None