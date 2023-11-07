from odoo import fields, models
from datetime import timedelta


class EstatePropertyType(models.Model):
    _name = "estate_property_type"
    _description = "Properties types"

    name = fields.Char(required=True)
