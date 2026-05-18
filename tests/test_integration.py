def test_signup_then_unregister_workflow(client):
    activity_name = "Programming Class"
    email = "workflow.student@mergington.edu"

    signup_response = client.post(
        "/activities/Programming%20Class/signup",
        params={"email": email},
    )
    assert signup_response.status_code == 200

    after_signup = client.get("/activities").json()[activity_name]["participants"]
    assert email in after_signup

    unregister_response = client.delete(
        "/activities/Programming%20Class/participants",
        params={"email": email},
    )
    assert unregister_response.status_code == 200

    after_unregister = client.get("/activities").json()[activity_name]["participants"]
    assert email not in after_unregister
