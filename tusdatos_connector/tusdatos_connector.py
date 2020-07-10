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

    def launch_verify(self, payload):
        """In this endpoint, requests are made to validate a document by indicating its type (CC, CE, NIT, PP, NOMBRE).
        In this query only the full name of the person is returned, and if it is a valid document.
        If the date of issue of the document is sent it is also validated

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "fechaE": date as a string DD/MM/AAAA}

        Successful Response Schema

          {
            "email": "string",
            "doc": 0,
            "jobid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "nombre": "string",
            "typedoc": "string",
            "validado": true
          }
"""
        return self.api_post("/api/launch/verify", payload)

    def launch_car(self, payload):
        """In this endpoint the requests are made to initiate the consultation on the desired
        vehicle indicating the owner's document and its type (CC, CE, NIT, PP, NOMBRE), and
        the vehicle's licence plate.

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "placa": string}

        Successful Response Schema

          {
            "jobid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "revision": {
              "fechaRevision": "string",
              "fechaVencimiento": "string",
              "noRevision": "string",
              "placa": "string",
              "reqrtm": true,
              "valido": true,
              "vigente": true
            },
            "soat": {
              "fechaExpedicion": "string",
              "fechaInicio": "string",
              "fechaVencimiento": "string",
              "noSoat": "string",
              "valido": true,
              "vigente": true
            },
            "vehiculo": {
              "color": "string",
              "estado": "string",
              "fmatri": "string",
              "linea": "string",
              "marca": "string",
              "placa": "string",
              "valido": true
            }
          }
        """
        return self.api_post("/api/launch/car", payload)
