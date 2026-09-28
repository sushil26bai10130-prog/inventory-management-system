print("OOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOO")
print()
print("     INVENTORY MANAGEMENT SYSTEM")
print()
print("OOOOOOOOOOOOOOOOOOOOOOOOOOO")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOO")
print()

E = {}
i = 0


def viewing():
    print("All Products:")
    print()

    if len(E) == 0:
        print("No products available")
    else:
        for j in E:
            print("Index:", j)
            print("Name:", E[j]["name"])
            print("Quantity:", E[j]["quantity"])
            print("Price:", E[j]["price"])
            print()


def searching():
    N = int(input("Enter index: "))

    if N in E:
        print("Product found:")
        print("Name:", E[N]["name"])
        print("Quantity:", E[N]["quantity"])
        print("Price:", E[N]["price"])
    else:
        print("No product on this index")

    print()


def update():
    a = int(input("Enter index of product: "))

    if a not in E:
        print("No product on this index")
        return

    print()
    print("What do you want to update?")
    print("1. Name")
    print("2. Quantity")
    print("3. Price")

    b = int(input("Enter your choice: "))

    if b == 1:
        x = input("Enter new name: ")
        E[a]["name"] = x
        print("Name updated!")

    elif b == 2:
        x = int(input("Enter new quantity: "))
        E[a]["quantity"] = x
        print("Quantity updated!")

    elif b == 3:
        x = int(input("Enter new price: "))
        E[a]["price"] = x
        print("Price updated!")

    else:
        print("Invalid choice")

    print()


def selling():
    print("Which product do you want to sell?")
    a = int(input("Enter index of product: "))

    if a not in E:
        print("No product on this index")
        return

    if E[a]["quantity"] > 0:
        E[a]["quantity"] = E[a]["quantity"] - 1
        print("Product is sold")
        print("Remaining quantity:", E[a]["quantity"])
    else:
        print("Product is out of stock")

    print()


def delete():
    print("Which product do you want to delete?")
    a = int(input("Enter index of product: "))

    if a in E:
        E.pop(a)
        print("Product is deleted")
    else:
        print("No product on this index")

    print()


while True:

    print("1. Add new product")
    print("2. View all products")
    print("3. Search a product")
    print("4. Update product")
    print("5. Sell a product")
    print("6. Delete a product")
    print("7. Exit")
    print()

    X = int(input("Enter your choice: "))
    print()

    if X == 1:

        print("Adding new product")
        print()

        A = input("Enter product's name: ")
        B = int(input("Enter product's quantity: "))
        C = int(input("Enter product's price: "))

        D = {
            "name": A,
            "quantity": B,
            "price": C
        }

        E[i] = D
        i = i + 1

        print("Product added successfully!")
        print()

    elif X == 2:

        print("Viewing all products")
        print()
        viewing()

    elif X == 3:

        print("Searching a product")
        print()
        searching()

    elif X == 4:

        print("Updating the product")
        print()
        update()

    elif X == 5:

        print("Selling the product")
        print()
        selling()

    elif X == 6:

        print("Deleting the product")
        print()
        delete()

    elif X == 7:

        print("Thank you for visiting us!")
        break

    else:

        print("Invalid choice!")
        print()
