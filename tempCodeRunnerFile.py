for rs in db["usuario"].find_one({"nivel":"usuario"}):
    print(rs)