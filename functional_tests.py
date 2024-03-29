import tomli
import json
import requests

# load username and password for test
with open('secrets.toml', 'rb') as f:
    secrets = tomli.load(f)

"""
Here are examples of calls to the api
"""
if __name__ == "__main__":
    base_url = secrets["test_server"]["base_url"]

    ######## EXAMPLE CALL
    # Post username and password to /api/v1/token-auth

    body = {
        "username": secrets["test_user"]["username"], 
        "password": secrets["test_user"]["password"]
    }
    
    ######## 

    # pull out token to send on subsequent requests
    response = requests.post(
            base_url + "token-auth", 
            json=body
    )
    token = json.loads(response.content)["token"]


    #### Example call for user info

    response = requests.get(
        base_url + "whoami",
        headers={"Authorization": f"Token {token}"}
    )

    assert json.loads(response.content)["pk"] is not None


    # Check base endpoint
    response = requests.get(base_url, 
        headers={"Authorization": f"Token {token}"})
    
    assert "lessons" in json.loads(response.content).keys()
    assert "sections" in json.loads(response.content).keys()
    assert "resources" in json.loads(response.content).keys()

    response = requests.get(base_url + "home", 
        headers={"Authorization": f"Token {token}"})

    home_view = json.loads(response.content)

    next_url = home_view["next_section"]["detail_url"]
    response = requests.get(base_url + next_url,
        headers={"Authorization": f"Token {token}"})
    
    section_obj = json.loads(response.content)

    # GRADES - This is how you mark a section complete

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

    # TIPS

    ######## EXAMPLE POST CALL 
    # Post new tip to endpoint /api/v1/tips/
    # Slide id is found on each slide object

    body = {
        "section": section_obj["id"],
        "slide_id": "23bc49dc-f684-4128-96a7-1e840aed613d",
        "body": "Hello, I thought that this might pelp hout."
    }

    ########

    response = requests.post(
        base_url + "tips/",
        headers={"Authorization": f"Token {token}"},
        json=body
    )

    response = requests.get(base_url + "tips/?slide_id=23bc49dc-f684-4128-96a7-1e840aed613d",
        headers={"Authorization": f"Token {token}"})

    tips_obj = json.loads(response.content)
    items = tips_obj["items"]

    tip = items[0]
    id = tip["id"]
    
    ######## EXAMPLE UPDATE CALL
    # Post tip updates to endpoint /api/v1/tips/{tip_pk}/
    # must have trailing '/' !

    body={
        "body": "Hello, I thought that this might help out."
    }

    ########

    response = requests.post(
        base_url + f"tips/{id}/",
        headers={"Authorization": f"Token {token}"},
        json=body
    )

    response = requests.get(base_url + "tips/?slide_id=23bc49dc-f684-4128-96a7-1e840aed613d",
        headers={"Authorization": f"Token {token}"})

    tips_obj = json.loads(response.content)

    print(tips_obj["items"])
