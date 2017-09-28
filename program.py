import sqlite3
from bottle import route, run,debug,template,request,redirect

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output



@route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        redirect('/todo')
        #return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')


@route('/do_insert' , method='GET')
def get_id():
    redirect('/new')      



@route('/edit/<no:int>', method='GET')
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        if status == 'open':
            status = 1
        else:
            status = 0
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()
        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()
        return template('edit_task', old=cur_data, no=no)

@route('/find_edit' , method='GET')
def get_id():
    id_edit = request.GET.editdata.strip()
    redirect('/edit/' + id_edit)   
    

@route('/delete/<no:int>', method='GET')
def delete_item(no):
       conn = sqlite3.connect('todo.db')
       c = conn.cursor()
       c.execute("DELETE FROM todo WHERE id LIKE ?", (str(no)))
       conn.commit()
       redirect('/todo')

@route('/find_delete' , method='GET')
def get_id():
    id_delete = request.GET.deletedata.strip()
    redirect('/delete/' + id_delete)   


debug(True)
run(reloader=True)
