import json
import requests
"""
Here are examples of calls to the api
"""
if __name__ == "__main__":
    base_url = "http://localhost:8000/api/v1/"
    
    ######## EXAMPLE CALL
    # Post username and password to /api/v1/token-auth

    body = {
        "username": "mikev", 
        "password": "c4ardPlayer"
    }
    
    ######## 

    # pull out token to send on subsequent requests
    response = requests.post(base_url + "token-auth", 
        data=body)

    token = json.loads(response.content)["token"]

    # Check base endpoint
    response = requests.get(base_url, 
        headers={"Authorization": f"Token {token}"})
    
    assert "lessons" in json.loads(response.content).keys()
    assert "sections" in json.loads(response.content).keys()
    assert "resources" in json.loads(response.content).keys()

    response = requests.get(base_url + "home/", 
        headers={"Authorization": f"Token {token}"})

    home_view = json.loads(response.content)

    next_url = home_view["next_section"]["detail_url"]
    response = requests.get(next_url,
        headers={"Authorization": f"Token {token}"})
    
    section_obj = json.loads(response.content)

    # GRADES

    ######## EXAMPLE POST CALL
    # Post 'grade' to endpoint /api/v1/grades/
    
    body = {
        "section": section_obj["id"], 
        "student": 2
    }

    ########

    response = requests.post(
        base_url + "grades/",
        headers={
            "Authorization": f"Token {token}",
        },
        json=body,
    )
    
    # Get notes

    response = requests.get(base_url + "notes/",
        headers={"Authorization": f"Token {token}"})

    
    # NOTES

    ######## EXAMPLE POST CALL 
    # Post new note to endpoint /api/v1/notes/
    
    body={
        "student":2,
        "section": section_obj["id"],
        "body": "Here is some text of a new note."
    }

    ########

    response = requests.post(
        base_url + "notes/",
        headers={"Authorization": f"Token {token}"},
        json=body
    )

    response = requests.get(base_url + "notes/",
        headers={"Authorization": f"Token {token}"})

    notes_obj = json.loads(response.content)
    items = notes_obj["items"]

    note = items[0]
    id = note["id"]
    
    ######## EXAMPLE UPDATE CALL
    # Post note updates to endpoint /api/v1/notes/{note_pk}/
    # must have trailing '/' !

    body={
        "body": "Here is new text of a older note."
    }

    ########

    response = requests.post(
        base_url + f"notes/{id}/",
        headers={"Authorization": f"Token {token}"},
        json=body
    )

