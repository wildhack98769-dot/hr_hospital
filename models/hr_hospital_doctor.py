from odoo import fields, models


class HospitalDoctor(models.Model):
    """Hospital Doctor personnel records."""

    _name = "hr.hospital.doctor"
    _description = "Hospital Doctor"

    name = fields.Char(string="Full Name", required=True)
    specialization = fields.Char(string="Specialization")
    mentor_id = fields.Many2one(
        comodel_name="hr.hospital.doctor",
        string="Mentor Doctor",
    )
