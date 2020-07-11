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
        self.session.headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        self.session.auth = auth

    def api_post(self, command, payload):
        return self.session.post(f"{self.url}{command}", json=payload).json()

    def api_get(self, command, payload):
        return self.session.get(f"{self.url}{command}", params=payload).json()

    def launch(self, payload):
        """In this endpoint the requests are made to initiate the consultation on the desired document
        indicating its type (CC, CE, NIT, PP, NOMBRE). The query is made based on the profile assigned
        to the user. If the query has already been made, it will have a different answer. This applies
        in the case of queries on the documents consulted in the last 15 days.

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "fechaE": date as a string DD/MM/AAAA}
        """
        return self.api_post("/api/launch", payload)

    def launch_verify(self, payload):
        """In this endpoint, requests are made to validate a document by indicating its type (CC, CE, NIT, PP, NOMBRE).
        In this query only the full name of the person is returned, and if it is a valid document.
        If the date of issue of the document is sent it is also validated

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "fechaE": date as a string DD/MM/AAAA}
        """
        return self.api_post("/api/launch/verify", payload)

    def launch_car(self, payload):
        """In this endpoint the requests are made to initiate the consultation on the desired
        vehicle indicating the owner's document and its type (CC, CE, NIT, PP, NOMBRE), and
        the vehicle's licence plate.

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"doc": int, "typedoc": type, "placa": string}
        """
        return self.api_post("/api/launch/car", payload)

    def retry(self, payload):
        """Retry the consultation to load the sources that presented some error, this end point
        does not discount consultations of the plan. We must send the oid of the report delivered
        by the endpoint /api/results previously, as well as the type of document (CC, CE, PEP, NAME, PP, NIT).

        :param payload: Required.
                        The parameter recieves a dictionary with the following keys:
                        {"id": string, "typedoc": type}
        """
        return self.api_get(
            f"/api/retry/{payload.get('id')}", {"typedoc": payload.get("typedoc")}
        )

    def results(self, payload):
        """Consultation of the status of the task currently running. This endpoint returns the status
        and result of a given task in execution. Considerations:
        - The jobid is delivered by the endpoint /api/launch.
        - The jobid has a validity of 4 hours, at the end of this time the endpoint answers that the task is invalid.
        """
        return self.api_get(f"/api/results/{payload}")

    def report(self, payload):
        """In this endpoint the report's html is generated. To receive the html you must send a get request
        with the id of the desired report. The id of the report is obtained from the result of the query in
        the endpoint /api/results/{job-id}.
        """
        return self.api_get(f"/api/report/{payload}")

    def report_pdf(self, payload):
        """This endpoint generates a pdf file of the report. In order to receive the pdf, a get request
        must be sent with the id of the desired report. The id of the report is obtained from the result of
        the query in the endpoint /api/results/{job-id}.
        """
        return self.api_get(f"/api/report_pdf/{payload}")

    def report_nit(self, payload):
        """This endpoint generates the html of the business report. To receive the html you must send a
        get request with the id of the desired report. The id of the report is obtained from the result
        of the consultation in the endpoint /api/results/{job-id}.
        """
        return self.api_get(f"/api/report_nit/{payload}")

    def report_nit_pdf(self, payload):
        """This endpoint generates a pdf file of the business report. To receive the pdf file, you must
        send a get request with the id of the desired report. The id of the report is obtained from the
        result of the consultation in the endpoint /api/results/{job-id}.
        """
        return self.api_get(f"/api/report_nit_pdf/{payload}")

    def report_json(self, payload):
        """In this endpoint the report json is generated. To receive the json, you must send a get request
        with the id of the desired report. The id of the report is obtained from the result of the query
        in the endpoint /api/results/{job-id}.
        """
        return self.api_get(f"/api/report_json/{payload}")

    def get_plans(self):
        """In this endpoint you can check the status of the user's current plan. To know the status of
        the plan you must send a get request without parameters.
        """
        return self.api_get("/api/plans")

    def get_querys(self):
        """In this endpoint you can consult the number of previous consultations made by the user.
        To know the number of queries a get request without parameters must be sent.
        """
        return self.api_get("/api/querys")
