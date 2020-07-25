from util import client
from util import ProductInformation
from flask import jsonify
from flask import abort
from datetime import datetime, date, timedelta

def getHistory(productId, mysql):
    try:
        return(jsonify(selectFromDb(productId, mysql)))
    except Exception as e:
        abort(500, e)

def selectFromDb(productId, mysql):
    try:
        con = mysql.connection
        cur = con.cursor()

        cur.execute("""SELECT DATE(ts)as 'date', HOUR(ts) as 'hour'
                    FROM `bazaar`.`productStats`
                    WHERE `name`=%s
                    GROUP BY DATE(ts), HOUR(ts)""", (productId,))
        result = cur.fetchall()

        # cur.close()

        timestamps = []

        for timestamp in result:
            timestamps.append(datetime.combine(timestamp['date'], datetime.min.time()) + timedelta(hours=timestamp['hour']))

        productData = []

        for timestamp in range(0, len(timestamps)-1):
            # cur = con.cursor()
            if (timestamp == len(timestamps)-1):
                cur.execute("""SELECT *
                            FROM `bazaar`.`productStats`
                            WHERE `name`=%s AND ts>=%s
                            ORDER BY ts ASC
                            LIMIT 1""", (productId, timestamps[timestamp]))
                productData += cur.fetchall()
                cur.execute("""SELECT *
                            FROM `bazaar`.`productStats`
                            WHERE `name`=%s AND ts>=%s
                            ORDER BY ts ASC
                            LIMIT 1""", (productId, timestamps[timestamp] + timedelta(hours=0.5)))
                productData += cur.fetchall()
            else:
                cur.execute("""SELECT *
                            FROM `bazaar`.`productStats`
                            WHERE `name`=%s AND ts BETWEEN %s and %s
                            ORDER BY ts ASC
                            LIMIT 1""", (productId, timestamps[timestamp], timestamps[timestamp+1]))
                productData += cur.fetchall()
                cur.execute("""SELECT *
                            FROM `bazaar`.`productStats`
                            WHERE `name`=%s AND ts BETWEEN %s and %s
                            ORDER BY ts ASC
                            LIMIT 1""", (productId, timestamps[timestamp] + timedelta(hours=0.5), timestamps[timestamp+1]))
                productData += cur.fetchall()
            # cur.close()
        cur.close()

        return(productData)
    except Exception as e:
        print(e)