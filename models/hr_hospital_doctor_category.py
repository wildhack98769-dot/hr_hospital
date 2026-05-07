from odoo.exceptions import ValidationError

from odoo import api, fields, models


class HospitalDoctorCategory(models.Model):
    """Model for managing doctor qualification levels."""

    _name = "hr.hospital.doctor.category"
    _description = "Doctor Category"
    _order = "sequence, id"

    name = fields.Char(string="Category Name", required=True, translate=True)

    sequence = fields.Integer(
        string="Sequence",
        default=10,
        help="Used to order categories. Lower values come first.",
    )

    is_intern_category = fields.Boolean(string="Is Intern Category")

    doctor_ids = fields.One2many(
        comodel_name="hr.hospital.doctor",
        inverse_name="category_id",
        string="Doctors",
        help="List of doctors belonging to this category",
    )

    # @api.constrains('name')
    # def _check_name(self):
    #     for disease in self:
    #         duplicated_names = self.env['hr.hospital.doctor.category'].search_count(
    #             [('name', '=', disease.name), ('id', '!=', disease.id)]
    #         )
    #         if duplicated_names:
    #             raise ValidationError(self.env._('The category name must be unique!'))

    # _sql_constraints = [
    #     ('name_unique',
    #      'unique(name)',
    #      _('The category name must be unique!'))
    # ]

    _unique_name = models.Constraint(
        "unique(name)",  # 'check(age > 18)' or/and 'check(activity = True)'
        "The category name must be unique!",
    )
