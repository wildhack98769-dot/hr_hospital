from odoo import fields, models


class HospitalPatient(models.Model):
    """Model representing patients receiving treatment."""

    _name = "hr.hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Full Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        string="Gender",
    )
