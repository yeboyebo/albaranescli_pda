# @class_declaration interna_lineascarro #
import importlib

from YBUTILS.viewREST import helpers

from models.flfacturac import models as modelos


class interna_lineascarro(modelos.mtd_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli_pda_lineascarro #
class albaranescli_pda_lineascarro(interna_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration lineascarro #
class lineascarro(albaranescli_pda_lineascarro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfacturac.lineascarro_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
