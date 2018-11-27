
# @class_declaration albaranescli_pda_lineasalbaranescli #
class albaranescli_pda_lineasalbaranescli(oficial_lineasalbaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def cambiaPvpUnitario(self, oParam):
        return form.iface.cambiaPvpUnitario(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def cambiarCantidadLineaAlbaran(self, oParam, cursor):
        return form.iface.cambiarCantidadLineaAlbaran(self, oParam, cursor)

    @helpers.decoradores.accion(aqparam=["oParam", "cursor"])
    def cambiarPvpReferencia(self, oParam, cursor):
        return form.iface.cambiarPvpReferencia(self, oParam, cursor)

