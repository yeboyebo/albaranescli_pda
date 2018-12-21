# @class_declaration interna_registrosexportados #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_registrosexportados(modelos.mtd_registrosexportados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli_pda_registrosexportados #
class albaranescli_pda_registrosexportados(interna_registrosexportados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration registrosexportados #
class registrosexportados(albaranescli_pda_registrosexportados, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.registrosexportados_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
