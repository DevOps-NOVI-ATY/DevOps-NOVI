from fastapi import HTTPException
from .connection import start_session
from ..Models.models import comics, series, characters, covers
from sqlalchemy import select

#Return 404 not found when no there are results
def return_or_404(resource, result):
    if result is None:
        raise HTTPException(status_code=404, detail=f"{resource} not found")
    else:
        if len(result) > 0:
            return result
        else:
            return None


#Get all rows of a particular model
def get_all(model):

    db = start_session()

    result = db.query(model).all()
    db.close()

    return return_or_404(resource="", result=result)

#Get all comic books
def get_all_comics():
    db = start_session()

    stmt = select(series, comics, characters, covers)\
        .join(comics.characters)\
        .join(comics.covers)\
        .join(comics.series)\
        
    
    result_objects = db.execute(stmt).fetchall()

    result =[]

    #remove '_sa_instance_state' from rows
    for tup in result_objects:
        temp = {key:val for key, val in tup[1].__dict__.items() if key != '_sa_instance_state'}
        temp['series'] = {key:val for key, val in tup[0].__dict__.items() if key != '_sa_instance_state'}
        temp['characters'] = {key:val for key, val in tup[2].__dict__.items() if key != '_sa_instance_state'}
        temp['covers'] = {key:val for key, val in tup[3].__dict__.items() if key != '_sa_instance_state'}

        result.append(temp)


    db.close()

    return return_or_404(resource="", result=result)

#Get filtered comic books
def get_filtered_comics(query):
    
    all_comics = get_all_comics()

    #list to save filtered comic books
    filtered_comics = []

    for comic in all_comics:

        check = True

        #check if attributes of comic book matches
        for key, value in query.items():

            #convert '+' to spaces
            if "+" in value:
                value.replace("+", " ")
            

            if key == 'publisher':
                #if attribute of comic book doesn't match, skip this comic book 
                if comic['series']['publisher'] != value:
                    check = False
                    break

            elif key == 'serie':
                if comic['series']['name'] != value:
                    check = False
                    break

            elif key == 'comic':
                if comic['name'] != value:
                    check = False
                    break

            elif key == 'character':
                if comic['characters']['name'] != value:
                    check = False
                    break

            elif key == 'cover':
                if comic['covers']['type'] != value:
                    check = False
                    break
                        

        # save comic if all attributes match            
        if check:
            filtered_comics.append(comic)
    
    #check if comics have to be in release order
    if "volgorde" in query:
        filtered_comics = sorted(filtered_comics, key= lambda i: i["release"])
    
    return return_or_404(resource="", result=filtered_comics)


def filtered_series(filter):

    db = start_session()

    #check if filter is size or publisher
    if filter.isdigit():
        result = db.query(series).filter(series.size == int(filter)).all()     
    else:
        #convert '+' to spaces
        if "+" in filter:
            filter.replace("+", " ")

        result = db.query(series).filter(series.publisher == filter).all()
    
    db.close()
    
    return return_or_404(resource="", result=result)


