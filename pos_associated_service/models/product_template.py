from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_has_associated_service = fields.Boolean(string="Tiene servicio asociado")
    x_associated_service_id = fields.Many2one(
        comodel_name="product.product",
        string="Servicio asociado",
        domain="[('type', '=', 'service')]",
    )

    @api.onchange("x_has_associated_service")
    def _onchange_x_has_associated_service(self):
        if not self.x_has_associated_service:
            self.x_associated_service_id = False

    @api.constrains("x_has_associated_service", "x_associated_service_id")
    def _check_x_associated_service_consistency(self):
        for template in self:
            if not template.x_has_associated_service and template.x_associated_service_id:
                raise ValidationError(
                    "No puede definir un servicio asociado si 'Tiene servicio asociado' no está marcado."
                )
            if (
                template.x_associated_service_id
                and template.x_associated_service_id.type != "service"
            ):
                raise ValidationError("El producto asociado debe ser de tipo Servicio.")


class ProductProduct(models.Model):
    _inherit = "product.product"

    x_has_associated_service = fields.Boolean(
        related="product_tmpl_id.x_has_associated_service",
        readonly=True,
    )
    x_associated_service_id = fields.Many2one(
        comodel_name="product.product",
        related="product_tmpl_id.x_associated_service_id",
        readonly=True,
    )
