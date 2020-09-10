# Question 7
def getUsernames(threshold):
    # Write your code here
    import requests
    users_list = list()
    response = requests.get(
        f'https://jsonmock.hackerrank.com/api/article_users')
    response = response.json()
    total_pages = response['total_pages']
    for num in range(1, total_pages+1):
        response = requests.get(
            f'https://jsonmock.hackerrank.com/api/article_users?page={num}')
        response = response.json()
        for user in response['data']:
            if user['submission_count'] > threshold:
                users_list.append(user['username'])
    return users_list


def main(threshold):
    return getUsernames(threshold)
