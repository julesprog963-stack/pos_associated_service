# POS Associated Service

## Funcionalidad
- Agrega en `product.template`:
  - `x_has_associated_service` (Tiene servicio asociado)
  - `x_associated_service_id` (Servicio asociado)
- Carga esos campos en POS.
- En POS, al agregar un producto con servicio asociado, muestra popup para:
  - Cantidad
  - Incluir o no el servicio asociado
- Si confirma:
  - Agrega cantidad del producto principal
  - Agrega la misma cantidad del servicio si se marcó incluir
- Si cancela: no agrega líneas.

## Instalación
1. Asegura que el módulo esté en `custom_addons/` (contenedor: `/mnt/extra-addons/`).
2. Apps > Actualizar lista.
3. Instalar `POS Associated Service`.

## Upgrade
- Cambios XML/JS: Apps > Upgrade del módulo.
- Cambios Python: upgrade por CLI con `-u pos_associated_service --stop-after-init`.
