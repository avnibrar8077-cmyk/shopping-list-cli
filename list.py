shopping_list = []
while True:
    user_action = input("type add, show or exit:")
    user_action = user_action.strip()
    match user_action:
        case'add':
            items= input("enter a item:")
            shopping_list.append(items)
        case'show':
            for item in shopping_list:
                print(item)
        case'exit':
            break

print("WELCOME")