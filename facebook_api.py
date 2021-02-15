import requests


def me():
    url = 'https://graph.facebook.com/v9.0/me'
    params = dict(
        fields='page_token,about,description_html,engagement,fan_count,posts{child_attachments,created_time,picture,shares,status_type,full_picture},picture',
        access_token='EAAEEQq7yp6gBANUomXZAaB6F4n96awIn3o9byyZCQvohbUtXZCn8sWjWWqA5DLTUTh4uEPIPsT0KLSYpgFBOQwxJv49LW4UH6VvoVOnfG2kM2AKfgTjgyTkOlzns1RLyKNZChNlV2ePUaqZBuPeIlx6itnKahSUrTDlBAah9LPXVIu6N7O2GzotcKFAkhu9DwXSddSZCwdl4bkV8ZB5UuXp'
    )
    print('test')

    resp = requests.get(url=url, params=params)
    # resp = requests.get(url=url)
    data = resp.json()
    print(data)


if __name__ == '__main__':
    me()
