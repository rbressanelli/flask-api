from flask import Blueprint

from app.routes.error_blueprint import bp_error
from app.routes.leads_blueprint import bp_leads

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_leads)
bp_api.register_blueprint(bp_error)
