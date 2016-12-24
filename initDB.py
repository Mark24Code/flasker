from app import db

if __name__ == "__main__":
    print("初始化数据库……")
    print("清理……")
    db.drop_all()
    print("创建新数据库……")
    db.create_all()
    print("创建完毕")
