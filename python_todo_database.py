# todo_database.py

todos = []

def add_todo(description, date):
    todo = {"description": description, "date": date}
    todos.append(todo)
    print_all_todos()

def print_all_todos():
    print("\nVisos užduotys:")
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo['description']} (Data: {todo['date']})")
    print()

def main():
    print("Todo užduočių pridėjimo programa\n")
    while True:
        description = input("Įveskite užduoties aprašymą (arba 'exit' išeiti): ")
        if description.lower() == 'exit':
            break
        date = input("Įveskite datą (pvz., 2025-05-19): ")
        add_todo(description, date)

if __name__ == "__main__":
    main()
