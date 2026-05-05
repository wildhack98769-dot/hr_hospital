from odoo import models, fields, api

class MassReassignDoctorWizard(models.TransientModel):
    _name = 'mass.reassign.doctor.wizard'
    _description = 'Mass Reassign Doctor Wizard'

    doctor_id = fields.Many2one(
        'hr.hospital.doctor',
        string='Новий Лікар',
        required=True
    )
    change_date = fields.Date(
        string='Дата зміни',
        default=fields.Date.context_today
    )

    def action_reassign_doctor(self):
        patient_ids = self.env.context.get('active_ids')
        patients = self.env['hr.hospital.patient'].browse(patient_ids)
        patients.write({'personal_doctor_id': self.doctor_id.id})