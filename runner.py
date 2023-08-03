import os

from dotenv import load_dotenv

class Runner:
    def generate_list_of_run_command(self):
        run_command = [
                        "python3 -m pytest --reruns 3 -n 8 -v -m 'rozetka.com.ua' ./tests//*/*/*.py -s -q --alluredir=allure-results",
                        './allure-2.15.0/bin/allure generate allure-results allure-report',
                      ]
        return run_command


if __name__ == "__main__":
    list_command = Runner().generate_list_of_run_command()
    for command in list_command:
        os.system(command)
