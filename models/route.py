from odoo import api, fields, models

class Route(models.Model):
    _name = "route"
    _description = """
                        this is the route model
                    """

    # Fields
    name = fields.Char(string = "Route name")
    expected_kilometer = fields.Float(string = "Expected kilometer")
    number = fields.Integer(string = "Number", readonly=True)
    # number = fields.Integer(string="Route Number", required=True)
    origin = fields.Selection(
        selection = '_get_origins_emplacement',
        string = "Origin"
    )
    destination = fields.Selection(
        selection = '_get_destinations_emplacement',
        string = "Destination"
    )
    route_number = fields.Char(compute = "_compute_route_number", store = True)
    trip_type = fields.Selection(
        [
            ("pickup", "Pickup"),
            ("dropOff", "DropOff"),
        ]
    )

    # Relational fields
    route_type = fields.Many2one("route.type", string="Route Type")

    # Private methods
    @api.model
    def _get_origins_emplacement(self):
        # fetch existing origins from emplacement
        origins = self.env['emplacement'].search([('type', '=', 'origin')])
        if origins:
            return [(origin.name.lower(), origin.name) for origin in origins]
        return []

    @api.model
    def _get_destinations_emplacement(self):
        destinations = self.env['emplacement'].search([('type', '=', 'destination')])
        if destinations:
            return [(destination.name.lower(), destination.name) for destination in destinations]
        return []

    @api.depends('origin', 'destination', 'route_type', 'number')
    def _compute_route_number(self):
        for record in self:
            if record.origin and record.destination and record.route_type:
                origin_abbr = record.origin[:3].upper()
                destination_abbr = record.destination[:3].upper()
                type_abbr = record.route_type.name[:3].upper()
                record.route_number = f"{origin_abbr}-{destination_abbr}-{type_abbr}-{record.number}"

    @api.model
    def create(self, vals):
        # Ensure vals is a dictionary
        if isinstance(vals, dict):
            # Get the last route and increment number if it exists
            last_route = self.search([], order="number desc", limit=1)
            vals['number'] = last_route.number + 1 if last_route else 1
        else:
            raise TypeError("Expected a dictionary for vals in create method")

        return super(Route, self).create(vals)

    # Public methods
    # def action_cancel(self):
    #     self.ensure_one()
    #     if self.state == 'completed':
    #         raise UserError("A sold property cannot be canceled.")
    #     self.state = 'canceled'

    # Start Trip: Opens the trip logging form.
    # Save Trip: Logs the trip details and adds it to the driver’s history.
    # Cancel Trip: Discards the trip and returns to the dashboard.
    # Upload Document: Allows uploading supporting trip documents.
