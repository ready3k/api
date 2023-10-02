from api.client import Client
import json


class Api(Client):
    USERS = '/users'
    BASE_URL = 'https://reqres.in/api'

    def list_users(self):
        url = self.BASE_URL + self.USERS + '?page=2'
        return self.get(url)

    def single_user_not_found(self):
        """
        :method:    get
        :route      api/users/23
        :status:    404
        """
        url = self.BASE_URL + self.USERS + '/23'
        return self.get(url)

    def single_user(self):
        """
        :method:    get
        :route      api/users/2
        :status:    200
        """
        url = self.BASE_URL + self.USERS + '/2'
        return self.get(url)

    def create(self, name: str, job: str):
        """
        :method:    post
        :routs:     /api/users
        :status:    201
        :body:      {
                        "name": "",
                        "job": ""
                    }
        """
        url = self.BASE_URL + self.USERS
        payload = json.dumps({
            "name": F"{name}",
            "job": F"{job}"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        return self.post(url, headers, payload)

    def delete_user(self, id: int):
        """
        :method:    delete
        :routs:     /api/users
        :status:    204
        """
        url = self.BASE_URL + self.USERS + F"/{id}"
        return self.delete(url)


api = Api()
