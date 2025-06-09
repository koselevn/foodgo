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
                    add_new_user = f"select * from products where product_count_for_day > 0 and product_active = 1;"
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

            return jsonify({"message": "!!!Данные успешно приняты на бэкенде!", "result": result_log[0]})

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
                    delete_Order = f"UPDATE `orders` SET order_status = 'Rejected' where order_id = {int(id)};"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "order": "Rejected"})

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
        id_cr = data.get('id_cr')
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
                    delete_Order = f"insert into `couriers_drive` (courier_id, order_id) value ({id_cr}, {id});"
                    cursor.execute(delete_Order)
                    conection.commit()
                finally:
                    print('And1')
                try:
                    cursor = conection.cursor()
                    delete_Order = f"select courier_id from couriers;"
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


@app.route('/get-couriers', methods=['GET'])
def get_couriers():
    try:
        conection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='test-foodgo',
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = conection.cursor()
        cursor.execute("SELECT courier_id, courer_name FROM couriers")
        couriers = cursor.fetchall()
        return jsonify({"couriers": couriers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/backend-endpoint10', methods=['POST'])
def handle_post_request10():
    try:
        data = request.get_json()
        operation = data.get('operation')
        category = data.get('category')
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
                    select_prod = f"select * from products where product_category = '{category}' and product_count_for_day > 0 and product_active = 1;"
                    cursor.execute(select_prod)
                    fProducts = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "fProducts": fProducts})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint11', methods=['POST'])
def handle_post_request11():
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
                    select_prod = f"select * from products where product_veg = 1 and product_count_for_day > 0 and product_active = 1;"
                    cursor.execute(select_prod)
                    fProducts = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "fProducts": fProducts})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint12', methods=['POST'])
def handle_post_request12():
    try:
        data = request.get_json()
        operation = data.get('operation')
        nameProduct = data.get('nameProduct')
        countProduct = data.get('countProduct')

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
                    cursor.execute(
                        "UPDATE products SET product_count_for_day = product_count_for_day - %s WHERE product_name = %s",
                        (int(countProduct), nameProduct)
                    )
                    conection.commit()
                finally:
                    print('And1')
                    print('Пытаемся уменьшить:', nameProduct, 'на', countProduct)
                    conection.close()
            except Exception as ex:
                print('No Conection')
                print(ex)
                return jsonify({"error": "Ошибка подключения к базе данных"}), 500

            return jsonify({"message": "Данные успешно приняты на бэкенде!"})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint13', methods=['POST'])
def handle_post_request13():
    try:
        data = request.get_json()
        operation = data.get('operation')
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
                    select_prod = f"select * from products where product_active = 1 order by product_price;"
                    cursor.execute(select_prod)
                    fProducts = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "fProducts": fProducts})
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
                    select_prod = f"select * from products where product_active = 1 order by product_price desc;"
                    cursor.execute(select_prod)
                    fProducts = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "fProducts": fProducts})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint14', methods=['POST'])
def handle_post_request14():
    try:
        data = request.get_json()
        operation = data.get('operation')
        id = data.get('id')
        value = data.get('value')
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
                    select_prod = f"select * from products where product_active = 1;"
                    cursor.execute(select_prod)
                    rows = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "rows": rows})
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
                    select_prod = f"update products set product_count_for_day = product_count_for_day + {int(value)} where product_id = {int(id)};"
                    cursor.execute(select_prod)
                    conection.commit()
                finally:
                    print('And2')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint15', methods=['POST'])
def handle_post_request15():
    try:
        data = request.get_json()
        operation = data.get('operation')
        phone = data.get('phone')
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
                    select_prod = f"SELECT * FROM orders WHERE order_client_phone = '{phone}' order by order_id desc;"
                    cursor.execute(select_prod)
                    ord = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "ord": ord})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint16', methods=['POST'])
def handle_post_request16():
    try:
        data = request.get_json()
        operation = data.get('operation')
        id = data.get('id')
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
                    select_prod = f"update products set product_active = 0 where product_id = {id};"
                    cursor.execute(select_prod)
                    conection.commit()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "Result": "Delete Product"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint17', methods=['POST'])
def handle_post_request17():
    try:
        data = request.get_json()
        operation = data.get('operation')
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
                    select_prod = f"select * from products where product_active = 0;"
                    cursor.execute(select_prod)
                    fProducts = cursor.fetchall()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "rows": fProducts})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint18', methods=['POST'])
def handle_post_request18():
    try:
        data = request.get_json()
        operation = data.get('operation')
        id = data.get('id')
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
                    select_prod = f"update products set product_active = 1 where product_id = {id};"
                    cursor.execute(select_prod)
                    conection.commit()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "Result": "Delete Product"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint19', methods=['POST'])
def handle_post_request19():
    try:
        data = request.get_json()
        operation = data.get('operation')
        name = data.get('name')
        des = data.get('des')
        img = data.get('img')
        price = data.get('price')
        count = data.get('count')
        category = data.get('category')
        veg = data.get('veg')
        print(data)
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
                    select_prod = f"insert into `products` (product_name, product_description, product_img, product_price, product_count_for_day, product_category, product_veg, product_active) value ('{name}', '{des}', '{img}', {price}, {count}, '{category}', {veg}, 1);"
                    cursor.execute(select_prod)
                    conection.commit()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "Result": "Delete Product"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint20', methods=['POST'])
def handle_post_request20():
    try:
        data = request.get_json()
        operation = data.get('operation')
        id = data.get('id')
        name = data.get('name')
        des = data.get('des')
        img = data.get('img')
        price = data.get('price')
        category = data.get('category')
        veg = data.get('veg')
        print(data)
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
                    select_prod = f"update products Set product_name = '{name}', product_description = '{des}', product_img = '{img}', product_price = {price}, product_category = '{category}', product_veg = {veg} where product_id = {id};"
                    cursor.execute(select_prod)
                    conection.commit()
                finally:
                    print('And1')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "Result": "Product is edit"})
    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint21', methods=['POST'])
def handle_post_request21():
    try:
        data = request.get_json()
        operation = data.get('operation')
        val = data.get('val')
        column = data.get('column')
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
                    select_prod = f"select * from orders left join couriers_drive using(order_id) left join couriers using(courier_id) where {column} = '{val}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    order = cursor.fetchall()
                    print(order)
                finally:
                    print('And1')
                try:
                    cursor = conection.cursor()
                    select_prod = f"select * from orders left join couriers_drive using(order_id) left join couriers using(courier_id) left join quantity_products using(order_id) left join products using(product_id) where {column} = '{val}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    product = cursor.fetchall()
                    print(order)
                finally:
                    print('And2')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "resultOrder": order, "product": product})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint22', methods=['POST'])
def handle_post_request22():
    try:
        data = request.get_json()
        operation = data.get('operation')
        dateOne = data.get('dateOne')
        dateTwo = data.get('dateTwo')
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
                    select_prod = f"select count(*) as noo from orders where order_date between '{dateOne}' and '{dateTwo}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    numberOfOrder = cursor.fetchall()
                    print(numberOfOrder)
                finally:
                    print('And1')
                try:
                    cursor = conection.cursor()
                    select_prod = f"select round(avg(order_pice), 2) as ab from orders where order_date between '{dateOne}' and '{dateTwo}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    avgBill = cursor.fetchall()
                    print(avgBill)
                finally:
                    print('And2')
                try:
                    cursor = conection.cursor()
                    select_prod = f"select round(sum(order_pice), 2) as solld from orders where order_date between '{dateOne}' and '{dateTwo}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    solld = cursor.fetchall()
                    print(solld)
                finally:
                    print('And3')
                try:
                    cursor = conection.cursor()
                    select_prod = f"select count(*) as cash from orders where order_date between '{dateOne}' and '{dateTwo}' and order_client_pay_method = 'Cash';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    cash = cursor.fetchall()
                    print(solld)
                finally:
                    print('And4')
                try:
                    cursor = conection.cursor()
                    select_prod = f"select count(*) as card from orders where order_date between '{dateOne}' and '{dateTwo}' and order_client_pay_method = 'Bank card';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    card = cursor.fetchall()
                    print(solld)
                finally:
                    print('And5')
                try:
                    cursor = conection.cursor()
                    select_prod = f"SELECT COUNT(CASE WHEN order_status = 'Send' THEN 1 ELSE NULL END) AS send, COUNT(CASE WHEN order_status = 'Cooking' THEN 1 ELSE NULL END) AS cooking, COUNT(CASE WHEN order_status = 'Delivered' THEN 1 ELSE NULL END) AS delivered, COUNT(CASE WHEN order_status = 'On the way' THEN 1 ELSE NULL END) AS onTheWay, COUNT(CASE WHEN order_status = 'Rejected' THEN 1 ELSE NULL END) AS rejected FROM orders  WHERE order_date BETWEEN '{dateOne}' AND '{dateTwo}';"
                    print(select_prod)
                    cursor.execute(select_prod)
                    status = cursor.fetchall()
                    print(solld)
                finally:
                    print('And6')
                try:
                    cursor = conection.cursor()
                    select_prod = f"SELECT p.product_name, SUM(qp.quantity) AS total_sales FROM quantity_products AS qp JOIN products AS p ON qp.product_id = p.product_id JOIN orders AS o ON qp.order_id = o.order_id WHERE o.order_date BETWEEN '{dateOne}' AND '{dateTwo}' GROUP BY p.product_name ORDER BY total_sales DESC;"
                    print(select_prod)
                    cursor.execute(select_prod)
                    productPopular = cursor.fetchall()
                    print(solld)
                finally:
                    print('And7')
            except Exception as ex:
                print('No Conection')
                print(ex)

            return jsonify({"message": "Данные успешно приняты на бэкенде!", "numberOfOrder": numberOfOrder[0], "AvgBill": avgBill[0], "solld": solld[0], "Cash": cash[0], "Card": card[0], "status": status, "PP": productPopular})

    except Exception as e:
        print("Ошибка обработки запроса:", str(e))
        return jsonify({"error": "Произошла ошибка обработки запроса"}), 500


@app.route('/backend-endpoint23', methods=['POST'])
def handle_post_request23():
    try:
        data = request.get_json()

        operation = data.get('operation')
        inpOne = data.get('inpOne')
        inpTwo = data.get('inpTwo')
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
                    add_new_user = f"select * from products where product_price between {inpOne} and {inpTwo};"
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


@app.route('/backend-endpoint24', methods=['POST'])
def handle_post_request24():
    try:
        data = request.get_json()

        operation = data.get('operation')
        word = data.get('word')
        print(word)
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
                    add_new_user = f"select * from products where product_description like '%{word}%';"
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


if __name__ == '__main__':
    app.run(debug=True)
