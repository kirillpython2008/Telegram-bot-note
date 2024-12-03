import aiosqlite


# create new note
async def get_db_text(id_file, id_user, text):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    await cursor.execute("INSERT INTO users (name_file, id_user, text) VALUES (?, ?, ?)", (id_file, id_user, text))
    await connect.commit()

    await cursor.close()
    await connect.close()


# return text note
async def get_db_number(id_file, id_user):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    text = await cursor.execute("SELECT text FROM users WHERE name_file = ? AND id_user = ?", (id_file, id_user))
    text = await text.fetchone()

    await cursor.close()
    await connect.close()

    return text[0]


# command all
async def get_all(id_user):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    all_text = await cursor.execute(f"SELECT * FROM users WHERE id_user = {id_user}")
    all_text = await all_text.fetchall()

    await cursor.close()
    await connect.close()

    user = [(i[0], i[-1]) for i in all_text]

    return user


# reply_button delete
async def delete(id_file, id_user):

    all_id = []

    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    all_id_file = await cursor.execute(f"SELECT name_file FROM users WHERE id_user = {id_user}")
    all_id_file = await all_id_file.fetchall()

    for i in all_id_file:
        all_id.append(i[0])

    await cursor.execute(f"DELETE FROM users WHERE name_file = ? and id_user = ?",
                         (id_file, id_user))
    await connect.commit()

    await cursor.close()
    await connect.close()

    return id_file in all_id


# reply_button remake message
async def remake(new_text, id_file, id_user):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    await cursor.execute(f"UPDATE users SET text = ? WHERE name_file = ? AND id_user = ?",
                         (new_text, id_file, id_user))
    await connect.commit()

    await cursor.close()
    await connect.close()


# return true if input id_file in id_file
async def all_id_1(id_file, id_user):
    all_id = []

    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()

    all_id_file = await cursor.execute(f"SELECT name_file FROM users WHERE id_user = {id_user}")
    all_id_file = await all_id_file.fetchall()

    for i in all_id_file:
        all_id.append(i[0])

    return id_file in all_id
