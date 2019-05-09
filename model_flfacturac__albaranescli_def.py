
# @class_declaration albaranescli_pda #
class albaranescli_pda(flfacturac):

    def albaranescli_pda_enviarAbanq(self, model, oParam):
        model.pda = "Pendiente"
        model.save()
        return True

    def albaranescli_pda_nuevaLinea(self, model, oParam):
        idalbaran = model.idalbaran
        barcode = oParam['codbarras']
        cantidad = parseFloat(oParam['field_cantidad'])
        idusuarioalta = qsatype.FLUtil.nameUser()
        print(cantidad)

        resul = {}
        hoy = qsatype.Date()

        pvp = 0
        descripcion = ""
        referencia = ""

        query = qsatype.FLSqlQuery()
        query.setTablesList(u"articulos")
        query.setSelect(u"referencia, descripcion, pvp")
        query.setFrom(u"articulos")
        query.setWhere(ustr(u"codbarras = '", barcode, u"'"))

        if query.exec_():
            if query.next():
                referencia = query.value(0)
                descripcion = query.value(1)
                pvp = query.value(2)
            else:
                resul['status'] = -1
                resul['msg'] = "No existe referencia asociada al código de barras"
                resul['param'] = barcode
                return resul
        else:
            resul['status'] = -1
            resul['msg'] = "Error al obtener la referencia asociada al código de barras"
            resul['param'] = barcode
            return resul

        curLA = qsatype.FLSqlCursor(u"lineasalbaranescli")
        curLA.select(ustr(u"idalbaran = ", idalbaran, u" AND referencia = '", referencia, "'"))
        if curLA.first():
            curLA.setModeAccess(curLA.Edit)
            curLA.refreshBuffer()
            curLA.setActivatedBufferChanged(True)
            curLA.setActivatedBufferCommited(True)
            cantidad = cantidad + curLA.valueBuffer(u"cantidad")
            curLA.setValueBuffer("cantidad", cantidad)
            curLA.setValueBuffer("canfactura", cantidad)
        else:
            curLA.setModeAccess(curLA.Insert)
            curLA.refreshBuffer()
            curLA.setActivatedBufferCommited(True)
            curLA.setValueBuffer("referencia", referencia)
            curLA.setValueBuffer("descripcion", descripcion)
            curLA.setValueBuffer("barcode", barcode)
            curLA.setValueBuffer("pvpreferencia", pvp)
            curLA.setValueBuffer("pvp", pvp)
            curLA.setValueBuffer("pvpunitario", pvp)
            curLA.setValueBuffer("pvptotal", cantidad * pvp)
            curLA.setValueBuffer("pvpsindto", pvp)
            curLA.setValueBuffer("cantidad", cantidad)
            curLA.setValueBuffer("canfactura", cantidad)
            curLA.setValueBuffer("idalbaran", idalbaran)
            curLA.setValueBuffer("idusuarioalta", idusuarioalta)
            curLA.setValueBuffer("horaalta", hoy.time())
            curLA.setValueBuffer("fechaalta", hoy.date())
            curLA.setValueBuffer("horamod", hoy.time())
            curLA.setValueBuffer("fechamod", hoy.date())
            curLA.setValueBuffer("candistribuida", 0)
            curLA.setValueBuffer("dtorappel", 0)
            curLA.setValueBuffer("dtolineal", 0)
            curLA.setValueBuffer("dtopor", 0)

            curLA.setActivatedBufferChanged(True)
            _LPC = qsatype.FactoriaModulos.get('formRecordlineaspedidoscli').iface
            _LPC.calculaPrecio(curLA)

        if not curLA.commitBuffer():
            resul['status'] = -1
            resul['msg'] = "Error al crear la linea de albarán"
            resul['param'] = referencia
            print("curlineasalbaran false???")
            return resul

        '''

        midata['referencia'] = articulo.data[0].referencia;
        midata['descripcion'] = articulo.data[0].descripcion;
        midata['pvpunitario'] = articulo.data[0].pvp;
        midata['pvpsindto'] = articulo.data[0].pvp;
        midata['pvptotal'] = articulo.data[0].pvp;
        midata['idusuarioalta'] =  sessionStorage.getItem('user');
        '''
        resul['status'] = 0
        resul['msg'] = "OK"
        resul['param'] = curLA.valueBuffer("idlinea")
        return True

    def __init__(self, context=None):
        super(albaranescli_pda, self).__init__(context)

    def enviarAbanq(self, model, oParam):
        return self.ctx.albaranescli_pda_enviarAbanq(model, oParam)

    def nuevaLinea(self, model, oParam):
        return self.ctx.albaranescli_pda_nuevaLinea(model, oParam)

