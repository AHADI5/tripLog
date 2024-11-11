from odoo import models, fields, api, _

class Trip(models.Model):
    _name = 'trip'
    _description = "This model is the main model for our trip logging"
    _inherit = ['mail.thread'] # Inherit the mail mixin

    name = fields.Char(string="Trip")
    start_time = fields.Datetime(string="Start Time")
    end_time = fields.Datetime(string="End Time")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    origin = fields.Selection(
        selection='_get_origins_emplacement',
        string="Origin"
    )
    destination = fields.Selection(
        selection='_get_destinations_emplacement',
        string="Destination"
    )
    state = fields.Selection(
        [
            ('current', 'Pending'),
            ('ongoing', 'On going'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        ]
    )
    trip_type = fields.Selection(
        [
            ('passenger_trip', 'Passenger trip'),
            ('cargo_trip', 'Cargo trip'),
            ('preplanned_trip', 'Passenger trip'),
        ],
        string = _('Trip type'),
    )
    kilometer_driven = fields.Float("Kilometer driven")
    route_id = fields.Many2one("route")
    passenger_ids = fields.Many2many("res.partner", string="Passenger(s)")
    department_ids = fields.Many2many("hr.department", string="Department(s)")
    driver_id = fields.Many2one("hr.employee", string="Driver", default=lambda self: self.env.user)

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

    # Public methods

