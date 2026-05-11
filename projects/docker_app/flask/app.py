from flask import Flask, app
import pymysql



app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/inserdata')
def insert_data():
    connection = pymysql.connect(
        host='mysql_container',
        user='root',
        password='rootpassword',
        db='mydatabase',
        
    )
    cursor = connection.cursor()
    insert_query = "INSERT INTO users (city, temperature) VALUES (%s, %s)"
    data = ('New York', 25.5)

    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()
    connection.close()
    return 'Data inserted successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)