
from src.service.service_user import ServiceUser

#setup
users = {
    "Naruto": "jinchuuriki",
    "Sakura": "Chunnin",
    "Hinata": "Chunnin",
    "Rock lee": "Chunnin",
    "Neji": "Jounin",
    "Shikamaru": "Jounin"}

service = ServiceUser()
# for n, j in users.items():
#     service.add_user(name = n, job = j)

service.list_name_for_job('Chunnin')