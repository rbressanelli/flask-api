from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import BadRequest

from app.errors import (EmailUpdateError, InvalidEmailError, NoStringError,
                        WrongEmailNameError)
from app.models.leads_model import LeadsModel
from app.services.auxiliar_functions import (check_update_request, date_maker,
                                             format_name_email, keys_check,
                                             phone_check, valid_email_checker)


def create_new_lead():

    new_lead = request.get_json()
    session: Session = current_app.db.session

    try:
        keys_check(new_lead)
        valid_email_checker(new_lead.get("email"))
        phone_check(new_lead.get("phone"))

        new_lead["creation_date"] = date_maker()
        new_lead["last_visit"] = date_maker()
        new_lead = format_name_email(new_lead)

        new_lead_data = LeadsModel(**new_lead)

        session.add(new_lead_data)
        session.commit()

    except IntegrityError as err:
        if type(err.__dict__["orig"]).__name__ == "UniqueViolation":
            return (
                jsonify({"error": "Lead informed already registered."}),
                HTTPStatus.CONFLICT,
            )
        elif type(err.__dict__["orig"]).__name__ == "NotNullViolation":
            return (
                jsonify({"error": "All fields shound be foward to server."}),
                HTTPStatus.BAD_REQUEST,
            )

    except BadRequest:
        return (
            jsonify({"error": "Phone number format should be (XX)XXXXX-XXXX"}),
            HTTPStatus.BAD_REQUEST,
        )

    except TypeError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    except KeyError as err:
        return (
            jsonify(
                {"error": str(err), "Fields": {"name": "", "email": "", "phone": ""}}
            ),
            HTTPStatus.BAD_REQUEST,
        )

    except NoStringError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    except InvalidEmailError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    new_lead_registered = LeadsModel.query.filter_by(email=new_lead["email"]).first()

    return jsonify(new_lead_registered), HTTPStatus.CREATED


def get_all_leads():

    leads = LeadsModel.query.order_by(
        LeadsModel.last_visit,
    )
    output = [lead for lead in leads]

    if not output:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    return jsonify(output[::-1]), HTTPStatus.OK


def update_lead():

    session: Session = current_app.db.session
    received_data = request.get_json()

    try:
        check_update_request(received_data)
        valid_email_checker(received_data.get("email"))

    except EmailUpdateError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    except WrongEmailNameError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    except NoStringError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    except InvalidEmailError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    updated_lead = LeadsModel.query.filter_by(email=received_data.get("email")).first()

    if not updated_lead:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    updated_lead.visits += 1
    updated_lead.last_visit = date_maker()

    for key, value in received_data.items():
        setattr(updated_lead, key, value)

    session.add(updated_lead)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


def delete_lead():
    session: Session = current_app.db.session
    request_data = request.get_json()

    try:
        request_data["email"].lower()
        valid_email_checker(request_data["email"])

    except KeyError:
        return {"error": "The correct field name is 'email'."}, HTTPStatus.BAD_REQUEST

    except AttributeError:
        return {"error": "Email must be a string"}, HTTPStatus.BAD_REQUEST

    except InvalidEmailError as err:
        return jsonify({"error": str(err)}), HTTPStatus.BAD_REQUEST

    deleted_lead = LeadsModel.query.filter_by(email=request_data.get("email")).first()

    if not deleted_lead:
        return {"message": "No data"}, HTTPStatus.NOT_FOUND

    session.delete(deleted_lead)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
