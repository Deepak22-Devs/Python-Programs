cart = []

def menu():
    print("======== SHOPPING CART ========")
    print("1. Add Product ")
    print("2. Show cart ")
    print("3. Search product ")
    print("4. Update Quantity ")
    print("5. Update Price ")
    print("6. Remove Product")
    print("7. Generate Bill")
    print("8. Check out")
    print("9. Exit")

def add_product():
    product_name = input("Enter Product name :")
    Price = int(input("Enter your price: "))
    Quantity = int(input("Enter your Quantity: "))
    cart.append([product_name, Price, Quantity])

def show_cart():
    if len(cart) == 0:
        print("No Product available")
        return
    print("\n Product Name \t\t Price \t Quantity")
    print("-"*48)
    for i in cart:
        print(f"\n {i[0]} \t\t {i[1]} \t {i[2]}")

def search_cart():
    scart = input("Enter product name: ")
    found = False
    for l in cart:
        if scart == l[0]:
            print("\n====== Product Details ======")
            print(f"Product Name     : {l[0]}")
            print(f"Price            : {l[1]}")
            print(f"Quantity         : {l[2]}")
            found = True
            break
    if not found:
        print("No product found.")

def delete_cart():
    dcart = input("enter product name: ")
    found = False
    for j in cart:
        if dcart == j[0]:
            cart.remove(j)
            print("Product is removed.")
            found = True
            break
    if not found:
        print("Product not found")

def update_quantity():
    ucart = input("Enter product name to change their quantity: ")
    found = False
    for i in cart:
        if ucart == i[0]:
            n = int(input("Change the quantity of the product: "))
            i[2] = n
            found = True
    if not found:
        print("Product not found")

def update_price():
    pcart = input("Enter product name to change their Price: ")
    found = False
    for k in cart:
        if pcart == k[0]:
            m = int(input("Enter your new price: "))
            k[1] = m
            found = True
    if not found:
        print("Product not found.")

def generate_bill():
    if len(cart) == 0:
        print("No product in cart.")
        return

    grand_total = 0

    print("\n========== BILL ==========")
    print("Product Name\tPrice\tQty\tTotal")
    print("-" * 45)

    for j in cart:
        total = j[1] * j[2]
        grand_total += total

        print(f"{j[0]}\t\t{j[1]}\t{j[2]}\t{total}")

    print("-" * 45)
    print(f"Grand Total = {grand_total}")
    print("=" * 45)
def check_out():
    if len(cart) == 0:
        print("Cart is empty.")
        return
    
    generate_bill()
    print("Thanks for coming.")
    print("Visit again.")
    cart.clear()
    return


while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter how many Product do you want to cart: "))
        for i in range(n):
            add_product()
    elif choice == 2:
        show_cart()
    elif choice == 3:
        search_cart()
    elif choice == 4:
        update_quantity()
    elif choice == 5:
        update_price()
    elif choice == 6:
        delete_cart()
    elif choice == 7:
        generate_bill()
    elif choice == 8:
        check_out()
        break
    elif choice == 9:
        print("Thanks for coming.")
        print("Visit again.")
        break