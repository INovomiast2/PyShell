import inquirer

def supermenu():
    questions = [
        inquirer.Text("username", "Insert your Username"),
        inquirer.Password("usrpwd", '*')
    ]
    answers = inquirer.prompt(questions)
    print(answers)
    return 0