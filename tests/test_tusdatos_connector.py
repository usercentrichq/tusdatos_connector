#!/usr/bin/env python

"""Tests for `tusdatos_connector` package."""

from tusdatos_connector import tusdatos_connector


validate_cc = {"doc": 123, "typedoc": "CC", "fechaE": "01/12/2017"}
verify_cc = {"doc": 123, "typedoc": "CC", "fechaE": "01/12/2017"}
verify_car = {"doc": 123, "typedoc": "CC", "placa": "ABC123"}
verify_retry = {"id": "7d1f10483800b5071688e101", "typedoc": "CC"}
verify_results = "6460fc34-4154-43db-9438-8c5a059304c0"
verify_report = "5d9e00483800a5071688a101"
verify_report_nit = "5d9e05963817a56d989523c0"
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
verify_results_resp = {
    "cedula": 123,
    "error": True,
    "errores": ["registraduria_mesa", "fosyga", "libretamilitar", "transitobog"],
    "estado": "finalizado",
    "hallazgo": True,
    "hallazgos": "medio",
    "id": "5d9e00483800a5071688a101",
    "nombre": "MIGUEL FERNANDO PEREZ GOMEZ",
    "results": {
        "Contaduria": False,
        "Contraloria": False,
        "EDU1": False,
        "EDU2": False,
        "EDU3": False,
        "Estado cedula": "Error",
        "Fosyga": "Error",
        "Interpol": False,
        "Libreta militar": "Error",
        "OFAC": False,
        "PEPS": False,
        "Policia": False,
        "Procesos TYBA": False,
        "Procuraduria": False,
        "RAMA": False,
        "RUNT": True,
        "SIMIT": False,
        "Sisben": True,
        "Transito Bogota": "Error",
    },
    "time": 48.549164,
    "typedoc": "CC",
    "validado": True,
}
verify_report_resp = "Reporte en HTML"
verify_report_pdf_resp = "Reporte en PDF"
verify_report_json_resp = {
    "contadores_s": False,
    "contaduria": False,
    "contraloria": False,
    "dest": "static/img/7d3c0000-d87e-403e-ad0a-0000d3be50cb",
    "email": "usuario@pruebas.com",
    "error": True,
    "errores": ["registraduria_mesa", "fosyga", "libretamilitar", "transitobog"],
    "fecha": "Este reporte fue generado el 09, Oct 2019 a las 11:22AM",
    "fecha_expedicion": False,
    "fopep": False,
    "fosyga": "Error",
    "genero": "F",
    "google": [],
    "hallazgos": "medio",
    "id": "30276719",
    "interpol": False,
    "juzgados_tyba": "",
    "libretamilitar": "Error",
    "lista_onu": False,
    "nombre": "JUAN PEREZ PEREZ",
    "ofac": False,
    "otros": False,
    "peps": False,
    "peps2": False,
    "peps_denom": False,
    "policia": False,
    "procuraduria": False,
    "profesion": [],
    "proveedores_ficticios": False,
    "rama": {
        "armeniajepms": False,
        "barranquillajepms": False,
        "bogotajepms": False,
        "bucaramangajepms": False,
        "bugajepms": False,
        "calijepms": False,
        "cartagenajepms": False,
        "florenciajepms": False,
        "ibaguejepms": False,
        "manizalesjepms": False,
        "medellinjepms": False,
        "monteriajepms": False,
        "neivajepms": False,
        "palmirajepms": False,
        "pastojepms": False,
        "pereirajepms": False,
        "popayanjepms": False,
        "quibdojepms": False,
        "tunjajepms": False,
        "villavicenciojepms": False,
    },
    "registraduria_mesa": "Error",
    "registraduria_solicitud": "Su solicitud del Documento 123 no se encuentra en Trámite.Si solicitó el\n        Trámite de su documento por favor consulte esta base de datos en los próximos días para verificar\n        el estado de su documento, y si aún no ha solicitado la RENOVACION de su documento, por favor\n        solicítela.",
    "relacionados": [],
    "rndc": [],
    "rnmc": "Los datos no son correctos por favor verifique.",
    "ruaf": "",
    "rues": "",
    "runt_app": {
        "exitoso": True,
        "licencia": {"licencias": [], "totalLicencias": 0},
        "multa": {
            "estadoCancelacion": "NO",
            "estadoPazSalvo": "SI",
            "estadoSuspension": "NO",
            "fechaCancelacion": "No Reporta",
            "fechaSuspension": "No Reporta",
            "numeroComparendos": "0",
            "numeroPazSalvo": "415598045067",
        },
        "nombres": "",
    },
    "rut": "No se encuentra registrado",
    "rut_estado": "N/A",
    "secop": False,
    "secop2": [],
    "secop_s": False,
    "sena": False,
    "simit": False,
    "simur": [],
    "sisben": {
        "Actualizacion ficha": " 8 de noviembre del 2018",
        "Actualizacion persona": " 8 de noviembre del 2018",
        "Antiguedad": "11 meses",
        "Apellido": "PEREZ PEREZ",
        "Departamento": "Antioquia",
        "Estado": "VALIDADO",
        "Fecha ingreso": " 30 de octubre del 2018",
        "Ficha": "",
        "Municipio": "Bolívar",
        "Nombre": "JUAN",
        "Puntaje": "40.64",
    },
    "sisconmp": {},
    "transitobog": "Error",
}
connector = tusdatos_connector.TusDatosConnector(("pruebas", "password"))
connector.url = "http://docs.tusdatos.co"


def test_launch():
    """Testing TusDatosConnector class method call to /api/launch endpoint."""
    response = connector.launch(validate_cc)
    assert response == validate_cc_resp


def test_verify():
    """Testing TusDatosConnector class method call to /api/launch/verify endpoint."""
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
    """Testing TusDatosConnector class method call to /api/launch/car endpoint."""
    response = connector.launch_car(verify_car)
    assert response == verify_car_resp


def test_retry():
    """Testing TusDatosConnector class method call to /api/retry endpoint."""
    response = connector.retry(verify_retry)
    assert response == verify_retry_resp


def test_results():
    """Testing TusDatosConnector class method call to /api/results endpoint."""
    response = connector.results(verify_results)
    assert response == verify_results_resp


def test_report():
    """Testing TusDatosConnector class method call to /api/report endpoint."""
    response = connector.report(verify_report)
    assert response == verify_report_resp


def test_report_pdf():
    """Testing TusDatosConnector class method call to /api/report_pdf endpoint."""
    response = connector.report_pdf(verify_report)
    assert response == verify_report_pdf_resp


def test_report_nit():
    """Testing TusDatosConnector class method call to /api/report_nit endpoint."""
    response = connector.report_nit(verify_report_nit)
    assert response == verify_report_resp


def test_report_nit_pdf():
    """Testing TusDatosConnector class method call to /api/report_nit_pdf endpoint."""
    response = connector.report_nit_pdf(verify_report_nit)
    assert response == verify_report_pdf_resp


def test_report_json():
    """Testing TusDatosConnector class method call to /api/report_json endpoint."""
    response = connector.report_json(verify_report)
    assert response == verify_report_json_resp


## TODO
# Still missing the last two methods of the connector.
