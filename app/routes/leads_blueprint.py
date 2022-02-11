from flask import Blueprint

from app.controllers.leads_controller import (
    create_new_lead, 
    get_all_leads,
    update_lead,
    delete_lead
    )


bp_leads = Blueprint("bp_leads", __name__, url_prefix="/leads")

bp_leads.post("")(create_new_lead)

bp_leads.get("")(get_all_leads)

bp_leads.patch("")(update_lead)

bp_leads.delete("")(delete_lead)
