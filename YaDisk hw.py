import requests

TOKEN = ''

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url=files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        data = self._get_upload_link(disk_file_path=disk_file_path)
        url = data.get('href')
        response = requests.put(url=url, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    data = ya.get_files_list()
    ya.upload_file_to_disk('test/test_20_06', 'file3.txt')