# python imports goes here

# odoo imports goes here
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class Emplacement(models.Model):
    _name = "emplacement"
    _description = """
        This model will help fleet managers to create routes emplacement (origins and destinations),
        Coming soon : lon & lat of each point
    """

    name = fields.Char(string="Emplacement name")
    type = fields.Selection(
        [
            ('origin','Origin'),
            ('destination','Destination')
        ],
        string="Emplacement type"
    )
