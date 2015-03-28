#encoding=utf-8
import connection

def ui_module_equipmentSelector():
    db = connection.connection()
    conn = db.connect()
    cur = conn.cursor()
    cur.execute('select location, ID, name from equipment order by ID')
    s = ''
    m = ''
    i = 0
    rsDict = {}
    for rs in cur.fetchall():
        if rs[0] in rsDict:
            rsDict[rs[0]].append((rs[1], rs[2]))
        else:
            rsDict[rs[0]] = [(rs[1], rs[2])]
    for btnhead in rsDict.keys():
        if i != 0:
            m += '<li class="divider"></li>'
        m += '<li class="dropdown-header">%s</li>' % btnhead
        for btn in rsDict[btnhead]:
            m += '<li><a class="eqSelector" eqID="%d" href="#">%s</a></li>' % btn
        i += 1
    conn.commit()
    cur.close()
    conn.close()
    if m == '':
        return ''
    else:
        s += '<div id="eqSelectorGroup" class="btn-group btn-group-sm">'
        s += '<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">'
        s += '选择设备'
        s += '<span class="caret"></span>'
        s += '</button>'
        s += '<ul class="dropdown-menu" role="menu">'
        s += m
        s += '</ul>'
        s += '</div>'
        return s

if __name__ == "__main__":
    print(ui_module_equipmentSelector())