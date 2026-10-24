print("=====Labrariy Managment System=====")
books=[]
while True:
    print("1.Add books\n2.view books\n3.search books\n4.remove book\n5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("Add the books")
        add_books=input("enter your books:")
        if add_books in books:
            print("book already exist")
        else:
            books.append(add_books)
            print(books)
    elif choice==2:
        print("view the books:")
        if books:
            for i in books:
                print("*",i)
        else:
            print("books are unavilable")
    elif choice==3:
        print("search the books")
        search_book=input("enter your book that you want to search:")
        if search_book in books:
            print("book found")
        else:
            print("book not found")
    elif choice==4:
        search=input("enter your book:")
        if search in books:
            books.remove(search)
            print("book removed succesfully")
            print(books)
        else:
            print("book not found")
    elif choice==5:
        print("exist the programme")
        break
    else:
        print("invalid choice")