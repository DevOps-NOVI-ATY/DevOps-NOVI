from .test_main import client

def test_karakter_status_code():
    response = client.get("/characters/")
    assert response.status_code == 200

def test_karakter_response():
    response = client.get("/characters/")
    assert response.json() == [{"name":"spider-man"},{"name":"x-men"},{"name":"avengers"},{"name":"iron man"},{"name":"thor"},
                               {"name":"black widow"},{"name":"captain america"},{"name":"hulk"},{"name":"guardians of the galaxy"},
                               {"name":"daredevil"},{"name":"fantastic four"},{"name":"wolverine"},{"name":"doctor strange"},
                               {"name":"ms. marvel"},{"name":"batman"},{"name":"superman"},{"name":"wonder woman"},{"name":"the flash"},
                               {"name":"aquaman"},{"name":"green lantern"},{"name":"batgirl"},{"name":"green arrow"},{"name":"teen titans"},
                               {"name":"hellboy"},{"name":"b.p.r.d. agents"},{"name":"marv"},{"name":"dwight mccarthy"},
                               {"name":"usagi yojimbo"},{"name":"the goon"},{"name":"black hammer"},{"name":"spawn"},{"name":"rick grimes"},
                               {"name":"invincible"},{"name":"alana"},{"name":"maika halfwolf"}]

