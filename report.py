import pynder
import config


def notify_match(id, match, me):
    print('{} matches your account {}'.format(match, me))
    pass


def notify_message(id, msg, sender, me):
    print('  message from {}: {}'.format(sender, msg))
    pass


def report_news():

    session = pynder.Session(
        facebook_id=config.fb_id,
        facebook_token=config.fb_token)

    me = session.profile
    matches = session.matches()

    for match in matches:
        match_name = match.user.name
        notify_match(match.id, match_name, me)
        for msg in match.messages:
            # don't report messages send by me
            if msg.sender.id != me.id:
                notify_message(msg._data['_id'], msg.body, match_name, me)


if __name__ == '__main__':
    try:
        report_news()
    except Exception as e:
        print('error: {} ... maybe try again laster?'.format(e))
