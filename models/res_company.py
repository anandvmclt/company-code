#company_code_manager/models/res_company.py

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'
    _order = "company_code,name"

    company_code = fields.Char(string='Company Code', unique=True)
    complete_name = fields.Char(compute="_compute_complete_name", store=True)

    _sql_constraints = [
        ("company_code_uniq", "unique (company_code)", "The company code must be unique !")
    ]

    @api.depends("company_code", "name")
    def _compute_complete_name(self):
        for company in self:
            if not company.company_code:
                company.complete_name = company.name
            else:
                company.complete_name = "{} - {}".format(company.company_code, company.name)

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('company_code', operator, name), ('vat', operator, name)]
        companies = self.search(domain + args, limit=limit)
        return companies.name_get()
