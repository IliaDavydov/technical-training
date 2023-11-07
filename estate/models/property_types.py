from odoo import fields, models
from datetime import timedelta


class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "Properties types"
    _order = "sequence, name"
    
    name = fields.Char(required=True)
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    
