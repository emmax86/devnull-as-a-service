def dump_data(data):
    dev_null = open("/dev/null", "w")
    dev_null.write(data)
    dev_null.close()