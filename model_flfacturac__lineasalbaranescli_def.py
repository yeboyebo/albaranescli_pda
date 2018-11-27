
# @class_declaration albaranescli_pda #

class albaranescli_pda(oficial):

    def albaranescli_pda_cambiaPvpUnitario(self, model, oParam):
        model.pvpreferencia = oParam['precio']
        model.save()
        return True

    def albaranescli_pda_cambiarCantidadLineaAlbaran(self, model, oParam, cursor):
        cursor.setValueBuffer("cantidad", oParam["cantidad"])
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("cantidad", cursor)
        cursor.setActivatedBufferCommited(True)
        if not cursor.commitBuffer():
            return False
        cursor.setActivatedBufferCommited(False)
        return True

    def albaranescli_pda_cambiarPvpReferencia(self, model, oParam, cursor):
        cursor.setValueBuffer("pvpreferencia", oParam["pvpreferencia"])
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("pvpreferencia", cursor)
        qsatype.FactoriaModulos.get('formRecordlineasalbaranescli').iface.bChCursor("cantidad", cursor)
        cursor.setActivatedBufferCommited(True)
        if not cursor.commitBuffer():
            return False
        cursor.setActivatedBufferCommited(False)
        return True

    def __init__(self, context=None):
        super(albaranescli_pda, self).__init__(context)

    def cambiaPvpUnitario(self, model, oParam):
        return self.ctx.albaranescli_pda_cambiaPvpUnitario(model, oParam)

    def cambiarCantidadLineaAlbaran(self, model, oParam, cursor):
        return self.ctx.albaranescli_pda_cambiarCantidadLineaAlbaran(model, oParam, cursor)

    def cambiarPvpReferencia(self, model, oParam, cursor):
        return self.ctx.albaranescli_pda_cambiarPvpReferencia(model, oParam, cursor)

