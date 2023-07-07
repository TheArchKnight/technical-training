from dateutil.relativedelta import relativedelta
from odoo import fields, models


class EstatePropertyModel(models.Model):
    _name = "estate.property"
    _description = "estate property model"
    
    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda self: fields.Datetime.today() + relativedelta(months=3))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
            string='Garden orientation',
            selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
            help="Type is used to separate orientation on properties"
            )
    state = fields.Selection(
            string="State",
            selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),
                       ('sold','Sold'),('canceled','Canceled')],
            help="Current state of the property")
