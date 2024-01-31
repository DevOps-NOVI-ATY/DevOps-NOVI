from .test_main import client


#Tests for endpoint /characters
def test_characters_status_code():
    response = client.get("/characters/")
    assert response.status_code == 200

def test_characters_response():
    response = client.get("/characters/")
    assert response.json() == [{"name":"spider-man"},{"name":"x-men"},{"name":"avengers"},{"name":"iron man"},{"name":"thor"},
                               {"name":"black widow"},{"name":"captain america"},{"name":"hulk"},{"name":"guardians of the galaxy"},
                               {"name":"daredevil"},{"name":"fantastic four"},{"name":"wolverine"},{"name":"doctor strange"},
                               {"name":"ms. marvel"},{"name":"batman"},{"name":"superman"},{"name":"wonder woman"},{"name":"the flash"},
                               {"name":"aquaman"},{"name":"green lantern"},{"name":"batgirl"},{"name":"green arrow"},{"name":"teen titans"},
                               {"name":"hellboy"},{"name":"b.p.r.d. agents"},{"name":"marv"},{"name":"dwight mccarthy"},
                               {"name":"usagi yojimbo"},{"name":"the goon"},{"name":"black hammer"},{"name":"spawn"},{"name":"rick grimes"},
                               {"name":"invincible"},{"name":"alana"},{"name":"maika halfwolf"}]



#Tests for endpoint /comics
def test_comics_status_code():
    response = client.get("/comics/")
    assert response.status_code == 200

def test_comics_status_code_404():
    response = client.get("/comics/?characters=unknown")
    assert response.status_code == 404

def test_comics_response_filtered():
    response = client.get("/comics/?character=black+widow")
    assert response.json() == [{"name":"red room redemption","pages":32,"issue":1,"release":"2023-01-12","price":3.99,"series":{"size":3,"publisher":"marvel","name":"black widow: deadly origin"},"characters":{"name":"black widow"},"covers":{"type":"softcover"}},
                               {"name":"the widow's gambit","pages":32,"issue":2,"release":"2023-02-12","price":3.99,"series":{"size":3,"publisher":"marvel","name":"black widow: deadly origin"},"characters":{"name":"black widow"},"covers":{"type":"softcover"}},
                               {"name":"assassin's legacy","pages":32,"issue":3,"release":"2023-03-12","price":3.99,"series":{"size":3,"publisher":"marvel","name":"black widow: deadly origin"},"characters":{"name":"black widow"},"covers":{"type":"softcover"}}]

def test_comics_response_sorted():
    response = client.get("/comics/?publisher=image+comics&sorted")
    assert response.json() == [{"name":"the al simmons saga","pages":30,"issue":1,"release":"2023-01-18","price":4.25,"series":{"size":3,"publisher":"image comics","name":"spawn"},"characters":{"name":"spawn"},"covers":{"type":"softcover"}},
                               {"name":"awakening","pages":30,"issue":1,"release":"2023-01-22","price":4.0,"series":{"size":3,"publisher":"image comics","name":"monstress"},"characters":{"name":"maika halfwolf"},"covers":{"type":"softcover"}},
                               {"name":"family matters","pages":32,"issue":1,"release":"2023-01-24","price":3.75,"series":{"size":3,"publisher":"image comics","name":"invincible"},"characters":{"name":"invincible"},"covers":{"type":"softcover"}},
                               {"name":"volume 1","pages":28,"issue":1,"release":"2023-01-28","price":3.25,"series":{"size":3,"publisher":"image comics","name":"saga"},"characters":{"name":"alana"},"covers":{"type":"softcover"}},
                               {"name":"days gone by","pages":28,"issue":1,"release":"2023-01-30","price":3.5,"series":{"size":3,"publisher":"image comics","name":"the walking dead"},"characters":{"name":"rick grimes"},"covers":{"type":"softcover"}},
                               {"name":"hellspawn redemption","pages":30,"issue":2,"release":"2023-02-18","price":4.25,"series":{"size":3,"publisher":"image comics","name":"spawn"},"characters":{"name":"spawn"},"covers":{"type":"softcover"}},
                               {"name":"the blood","pages":30,"issue":2,"release":"2023-02-22","price":4.0,"series":{"size":3,"publisher":"image comics","name":"monstress"},"characters":{"name":"maika halfwolf"},"covers":{"type":"softcover"}},
                               {"name":"viltrumite war","pages":32,"issue":2,"release":"2023-02-24","price":3.75,"series":{"size":3,"publisher":"image comics","name":"invincible"},"characters":{"name":"invincible"},"covers":{"type":"softcover"}},
                               {"name":"made to suffer","pages":28,"issue":2,"release":"2023-02-28","price":3.5,"series":{"size":3,"publisher":"image comics","name":"the walking dead"},"characters":{"name":"rick grimes"},"covers":{"type":"softcover"}},
                               {"name":"the war for phang","pages":28,"issue":2,"release":"2023-02-28","price":3.25,"series":{"size":3,"publisher":"image comics","name":"saga"},"characters":{"name":"alana"},"covers":{"type":"softcover"}},
                               {"name":"angelic warfare","pages":30,"issue":3,"release":"2023-03-18","price":4.25,"series":{"size":3,"publisher":"image comics","name":"spawn"},"characters":{"name":"spawn"},"covers":{"type":"softcover"}},
                               {"name":"haven","pages":30,"issue":3,"release":"2023-03-22","price":4.0,"series":{"size":3,"publisher":"image comics","name":"monstress"},"characters":{"name":"maika halfwolf"},"covers":{"type":"softcover"}},
                               {"name":"the end of all things","pages":32,"issue":3,"release":"2023-03-24","price":3.75,"series":{"size":3,"publisher":"image comics","name":"invincible"},"characters":{"name":"invincible"},"covers":{"type":"softcover"}},
                               {"name":"the last revolution","pages":28,"issue":3,"release":"2023-03-28","price":3.25,"series":{"size":3,"publisher":"image comics","name":"saga"},"characters":{"name":"alana"},"covers":{"type":"softcover"}},
                               {"name":"whispers into screams","pages":28,"issue":3,"release":"2023-03-30","price":3.5,"series":{"size":3,"publisher":"image comics","name":"the walking dead"},"characters":{"name":"rick grimes"},"covers":{"type":"softcover"}}]
    



#Tests for endpoint /publishers
def test_publishers_status_code():
    response = client.get("/publishers/")
    assert response.status_code == 200

def test_publishers_response():
    response = client.get("/publishers/")
    assert response.json() == [{"name":"marvel"},{"name":"dc comics"},{"name":"dark horse comics"},{"name":"image comics"}]


#Tests for endpoint /series
def test_series_status_code():
    response = client.get("/series/")
    assert response.status_code == 200

def test_series_status_code_404():
    response = client.get("/series/size/9")
    assert response.status_code == 404

def test_series_response():
    response = client.get("/series/")
    assert response.json() == [{"size":3,"publisher":"marvel","name":"the amazing spider-man"},{"size":3,"publisher":"marvel","name":"x-men: mutant genesis"},
                               {"size":3,"publisher":"marvel","name":"avengers assemble"},{"size":3,"publisher":"marvel","name":"iron man: armored adventures"},
                               {"size":3,"publisher":"marvel","name":"thor: god of thunder"},{"size":3,"publisher":"marvel","name":"black widow: deadly origin"},
                               {"size":3,"publisher":"marvel","name":"captain america: sentinel of liberty"},{"size":3,"publisher":"marvel","name":"hulk: smash and grab"},
                               {"size":3,"publisher":"marvel","name":"guardians of the galaxy: cosmic chronicles"},{"size":3,"publisher":"marvel","name":"daredevil: the man without fear"},
                               {"size":3,"publisher":"marvel","name":"fantastic four: future foundation"},{"size":3,"publisher":"marvel","name":"wolverine: weapon x"},
                               {"size":3,"publisher":"marvel","name":"doctor strange: mystic arts"},{"size":3,"publisher":"marvel","name":"ms. marvel: kamala's journey"},
                               {"size":3,"publisher":"dc comics","name":"batman: the dark knight"},{"size":3,"publisher":"dc comics","name":"superman: man of steel"},
                               {"size":3,"publisher":"dc comics","name":"wonder woman: princess of themyscira"},{"size":3,"publisher":"dc comics","name":"the flash: speed force"},
                               {"size":3,"publisher":"dc comics","name":"aquaman: king of atlantis"},{"size":3,"publisher":"dc comics","name":"green lantern: emerald corps"},
                               {"size":3,"publisher":"dc comics","name":"batgirl: gotham's guardian"},{"size":3,"publisher":"dc comics","name":"green arrow: the emerald archer"},
                               {"size":3,"publisher":"dc comics","name":"teen titans: titans together"},{"size":3,"publisher":"dark horse comics","name":"hellboy: seed of destruction"},
                               {"size":3,"publisher":"dark horse comics","name":"b.p.r.d.: plague of frogs"},{"size":3,"publisher":"dark horse comics","name":"sin city"},
                               {"size":3,"publisher":"dark horse comics","name":"usagi yojimbo"},{"size":3,"publisher":"dark horse comics","name":"the goon"},
                               {"size":3,"publisher":"dark horse comics","name":"black hammer"},{"size":3,"publisher":"image comics","name":"spawn"},
                               {"size":3,"publisher":"image comics","name":"the walking dead"},{"size":3,"publisher":"image comics","name":"invincible"},
                               {"size":3,"publisher":"image comics","name":"saga"},{"size":3,"publisher":"image comics","name":"monstress"}]

def test_series_response_filtered():
    response = client.get("/series/publisher/marvel")
    assert response.json() == [{"size":3,"publisher":"marvel","name":"the amazing spider-man"},{"size":3,"publisher":"marvel","name":"x-men: mutant genesis"},
                               {"size":3,"publisher":"marvel","name":"avengers assemble"},{"size":3,"publisher":"marvel","name":"iron man: armored adventures"},
                               {"size":3,"publisher":"marvel","name":"thor: god of thunder"},{"size":3,"publisher":"marvel","name":"black widow: deadly origin"},
                               {"size":3,"publisher":"marvel","name":"captain america: sentinel of liberty"},{"size":3,"publisher":"marvel","name":"hulk: smash and grab"},
                               {"size":3,"publisher":"marvel","name":"guardians of the galaxy: cosmic chronicles"},{"size":3,"publisher":"marvel","name":"daredevil: the man without fear"},
                               {"size":3,"publisher":"marvel","name":"fantastic four: future foundation"},{"size":3,"publisher":"marvel","name":"wolverine: weapon x"},
                               {"size":3,"publisher":"marvel","name":"doctor strange: mystic arts"},{"size":3,"publisher":"marvel","name":"ms. marvel: kamala's journey"}]