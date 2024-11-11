from odoo import fields, models

class RouteType(models.Model):
    _name = "route.type"
    _description = """
                        This is the route type model
                    """
    name = fields.Char(required = True)
