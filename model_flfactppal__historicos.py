# @class_declaration interna_historicos #
import importlib

from YBUTILS.viewREST import helpers

from models.flfactppal import models as modelos


class interna_historicos(modelos.mtd_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration albaranescli_pda_historicos #
class albaranescli_pda_historicos(interna_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration historicos #
class historicos(albaranescli_pda_historicos, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.flfactppal.historicos_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
