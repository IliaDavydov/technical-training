from odoo import fields, models
from datetime import timedelta


class Offer(models.Model):
    _name = "offer"
    _description = "Offers for properties"

    price = fields.Float()
    status = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one('res.partner')
    property_id = fields.Many2one('estate_property')

