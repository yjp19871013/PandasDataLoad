from DataAdapter.AdapterFactory import AdapterFactory

if __name__ == "__main__":

    # Excel
    adapter = AdapterFactory.create("1.xlsx")
    adapter.connect()
    data_set = adapter.open_data_set("工作表1")
    adapter.query_data(data_set)
    print(data_set)
    adapter.close_data_set(data_set)
    adapter.disconnect()

    # Mysql
    adapter = AdapterFactory.create("mysql")
    adapter.connect(host='127.0.0.1',
                    port=3306,
                    user='root',
                    passwd='root',
                    db='book_borrow_go',
                    charset='utf8')
    data_set = adapter.open_data_set("permissions")
    adapter.query_data(data_set)
    print(data_set)
    adapter.close_data_set(data_set)
    adapter.disconnect()
