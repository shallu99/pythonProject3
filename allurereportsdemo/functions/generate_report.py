import os
import shutil
import subprocess
import datetime
import shutil
import os
# def sessionfinish():

    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    # # report_path = f"C:\\Users\\Shreyank M\\allure report rantcell\\report_{timestamp}"
    #
    # report_path = f"C:\\Users\\Shreyank M\\allure report rantcell\\report_{timestamp}"
    # temp_path = "C:\\Users\\Shreyank M\\AppData\\Local\\Temp\\allure-report"
    #
    # # Copy the Allure report files to the desired path
    # for file_name in os.listdir(temp_path):
    #     if file_name.endswith('.html') or file_name.endswith('.json') or file_name.endswith('.png'):
    #         shutil.copy(os.path.join(temp_path, file_name), os.path.join(report_path, file_name))

    # report_path = f"C:\\Users\\Shreyank M\\allure report rantcell\\report_{timestamp}"
    # os.makedirs(report_path, exist_ok=True)
    # report_path = "C:\\Users\\Shreyank M\\allure report rantcell"
    # os.chdir(report_path)
    #
    # cmd = f"allure generate {report_path} --clean"
    # subprocess.call(cmd, shell=True)
    # source_files = ["report_path.json", "report_path.json", "report_path.png"]
    # for file in source_files:
    #     if os.path.isfile(file):
    #         shutil.copy(file, os.path.join(report_path, os.path.basename(file)))





# import os
# import subprocess
# import datetime
#
# def sessionfinish():
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#     report_path = f"C:\\Users\\Shreyank M\\allure report rantcell\\report_{timestamp}"
#     os.makedirs(report_path, exist_ok=True)
#
#     cmd = f"allure generate {report_path} --clean"
#     subprocess.call(cmd, shell=True)

# import subprocess
# import sys
#
# def sessionfinish(results_path):
#     """
#     Generates an Allure report for the test results located in the specified directory.
#
#     Args:
#         results_path (str): The path to the directory containing the test results.
#     """
#     try:
#         subprocess.run(['allure', 'generate', results_path, '-o', f'{results_path}/allure-report'], check=True)
#     except subprocess.CalledProcessError as error:
#         sys.exit(f'Error generating Allure report: {error}')
#
