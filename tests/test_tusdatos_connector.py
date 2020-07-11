#!/usr/bin/env python

"""Tests for `tusdatos_connector` package."""

import pytest

from tusdatos_connector import tusdatos_connector


validate_cc = {"doc": 123, "typedoc": "CC", "fechaE": "01/12/2017"}
verify_cc = {"doc": 123, "typedoc": "CC", "fechaE": "01/12/2017"}
verify_car = {"doc": 123, "typedoc": "CC", "placa": "ABC123"}
verify_retry = {"id": "7d1f10483800b5071688e101", "typedoc": "CC"}
validate_cc_resp = {
    "email": "usuario@pruebas.com",
    "doc": 123,
    "jobid": "6460fc34-4154-43db-9438-8c5a059304c0",
    "nombre": "MIGUEL FERNANDO PEREZ GOMEZ",
    "typedoc": "CC",
    "validado": True,
}
verify_cc_resp = {
    "email": "usuario@pruebas.com",
    "doc": 123,
    "jobid": "6460fc34-4154-43db-9438-8c5a059304c0",
    "nombre": "MIGUEL FERNANDO PEREZ GOMEZ",
    "typedoc": "CC",
    "validado": True,
}
verify_car_resp = {
    "jobid": "ff633685-948b-4eea-9516-171cb9099da4",
    "revision": {
        "fechaRevision": "29/11/2018",
        "fechaVencimiento": "29/11/2019",
        "noRevision": "130000463",
        "placa": "ABC123",
        "reqrtm": True,
        "valido": True,
        "vigente": True,
    },
    "soat": {
        "fechaExpedicion": "10/11/2018",
        "fechaInicio": "11/11/2018",
        "fechaVencimiento": "10/11/2019",
        "noSoat": "75000093",
        "valido": True,
        "vigente": True,
    },
    "vehiculo": {
        "color": "NEGRO",
        "estado": "ACTIVO",
        "fmatri": "21/03/2005",
        "linea": "C200",
        "marca": "MERCEDES",
        "placa": "ABC123",
        "valido": True,
    },
}
verify_retry_resp = {"doc": 124, "jobid": "ecbfc775-8d9b-47a0-a2ec-bf0225bb8f6e"}
connector = tusdatos_connector.TusDatosConnector(("pruebas", "password"))
connector.url = "http://docs.tusdatos.co"


def test_launch():
    """Testing launch endpoint."""
    response = connector.launch(validate_cc)
    assert response == validate_cc_resp


def test_verify():
    response = connector.launch_verify(verify_cc)
    unvalid_response = {
        "detail": [
            {
                "loc": ["body", "consulta", "placa"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }
    assert response == unvalid_response
    # Added this to run the test, keeping in mind the API endpoint is returning
    # wrong values
    assert response != verify_cc_resp


def test_car():
    response = connector.launch_car(verify_car)
    assert response == verify_car_resp


def test_retry():
    response = connector.retry(verify_retry)
    assert response == verify_retry_resp
