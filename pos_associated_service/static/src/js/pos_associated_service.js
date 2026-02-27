/** @odoo-module */

import { useState } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { AbstractAwaitablePopup } from "@point_of_sale/app/popup/abstract_awaitable_popup";

export class AssociatedServicePopup extends AbstractAwaitablePopup {
    static template = "pos_associated_service.AssociatedServicePopup";
    static defaultProps = {
        title: _t("Configurar servicio asociado"),
        confirmText: _t("Confirmar"),
        cancelText: _t("Cancelar"),
        serviceName: "",
        defaultQuantity: 1,
        defaultIncludeService: true,
    };

    setup() {
        super.setup();
        this.state = useState({
            quantity: this.props.defaultQuantity > 0 ? this.props.defaultQuantity : 1,
            includeService: this.props.defaultIncludeService,
        });
    }

    getPayload() {
        const quantity = Number.parseInt(this.state.quantity, 10);
        return {
            quantity: Number.isInteger(quantity) && quantity > 0 ? quantity : 1,
            includeService: !!this.state.includeService,
        };
    }
}

patch(PosStore.prototype, {
    async addProductToCurrentOrder(product, options = {}) {
        if (Number.isInteger(product)) {
            product = this.db.get_product_by_id(product);
        }

        if (!product?.x_has_associated_service || !product?.x_associated_service_id) {
            return super.addProductToCurrentOrder(product, options);
        }

        const associatedServiceId = Array.isArray(product.x_associated_service_id)
            ? product.x_associated_service_id[0]
            : product.x_associated_service_id;
        const serviceProduct = this.db.get_product_by_id(associatedServiceId);

        if (!serviceProduct) {
            return super.addProductToCurrentOrder(product, options);
        }

        const { confirmed, payload } = await this.popup.add(AssociatedServicePopup, {
            serviceName: serviceProduct.display_name,
            defaultQuantity: options.quantity && options.quantity > 0 ? options.quantity : 1,
            defaultIncludeService: true,
        });

        if (!confirmed) {
            return;
        }

        const quantity = payload?.quantity || 1;
        await super.addProductToCurrentOrder(product, {
            ...options,
            quantity,
        });

        if (payload?.includeService) {
            await super.addProductToCurrentOrder(serviceProduct, { quantity });
        }
    },
});
