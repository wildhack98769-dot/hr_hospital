from odoo import fields, models


class HospitalVisit(models.Model):
    """Model for managing visits."""

    _name = "hr.hospital.visit"
    _description = "Patient Visit"

    visit_date = fields.Datetime(
        string="Visit Date", default=fields.Datetime.now, required=True
    )
    doctor_id = fields.Many2one("hr.hospital.doctor", string="Doctor", required=True)
    patient_id = fields.Many2one("hr.hospital.patient", string="Patient", required=True)
    disease_id = fields.Many2one("hr.hospital.disease", string="Final Diagnosis")
