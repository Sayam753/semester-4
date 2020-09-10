# Question 6
def numDevices(statusQuery, threshold, dateStr):
    # Write your code here
    import requests
    import datetime
    total_devices = 0
    given_month, given_year = list(map(int, dateStr.split("-")))
    response = requests.get(
        f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}')
    response = response.json()
    total_pages = response['total_pages']
    for num in range(1, total_pages+1):
        response = requests.get(
            f'https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={num}')
        response = response.json()
        for device in response['data']:
            time = datetime.datetime.fromtimestamp(device['timestamp']/1000.0)
            month, year = time.month, time.year
            params = device['operatingParams']
            if params['rootThreshold'] > threshold and month == given_month and year == given_year:
                total_devices += 1
    return total_devices


def main(statusQuery, threshold, dateStr):
    return numDevices(statusQuery, threshold, dateStr)
