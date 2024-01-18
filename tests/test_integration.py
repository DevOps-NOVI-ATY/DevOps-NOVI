from app.models.dbFunctions import startSession, closeSession, commitAndCloseSession, runSelectStatement
from sqlalchemy import select
from app.models.models import Karakter
from fastapi.testclient import TestClient
from .test_main import client

def test_karakter_status_code():
    response = client.get("/karakters/")
    assert response.status_code == 200

def test_karakter_response():
    response = client.get("/karakters/")
    assert response.json() == [{"Karakter":{"naam":"spider-man"}},{"Karakter":{"naam":"x-men"}},
                               {"Karakter":{"naam":"avengers"}},{"Karakter":{"naam":"iron man"}},
                               {"Karakter":{"naam":"thor"}},{"Karakter":{"naam":"black widow"}},
                               {"Karakter":{"naam":"captain america"}},{"Karakter":{"naam":"hulk"}},
                               {"Karakter":{"naam":"guardians of the galaxy"}},{"Karakter":{"naam":"daredevil"}},
                               {"Karakter":{"naam":"fantastic four"}},{"Karakter":{"naam":"wolverine"}},
                               {"Karakter":{"naam":"doctor strange"}},{"Karakter":{"naam":"ms. marvel"}},
                               {"Karakter":{"naam":"batman"}},{"Karakter":{"naam":"superman"}},{"Karakter":{"naam":"wonder woman"}},
                               {"Karakter":{"naam":"the flash"}},{"Karakter":{"naam":"aquaman"}},{"Karakter":{"naam":"green lantern"}},
                               {"Karakter":{"naam":"batgirl"}},{"Karakter":{"naam":"green arrow"}},{"Karakter":{"naam":"teen titans"}},
                               {"Karakter":{"naam":"hellboy"}},{"Karakter":{"naam":"b.p.r.d. agents"}},{"Karakter":{"naam":"marv"}},
                               {"Karakter":{"naam":"dwight mccarthy"}},{"Karakter":{"naam":"usagi yojimbo"}},
                               {"Karakter":{"naam":"the goon"}},{"Karakter":{"naam":"black hammer"}},
                               {"Karakter":{"naam":"spawn"}},{"Karakter":{"naam":"rick grimes"}},
                               {"Karakter":{"naam":"invincible"}},{"Karakter":{"naam":"alana"}},
                               {"Karakter":{"naam":"maika halfwolf"}}]

# def test_databaseIntegratie():
#     stmt = select(Karakter)
#     result = runSelectStatement(stmt)
#     print(result)
#     assert result == [{"Karakter":{"naam":"spider-man"}},{"Karakter":{"naam":"x-men"}},
#                         {"Karakter":{"naam":"avengers"}},{"Karakter":{"naam":"iron man"}},
#                         {"Karakter":{"naam":"thor"}},{"Karakter":{"naam":"black widow"}},
#                         {"Karakter":{"naam":"captain america"}},{"Karakter":{"naam":"hulk"}},
#                         {"Karakter":{"naam":"guardians of the galaxy"}},{"Karakter":{"naam":"daredevil"}},
#                         {"Karakter":{"naam":"fantastic four"}},{"Karakter":{"naam":"wolverine"}},
#                         {"Karakter":{"naam":"doctor strange"}},{"Karakter":{"naam":"ms. marvel"}},
#                         {"Karakter":{"naam":"batman"}},{"Karakter":{"naam":"superman"}},{"Karakter":{"naam":"wonder woman"}},
#                         {"Karakter":{"naam":"the flash"}},{"Karakter":{"naam":"aquaman"}},{"Karakter":{"naam":"green lantern"}},
#                         {"Karakter":{"naam":"batgirl"}},{"Karakter":{"naam":"green arrow"}},{"Karakter":{"naam":"teen titans"}},
#                         {"Karakter":{"naam":"hellboy"}},{"Karakter":{"naam":"b.p.r.d. agents"}},{"Karakter":{"naam":"marv"}},
#                         {"Karakter":{"naam":"dwight mccarthy"}},{"Karakter":{"naam":"usagi yojimbo"}},
#                         {"Karakter":{"naam":"the goon"}},{"Karakter":{"naam":"black hammer"}},
#                         {"Karakter":{"naam":"spawn"}},{"Karakter":{"naam":"rick grimes"}},
#                         {"Karakter":{"naam":"invincible"}},{"Karakter":{"naam":"alana"}},
#                         {"Karakter":{"naam":"maika halfwolf"}}]
