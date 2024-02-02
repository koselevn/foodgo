from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

last_order_id = [0]
result_log = [0]


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/backend-endpoint', methods=['POST'])
def handle_post_request():
    try:
        data = request.get_json()

        operation = data.get('operation')
        name = data.get('name')
        address = data.get('address')
        phone = data.get('phone')
        requests = data.get('requests')
        payment = data.get('payment')
        datetime = data.get('datetime')
        basket = data.get('basket')

        date = str(datetime).partition('T')[0]
        time = str(datetime).split('T', 1)[1]

        print(time)

        total_price = 0.0

        for item in basket:
            total_price += float(item['product_price']) * float(item['count'])

        if operation == 1:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                print(basket)
                print(data)
                print(total_price)
                try:
                    cursor = conection.cursor()
                    add_new_order = f"insert into `orders` (order_client_name, order_status, order_client_adress, order_client_phone, order_client_pay_method, order_client_comment, order_pice, order_time, order_date) values ('{name}', 'Send', '{address}','{phone}', '{payment}', '{requests}', {total_price}, '{time}', '{date}');"
                    cursor.execute(add_new_order)
                    conection.commit()
                    last_id = cursor.lastrowid
                    last_order_id[0] = (int(last_id))
                    print(last_id)
                finally:
                    conection.close()
                    print('Conection close')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "name": name, "adress": address})
        if operation == 3:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    if last_order_id[0] != 0:
                        for item in basket:
                            cursor.execute(
                                f"INSERT INTO `quantity_products` (order_id, product_id, quantity) VALUES ({last_order_id[0]}, {item['product_id']}, {item['count']})")
                            conection.commit()
                    elif (last_order_id[0] == 0):
                        print('erorrrr!!!')
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "name": name, "adress": address})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint2', methods=['POST'])
def handle_post_request2():
    try:
        data = request.get_json()

        operation = data.get('operation')
        if operation == 2:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    add_new_user = f"select * from products"
                    cursor.execute(add_new_user)
                    rows = cursor.fetchall()
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "rows": rows})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint3', methods=['POST'])
def handle_post_request3():
    try:
        data = request.get_json()

        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        if operation == 4:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    Log = f"select * from login_admin;"
                    cursor.execute(Log)
                    dataLog = cursor.fetchall()
                    print(dataLog)
                    print(password)

                    if dataLog[0]['admin_password'] == str(password) and dataLog[0]['admin_login'] == login:
                        result_log[0] = 1
                        print(result_log)
                    else:
                        result_log[0] = 0
                        print(result_log)
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "result": result_log[0]})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint4', methods=['POST'])
def handle_post_request4():
    try:
        data = request.get_json()

        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        if operation == 5:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    ordersSel = f"select * from quantity_products join orders using(order_id) join products using(product_id) ORDER BY order_date, order_time;"
                    cursor.execute(ordersSel)
                    orders = cursor.fetchall()
                    print(orders)
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "orders": orders})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint5', methods=['POST'])
def handle_post_request5():
    try:
        data = request.get_json()

        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        id = data.get('id')
        if operation == 6:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    orderSel = f"select * from quantity_products join orders using(order_id) join products using(product_id) where order_id = {id};"
                    cursor.execute(orderSel)
                    order = cursor.fetchall()
                    print(order)
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "order": order})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint6', methods=['POST'])
def handle_post_request6():
    try:
        data = request.get_json()

        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        id = data.get('id')
        print(id)
        if operation == 1:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"DELETE FROM `quantity_products` WHERE order_id = {int(id)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    print('And1')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"delete from orders where order_id = {int(id)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    conection.close()
                    print('And2')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "order": "delete"})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500

@app.route('/backend-endpoint7', methods=['POST'])
def handle_post_request7():
    try:
        data = request.get_json()
        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        id = data.get('id')
        print(id)
        if operation == 1:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"UPDATE `orders` SET order_status = 'Cooking' where order_id = {int(id)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "order": "Cooking status"})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint8', methods=['POST'])
def handle_post_request8():
    try:
        data = request.get_json()
        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        id = data.get('id')
        print(id)
        if operation == 1:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"UPDATE `orders` SET order_status = 'On the way' where order_id = {int(id)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "order": "On the way status"})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint9', methods=['POST'])
def handle_post_request9():
    try:
        data = request.get_json()
        operation = data.get('operation')
        login = data.get('login')
        password = data.get('password')
        id = data.get('id')
        tg_cr = data.get('tg_cr')
        if operation == 1:
            try:
                conection = pymysql.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    password='',
                    database='test-foodgo',
                    cursorclass=pymysql.cursors.DictCursor
                )
                print('Conection')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"UPDATE couriers SET order_id = {int(id)} where courier_tg_id = {int(tg_cr)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    print('And1')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"select courier_tg_id from couriers;"
                    cursor.execute(delete_Order)
                    couriers = cursor.fetchall()
                    print(couriers)
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "couriers": couriers})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


if __name__ == '__main__':
    app.run(debug=True)
