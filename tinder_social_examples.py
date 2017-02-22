import pynder
import config

session = pynder.Session(
    facebook_id=config.fb_id,
    facebook_token=config.fb_token)
friends = session.get_fb_friends()

# Print the names of all facebook friends using Tinder Social.
print(", ".join([x.name for x in friends]))

# Get the user_info of these facebook friends.
user_info_objects = []
for friend in friends:
    user_info_objects.append(friend.get_tinder_information())

# Print the bios.
for user_info, friend in zip(user_info_objects, friends):
    print("=" * 50)
    # Use Friend.name, as user_info.name only contains first name.
    print(friend.name)
    print(friend.facebook_link)
    print("-" * 50)
    print(user_info.bio)
print("=" * 50)
