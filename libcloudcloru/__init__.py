from libcloud.common.base import ConnectionKey, JsonResponse
from libcloud.common.types import InvalidCredsError
from libcloud.compute.base import KeyPair, NodeDriver, NodeImage, NodeLocation
from libcloud.utils.publickey import get_pubkey_openssh_fingerprint


class CloResponse(JsonResponse):
    def parse_error(self):
        body = super().parse_error()
        if body["code"] == 401:
            raise InvalidCredsError(body["error"]["message"])
        return body["error"]["message"]


class CloConnection(ConnectionKey):
    responseCls = CloResponse
    host = "api.clo.ru"

    def add_default_headers(self, headers) -> dict:
        headers["Accept"] = "application/json"
        headers["Authorization"] = f"Bearer {self.key}"
        return headers


class CloDriver(NodeDriver):
    connectionCls = CloConnection
    name = "CLO"
    website = "https://clo.ru/"

    # TODO: добавить NODE_STATE_MAP

    def list_locations(self):
        # https://clo.ru/about
        # По информации на сайте - ДЦ IXcellerate

        locations = [
            NodeLocation("IX", "IXcellerate", "RU", self),
        ]
        return locations

    def list_images(self):
        projects = self.connection.request("v1/projects")
        results = projects.object["results"]

        if not results:
            # TODO: Придумать ошибку получше
            raise Exception("there is no active projects")

        # TODO: проверять что проект ACTIVE

        project_id = results[0].id

        project_images = self.connection.request(f"/v1/projects/{project_id}/images")

        images = []
        for project_image in project_images.object["results"]:
            image = NodeImage(
                id=project_image.pop("id"),
                name=project_image.pop("name"),
                driver=self,
                extra=project_image,
            )
            images.append(image)

        return images

    def list_key_pairs(self):
        response = self.connection.request("v1/keypairs")
        key_pairs = []
        for kp in response.object["results"]:
            key_pair = KeyPair(
                name=kp["name"],
                public_key=kp["key"],
                fingerprint=get_pubkey_openssh_fingerprint(kp["key"]),
                driver=self,
                extra=dict(id=kp["id"]),
            )
            key_pairs.append(key_pair)
        return key_pairs
