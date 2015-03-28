#encoding=utf-8
import connection

def ui_module_componentSelector(eqID):
    db = connection.connection()
    conn = db.connect()
    cur = conn.cursor()
    cur.execute('select ID, name from component where equipment_ID=%s order by ID', eqID) 
    t = ''
    s = ''
    m = ''
    i = 0
    rsDict = {}
    for rs in cur.fetchall():
        m += '<li><a class="cpSelector" cpID="%d" href="#">%s</a></li>' % rs
    conn.commit()
    cur.close()
    conn.close()
    if m == '':
        return ''
    else:
        s += '<div id="cpSelectorGroup" class="btn-group btn-group-sm">'
        s += '<button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-expanded="false">'
        s += '选择部件'
        s += '<span class="caret"></span>'
        s += '</button>'
        s += '<ul class="dropdown-menu" role="menu">'
        s += m
        s += '</ul>'
        s += '</div>'
        return s

if __name__ == "__main__":
    print(ui_module_componentSelector('1'))