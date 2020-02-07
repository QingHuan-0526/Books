# 图书管理的相关功能函数

# 存储所有图书
books = []


# 主菜单
def show_menu():
    print("*" * 50)
    print("欢迎使用【图书管理系统】V1.0")
    print()
    print("1. 查看书库")
    print("2. 图书检索")
    print("3. 图书添加")
    print()
    print("0. 退出系统")
    print("*" * 50)


# 查看书库
def show_books():
    # 判断是否有图书
    if len(books) == 0:
        print("暂无图书！[按任意键返回主菜单]")
        input()
        return
    # 有图书
    print("-" * 50)
    print("名称\t\t\t\t作者\t\t价格\t\t分类\t\t")
    for book in books:
        print("{name}\t\t\t\t{author}\t\t{price}\t\t{type}"
              .format(name=book["book_name"], author=book["book_author"],
                      price=book["book_price"], type=book["book_type"]))
    print("-" * 50)
    print("按任意键返回主菜单！")
    input()


# 图书检索
def search_book():
    # 是否检索到图书标志
    is_exist = False
    book_name = input("请输入你要检索的书名：")
    for book in books:
        if book_name == book["book_name"]:
            print("{name}\t\t\t\t{author}\t\t{price}\t\t{type}"
                  .format(name=book["book_name"], author=book["book_author"],
                          price=book["book_price"], type=book["book_type"]))
            is_exist = True
            action = input("请选择要进行的操作： [1]修改 [2]删除 [3]返回主菜单")
            if action in ["1", "2", "3"]:
                if action == "1":
                    update_book(book)
                elif action == "2":
                    del_book(book)
                elif action == "3":
                    print("按任意键返回主菜单！")
            else:
                print("输入有误，按任意键返回主菜单！")
    if not is_exist:
        print("未检索到该图书！[按任意键返回主菜单]")
    input()


# 图书添加
def add_book():
    book_name = input("请输入图书的名称：")
    book_author = input("请输入图书的作者：")
    book_price = input("请输入图书的价格：")
    book_type = input("请输入图书的分类：")
    book = {"book_name": book_name,
            "book_author": book_author,
            "book_price": book_price,
            "book_type": book_type}
    books.append(book)
    print("图书【{0}】添加成功![按任意键返回主菜单]".format(book_name))
    input()


# 图书删除
def del_book(book):
    books.remove(book)
    print("图书删除成功！[按任意键返回主菜单]")


# 图书修改
def update_book(book):
    book["book_name"] = input_book(book["book_name"], "请输入新的图书名称：")
    book["book_author"] = input_book(book["book_author"], "请输入新的图书作者：")
    book["book_price"] = input_book(book["book_price"], "请输入新的图书价格：")
    book["book_type"] = input_book(book["book_type"], "请输入新的图书类别：")
    print("图书修改成功！[按任意键返回主菜单]")


# 根据输入返回  如果输入则返回新值 否则返回原值
def input_book(old_value, tips_message):
    new_value = input(tips_message)
    if len(new_value) > 0:
        return new_value
    else:
        return old_value
