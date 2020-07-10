"""Main module."""
import requests


class TusDatosConnector:
    def __init__(self, auth):
        """
        Class constructor for the connector to TusDatos.co webservice with API REST. This connector implements all the
        available API methods. In case of a Validation Error with data or the call itself, the schema to be expected
        will look like the following:
        {
          "detail": [
            {
              "loc": [
                "string"
              ],
              "msg": "string",
              "type": "string"
            }
          ]
        }
        :param auth: Required. Tuple with two strings in the following order (<username>, <password>).
        """
        self.url = "https://dash-board.tusdatos.co"
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.auth = auth

    def api_post(self, command, payload):
        return self.session.post(f"{self.url}{command}", json=payload).json()

    def api_get(self, command):
        return self.session.get(f"{self.url}{command}").json()

    def launch(self, payload):
        """In this endpoint the requests are made to initiate the consultation on the desired document
        indicating its type (CC, CE, NIT, PP, NOMBRE). The query is made based on the profile assigned
        to the user. If the query has already been made, it will have a different answer. This applies
        in the case of queries on the documents consulted in the last 15 days.

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "fechaE": date as a string DD/MM/AAAA}

        Successful Response Schema:
          {
            "email": "string",
            "doc": 0,
            "jobid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "nombre": "string",
            "typedoc": "string",
            "validado": true
          }
        """
        return self.api_post("/api/launch", payload)
