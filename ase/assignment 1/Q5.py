# Question 5
def getArticleTitles(author):
    # Write your code here
    import requests
    articles_list = list()
    response = requests.get(
        f'https://jsonmock.hackerrank.com/api/articles?author={author}')
    response = response.json()
    total_pages = response['total_pages']
    for num in range(1, total_pages+1):
        response = requests.get(
            f'https://jsonmock.hackerrank.com/api/articles?author={author}&page={num}')
        response = response.json()
        for article in response['data']:
            if article['author'] == author:
                if article['title'] is None and article['story_title'] is None:
                    pass
                elif article['title']:
                    articles_list.append(article['title'])
                elif article['story_title']:
                    articles_list.append(article['story_title'])
    return articles_list


def main(author):
    return getArticleTitles(author)
