from flask_mysqldb import MySQL


def db_connector(app, message):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'password'
    app.config['MYSQL_DB'] = 'attacat_360'
    
    mysql = MySQL(app)

    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute(message)
        result = cursor.fetchall()
        print(result)


        mysql.connection.commit()
        cursor.close()

    return result  