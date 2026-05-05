from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HospitalVisit(models.Model):
    """Model for managing visits."""

    _name = "hr.hospital.visit"
    _description = "Patient Visit"

    state = fields.Selection([
        ('planned', 'Planned'),
        ('done', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='planned', required=True)

    planned_date = fields.Datetime(
        string="Planned Date/Time",
        required=True,
        help="Scheduled time for the doctor's appointment"
    )
    actual_date = fields.Datetime(
        string="Actual Date/Time",
        help="The time when the visit actually took place"
    )

    doctor_id = fields.Many2one("hr.hospital.doctor", string="Doctor", required=True)
    patient_id = fields.Many2one("hr.hospital.patient", string="Patient", required=True)

    summary = fields.Html(string="Epicrisis / Summary")
    disease_id = fields.Many2one("hr.hospital.disease", string="Disease")

    active = fields.Boolean(default=True)

    def write(self, vals):
        for rec in self:
            if rec.state == 'done':
                readonly_fields = ['planned_date', 'actual_date', 'doctor_id', 'patient_id']
                if any(f in vals for f in readonly_fields):
                    raise ValidationError(_(
                        "You cannot change the date, time, or doctor for a visit that has already taken place."
                    ))
        return super().write(vals)

    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError(_("You cannot delete a completed visit."))
        return super().unlink()

    def toggle_active(self):
        """Перевірка при спробі архівування через інтерфейс."""
        for rec in self:
            if rec.active and rec.state == 'done':
                raise ValidationError(_("You cannot archive a completed visit."))
        return super().toggle_active()

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            if not rec.actual_date:
                rec.actual_date = fields.Datetime.now()