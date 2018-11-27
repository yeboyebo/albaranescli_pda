# @class_declaration interna #
from YBLEGACY import qsatype


class interna(qsatype.objetoBase):

    ctx = qsatype.Object()

    def __init__(self, context=None):
        self.ctx = context


# @class_declaration albaranescli_pda #
from YBLEGACY.constantes import *


class albaranescli_pda(interna):

    def albaranescli_pda_initValidation(self, name, data=None):
        response = True
        return response

    def albaranescli_pda_iniciaValoresLabel(self, model=None, template=None, cursor=None):
        labels = {}
        return labels

    def albaranescli_pda_bChLabel(self, fN=None, cursor=None):
        labels = {}
        return labels

    def albaranescli_pda_getFilters(self, model, name, template=None):
        filters = []
        return filters

    def albaranescli_pda_getForeignFields(self, model, template=None):
        fields = []
        return fields

    def albaranescli_pda_getDesc(self):
        desc = None
        return desc

    def __init__(self, context=None):
        super(albaranescli_pda, self).__init__(context)

    def initValidation(self, name, data=None):
        return self.ctx.albaranescli_pda_initValidation(name, data)

    def iniciaValoresLabel(self, model=None, template=None, cursor=None):
        return self.ctx.albaranescli_pda_iniciaValoresLabel(model, template, cursor)

    def bChLabel(self, fN=None, cursor=None):
        return self.ctx.albaranescli_pda_bChLabel(fN, cursor)

    def getFilters(self, model, name, template=None):
        return self.ctx.albaranescli_pda_getFilters(model, name, template)

    def getForeignFields(self, model, template=None):
        return self.ctx.albaranescli_pda_getForeignFields(model, template)

    def getDesc(self):
        return self.ctx.albaranescli_pda_getDesc()


# @class_declaration head #
class head(albaranescli_pda):

    def __init__(self, context=None):
        super(head, self).__init__(context)


# @class_declaration ifaceCtx #
class ifaceCtx(head):

    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)


# @class_declaration FormInternalObj #
class FormInternalObj(qsatype.FormDBWidget):
    def _class_init(self):
        self.iface = ifaceCtx(self)
