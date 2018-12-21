# @class_declaration interna_montadospedido #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_montadospedido(modelos.mtd_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli_pda_montadospedido #
class albaranescli_pda_montadospedido(interna_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration montadospedido #
class montadospedido(albaranescli_pda_montadospedido, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.montadospedido_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
