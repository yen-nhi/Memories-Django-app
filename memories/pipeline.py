from memories.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == "facebook":
        if not Profile.objects.filter(uid=response['id']).exists():
        # The main part is how to get the profile picture URL and then do what you need to do
            avatar_url = f"https://graph.facebook.com/{response['id']}/picture/?type=large&access_token={response['access_token']}"
            Profile.objects.create(user=user, uid=response['id'], avatar=avatar_url)
