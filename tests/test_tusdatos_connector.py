#!/usr/bin/env python

"""Tests for `tusdatos_connector` package."""

import pytest


from tusdatos_connector import tusdatos_connector


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

    def launch(self, payload):
        """En este endpoint se realizan las peticiones para iniciar la consulta sobre el documento deseado indicando su tipo (CC, CE, NIT, PP, NOMBRE). La consulta se realiza en base al perfil asignado al usuario.
        Si la consulta ya fue realizada previamente tendrá una respuesta diferente, aplica para el caso de consultas de cédulas onsultadas en los últimos 15 días.

        Para pruebas podemos usar los siguientes ejemplos:

        CC:
        { "doc": 123, "typedoc": "CC", "fechaE": "01/12/2017" }

        CC (No validada):
        { "doc": 125, "typedoc": "CC", "fechaE": "13/11/2001" }

        CC (No validada inicialmente, retorna validado false pero al consultar el jobid retorna validado true):
        { "doc": 124, "typedoc": "CC", "fechaE": "03/04/2017" }

        CE:
        { "doc": 960696, "typedoc": "CE", "fechaE": "01/11/2001" }

        PEP:
        { "doc": 900000000000077, "typedoc": "PEP" }

        NIT:
        { "doc": 900000152, "typedoc": "NIT" }

        NOMBRE:
        { "nombre": "JUAN PEREZ PEREZ", "typedoc": "NOMBRE" }

        PP:
        { "doc": "381310014", "typedoc": "PP" }

        CC (Consultada previamente):
        { "doc": 126, "typedoc": "CC" }

        Code	Description	Links

Successful Response
    Schema

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
        """En este endpoint se realizan las peticiones para validar un documento indicando su tipo. En esta consulta se retorna únicamente el nombre completo de la persona, y si es un documento válido. Si se envía la fecha de expedición del documento esta es validada también


Successful Response
    Schema

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
        """En este endpoint se realizan las peticiones para iniciar la consulta sobre el vehiculo deseado indicando el documento del propietario y su tipo.
            Example Value:
{
  "doc": 123,
  "typedoc": "CC",
  "placa": "ABC123"
}

Successful Response
    Schema

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

    def retry(self, payload):
        """Reintentar la consulta para cargar las fuentes que presentaron algún error, este end point no descuenta consultas del plan.
        Debemos enviar el oid del reporte realizado anteriormente así como el tipo del documento (CC, CE, PEP, NOMBRE, PP, NIT).
        El oid es entregado por el endpoint /api/results. Como ejemplo de prueba podemos usar el oid: 7d1f10483800b5071688e101 con typedoc "CC"

id *
string
(path)

typedoc *
string
(query)

Successful Response
    Schema

{
  "doc": 0,
  "jobid": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
        """
        return self.api_get(f"/api/retry/{payload}")

    def results(self, payload):
        """Consulta del estado de la tarea en ejecución. En este endpoint se realiza la consulta del estado y resultado de la tarea en ejecucion. Para consultar el estado se debe enviar una petición get con parámetro el jobid.
El jobid es entregado por el endpoint /api/launch. El jobid tiene una vigencía de 4 horas, al finalizar este tiempo el endpoint responde que la tarea es inválida.
Podemos usar los jobid entregados en la documentación.

Otros ejemplos:
En proceso: 6769d210-3476-4c82-a044-045e9d5bc157
Finalizado: 6460fc34-4154-43db-9438-8c5a059304c0


Successful Response
    Schema

{
  "cedula": 0,
  "error": true,
  "errores": [
    "string"
  ],
  "estado": "string",
  "hallazgo": true,
  "hallazgos": "string",
  "id": "string",
  "nombre": "string",
  "results": {},
  "time": 0,
  "typedoc": "string",
  "validado": true
}
        """
        return self.api_get(f"/api/results/{payload}")

    def report(self, payload):
        """En este endpoint se genera el html del reporte. Para recibir el html se debe enviar una petición get con el id del reporte deseado. El id del reporte es obtenido del resultado de la consulta en el endpoint /api/results/{job-id}.
Como ejemplo podemos usar el id: 5d9e00483800a5071688a101

"""
        return self.api_get(f"/api/report/{payload}")

    def report_pdf(self, payload):
        """En este endpoint se genera un archivo en pdf del reporte. Para recibir el pdf se debe enviar una petición get con el id del reporte deseado. El id del reporte es obtenido del resultado de la consulta en el endpoint /api/results/{job-id}.
Como ejemplo podemos usar el id: 5d9e00483800a5071688a101
"""
        return self.api_get(f"/api/report_pdf/{payload}")

    def report_nit(self, payload):
        """En este endpoint se genera el html del reporte de empresas. Para recibir el html se debe enviar una petición get con el id del reporte deseado. El id del reporte es obtenido del resultado de la consulta en el endpoint /api/results/{job-id}.
Como ejemplo podemos usar el oid: 5d9e05963817a56d989523c0
"""
        return self.api_get(f"/api/report_nit/{payload}")

    def report_nit_pdf(self, payload):
        """En este endpoint se genera un archivo en pdf del reporte de empresas. Para recibir el pdf se debe enviar una petición get con el id del reporte deseado. El id del reporte es obtenido del resultado de la consulta en el endpoint /api/results/{job-id}.
Como ejemplo podemos usar el oid: 5d9e05963817a56d989523c0
"""
        return self.api_get(f"/api/report_nit_pdf/{payload}")

    def report_json(self, payload):
        """En este endpoint se genera el json del reporte. Para recibir el json se debe enviar una petición get con el id del reporte deseado. El id del reporte es obtenido del resultado de la consulta en el endpoint /api/results/{job-id}.
Como ejemplo podemos usar los siguientes oids:
CC: 5d9e00483800a5071688a101
NIT: 5d9e05963817a56d989523c0
"""
        return self.api_get(f"/api/report_json/{payload}")

    def get_plans(self):
        """En este endpoint se puede consultar el estado del plan actual del usuario. Para conocer el estado del plan se debe enviar una petición get sin parámetros.
        Successful Response
    Schema

{
  "amount": 0,
  "purchase_amount": 0,
  "purchase_date": "string",
  "user": "string"
}
        """
        return self.api_get("/api/plans")

    def get_querys(self):
        """En este endpoint se puede consultar la cantidad de consultas previas realizadas por el usuario. Para conocer el número de consultas se debe enviar una petición get sin parámetros."""
        return self.api_get("/api/querys")
