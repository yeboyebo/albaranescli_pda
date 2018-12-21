# @class_declaration interna_registrosmodificados #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_registrosmodificados(modelos.mtd_registrosmodificados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli_pda_registrosmodificados #
class albaranescli_pda_registrosmodificados(interna_registrosmodificados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration registrosmodificados #
class registrosmodificados(albaranescli_pda_registrosmodificados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.registrosmodificados_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
