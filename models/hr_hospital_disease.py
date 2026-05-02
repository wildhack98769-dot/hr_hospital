from odoo import fields, models


class HospitalDisease(models.Model):
    """Model for managing hospital disease classifications."""

    _name = "hr.hospital.disease"
    _description = "Disease Type"

    name = fields.Char(string="Disease Name", required=True)
    description = fields.Text(string="Description")
