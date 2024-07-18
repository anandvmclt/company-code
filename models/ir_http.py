#company_code_manager/models/ir_http.py
from odoo import models
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super().session_info()
        user = request.env.user
        display_switch_company_menu = (
                user.has_group("base.group_multi_company") and len(user.company_ids) > 1
        )
        # 1. Replace company name by company complete name in the session
        #    The values are used in the switch_company_menu widget (web module)
        # 2. Recompute sequence. (as the widget hard-codes the order by sequence).

        if display_switch_company_menu:
            for sequence, company in enumerate(user.company_ids):
                result["user_companies"]["allowed_companies"].get(company.id).update(
                    {
                        "name": company.complete_name,
                        "sequence": sequence,
                        "code": company.company_code,  # Add company code to session info
                    }
                )
        return result

