from odoo import fields, models


class HospitalPatient(models.Model):
    """Model representing patients receiving treatment."""

    _name = "hr.hospital.patient"
    _description = "Hospital Patient"
    _inherit = ["hr.hospital.medic.info"]

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

    personal_doctor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Personal Doctor",
    )

    doctor_history_ids = fields.One2many(
        comodel_name="hr.hospital.doctor.history",
        inverse_name="patient_id",
        string="Doctor History",
    )

    insurance_policy = fields.Char(string="Insurance Policy", size=20)
