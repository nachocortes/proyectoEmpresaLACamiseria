tipo_direccion_choices = (
    ('contacto', 'Contacto'),
    ('envio', 'Envío'),
    ('facturacion', 'Facturación'),
)

tipo_via_choices = (
    ('calle', 'Calle'),
    ('avenida', 'Avenida'),
    ('camino', 'Camino'),
    ('via', 'Vía'),
    ('plaza', 'Plaza'),
    ('ronda', 'Ronda'),
    ('bulevar', 'Bulevar'),
)

tipo_documento_choices = (
    ('dni', 'DNI'),
    ('nif', 'NIF'),
    ('cif', 'CIF'),
    ('pasaporte', 'Pasaporte'),
    ('nie', 'NIE'),
)

tipo_cliente_choices = (
    ('particular', 'particular'),
    ('empresa', 'empresa'),
)

estado_pedido_choices = (
        ('Borrador', 'Borrador'),
        ('Presupuesto enviado', 'Presupuesto enviado'),
        ('A facturar', 'A facturar'),
        ('Pagado', 'Pagado'),
    )
