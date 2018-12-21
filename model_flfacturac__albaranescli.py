
# @class_declaration albaranescli_pda_albaranescli #
class albaranescli_pda_albaranescli(flfacturac_albaranescli, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    @helpers.decoradores.accion(aqparam=["oParam"])
    def enviarAbanq(self, oParam):
        return form.iface.enviarAbanq(self, oParam)

    @helpers.decoradores.accion(aqparam=["oParam"])
    def nuevaLinea(self, oParam):
        return form.iface.nuevaLinea(self, oParam)

