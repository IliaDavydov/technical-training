from odoo import fields, models
from datetime import timedelta


class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Properties of the estate"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Selection(
        string='Type',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Garden Area orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection(string='Status'
                             , selection=[('new', 'New'),
                                          ('offer_received', 'Offer Received'),
                                          ('offer_accepted', 'Offer Accepted'),
                                          ('sold', 'Sold'), ('canceled', 'Canceled')],
                             default='new')
