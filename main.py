import sqlite3

conn = sqlite3.connect('Finances.db')
c = conn.cursor()

# with conn:
#     c.execute('CREATE TABLE Finances(id integer PRIMARY KEY UNIQUE, type string, amount integer, category string)')
#     print(c.fetchall())


def income():
    amount = int(input('Enter amount: '))
    category = input('Enter category: ')
    with conn:
        c.execute('INSERT INTO "Finances"("type", "amount", "category") VALUES("income", ?, ?)', (amount, category))
        all_income()


def expenses():
    amount = int(input('Enter amount: '))
    category = input('Enter category: ')
    with conn:
        c.execute('INSERT INTO "Finances"("type", "amount", "category") VALUES("expenses", ?, ?)', (amount, category))
        all_expenses()


def balance():
    c.execute('SELECT SUM(amount) FROM "Finances" WHERE type = "income"')
    for number in c.fetchall():
        total_income = number[0]
    c.execute('SELECT SUM(amount) FROM "Finances" WHERE type = "expenses"')
    for number in c.fetchall():
        total_expenses = number[0]
    print(f'\nTotal balance:\n{total_income - total_expenses}')


def all_income():
    with conn:
        c.execute('SELECT * FROM "Finances" WHERE type = "income"')
        if not c.fetchall():
            print('The list is empty.')
        else:
            print('\nIncome list:\n')
            c.execute('SELECT * FROM "Finances" WHERE type = "income"')
            outcome = c.fetchall()
            for item in outcome:
                print(f'ID: {item[0]}, amount: {item[2]}, category: {item[3]}')


def all_expenses():
    with conn:
        c.execute('SELECT * FROM "Finances" WHERE type = "expenses"')
        if not c.fetchall():
            print('The list is empty.')
        else:
            print('\nExpenses list:\n')
            c.execute('SELECT * FROM "Finances" WHERE type = "expenses"')
            outcome = c.fetchall()
            for item in outcome:
                print(f'ID: {item[0]}, amount: {item[2]}, category: {item[3]}')


def delete():
    delete_id = input('What is the ID of the income/expense that you would like to delete? ')
    with conn:
        c.execute('DELETE FROM "Finances" WHERE id = ?', (delete_id, ))
        c.fetchall()
        print('Item has been deleted.')


def update():
    update_id = input('What is the ID of the income/expense that you would like to update? ')
    column_to_update = input('Which column would you like to update? ')
    update_info = input(f'How should the {column_to_update} be updated (id, type, amount, category)? ')
    with conn:
        c.execute(f'UPDATE "Finances" SET {column_to_update} = "{update_info}" WHERE id = {update_id}')
        c.fetchall()
        print(f'{column_to_update} has been updated.')


def main():
    while True:
        print("\nFinance functions:")
        print("1. Enter income")
        print("2. Enter expenses")
        print("3. Get balance")
        print("4. Get all income")
        print("5. Get all expenses")
        print("6. Delete income/expense")
        print("7. Update income/expense")
        print("8. QUIT")
        try:
            option = int(input('Enter your choice: '))
            if option == 1:
                income()
            elif option == 2:
                expenses()
            elif option == 3:
                balance()
            elif option == 4:
                all_income()
            elif option == 5:
                all_expenses()
            elif option == 6:
                delete()
            elif option == 7:
                update()
            elif option == 8:
                print('Exiting finances list!')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 8.')
        except ValueError:
            print('Please enter a number.')


main()
