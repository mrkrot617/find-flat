def pg_connect(connection, ads, town):
    unique = []
    cursor = connection.cursor()

    for key in ads:
        is_exist = f"SELECT ad_id FROM {town} WHERE ad_id='{key['ad_id']}'"
        cursor.execute(is_exist)

        if cursor.fetchone() is None:
            sql = f"INSERT INTO {town}(ad_id, company_ad, ad_date) " \
                  f"VALUES ({key['ad_id']}, {key['company_ad']}, '{key['ad_date']}')"
            cursor.execute(sql)
            connection.commit()

            unique.append(key)
    cursor.close()

    return unique




