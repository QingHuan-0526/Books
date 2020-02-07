# 图书管理系统主程序
import v1.books_tools as books_tools

while True:

    # 显示菜单
    books_tools.show_menu()

    # 用户输入
    action_str = input("请输入你的选择：")

    if action_str in ["0", "1", "2", "3"]:
        if action_str == "1":
            books_tools.show_books()
        elif action_str == "2":
            books_tools.search_book()
        elif action_str == "3":
            books_tools.add_book()
        elif action_str == "0":
            # TODO 保存书籍信息
            print("信息保存完成，系统退出！")
            break
    else:
        print("输入错误，请重新输入！[按任意键返回主菜单]")
        input()
