from getpass import getpass
import vk

APP_ID = 6500844


def enter_login():
    return input('Enter your login:    ')


def enter_password():
    return getpass('Enter you password:   ')


def connect_vk(login, password,vk_api_version=5.78):
    session = vk.AuthSession(app_id=APP_ID,
                             user_login=login,
                             user_password=password,
                             scope='friends')
    return vk.API(session, v=vk_api_version, timeout=20)


def get_online_friends(vk_api):
    online_friends_ids = vk_api.friends.getOnline()
    return vk_api.users.get(user_ids=online_friends_ids)


def output_users(friends_are_online):
    if len(friends_are_online) == 0:
        print('There is not any friends to be online')
    else:
        print('The friends are online:  ')
        for friend in friends_are_online:
            print('{} {}'.format(friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = enter_login()
    password = enter_password()
    vk_api = connect_vk(login, password)
    friends_are_online = get_online_friends(vk_api)
    output_users(friends_are_online)
