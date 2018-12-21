
# @class_declaration albaranescli_pda #
from YBLEGACY.constantes import *
from YBUTILS.viewREST import cacheController


class albaranescli_pda(flfacturac):

    def albaranescli_pda_bufferCommited_lineasalbaranescli(self, curLinea=None):
        # _i = self.iface
        curAlbaran = qsatype.FLSqlCursor(u"albaranescli")
        curAlbaran.select(ustr(u"idalbaran = ", curLinea.valueBuffer(u"idalbaran")))
        if not curAlbaran.first():
            return False
        curAlbaran.setModeAccess(curAlbaran.Edit)
        curAlbaran.refreshBuffer()
        if not qsatype.FactoriaModulos.get('formRecordalbaranescli').iface.calcularTotalesCursor(curAlbaran):
            return False
        if not curAlbaran.commitBuffer():
            return False
        return True

    def __init__(self, context=None):
        super(albaranescli_pda, self).__init__(context)

    def bufferCommited_lineasalbaranescli(self, curLinea=None):
        return self.ctx.albaranescli_pda_bufferCommited_lineasalbaranescli(curLinea)

