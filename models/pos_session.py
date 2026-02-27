from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        fields_to_add = ["x_has_associated_service", "x_associated_service_id"]
        search_fields = result["search_params"]["fields"]
        for field_name in fields_to_add:
            if field_name not in search_fields:
                search_fields.append(field_name)
        return result
