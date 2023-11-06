from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Properties of the estate"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()