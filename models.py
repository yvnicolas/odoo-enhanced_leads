# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons.crm import crm_lead

class enhanced_Leads(models.Model):

	# _inherit and _name being the same ensures we keep the same object everywhere
    _inherit = 'crm.lead'
    _name = 'crm.lead'
    name = fields.Char()
    last_Contact=fields.Char(string="Last Contact Summary", required=False)
    last_Contact_Date=fields.Date(string="Last Contact Date", required=False)
    next_Action=fields.Char(string="Next Step", required=False)
    next_Action_Date=fields.Date(string="Next Step Date", required=False)


