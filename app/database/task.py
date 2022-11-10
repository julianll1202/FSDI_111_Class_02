from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "title": result[1],
            "subtitle": result[2],
            "body": result[3],
            "active": result[4]
        }
        out.append(result_dict)
    return out

def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE active=1", ())
    
    results = cursor.fetchall()
    cursor.close()

    return output_formatter(results)

def read(task_id):
    conn = get_db()
    statement = """
        SELECT *
        FROM task
        WHERE id = ?
    """
    cursor = conn.execute(statement, (task_id,))
    result = cursor.fetchall()
    cursor.close()

    return output_formatter(result)
def insert(raw_data):
    # create a task tuple with the information from raw_data
    task_data = (
        raw_data.get("title"),
        raw_data.get("subtitle"),
        raw_data.get("body")
    )
    # the statement contains the query structure to insert a new task
    # SQLite uses question marks (?) to match i
    statement = """
        INSERT INTO task (
            title,
            subtitle,
            body
        ) VALUES (
            ?,?,? 
        )
    """
    # Makes a connection with the database
    conn = get_db()
    # the cursor is used to execute the SQL querie
    # stated in "statement"
    conn.execute(statement, task_data)
    # makes the changes we made persist
    conn.commit()
    # closes the connection
    conn.close()

def update(taskId, new_task):
    task_data = (
        new_task.get("title"),
        new_task.get("subtitle"),
        new_task.get("body"),
        taskId
    )

    statement = """
        UPDATE task 
        SET title=?, 
            subtitle=?,
            body=?
        WHERE id=?
    """

    conn = get_db()

    conn.execute(statement, task_data)
    conn.commit()
    conn.close()

def delete(task_id):
    statement = """
        DELETE FROM task
        WHERE id = ?
    """

    conn = get_db()
    conn.execute(statement, (task_id,))
    conn.commit()
    conn.close()