import os
import datetime

def run_pytest_with_allure_reports_in_JSON(script_path,report_dir,Report_folder_name):
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create folder with timestamp as name
    report_dir1 = report_dir +'\\'+ Report_folder_name + f"{timestamp}"
    folderReportname = Report_folder_name + f"{timestamp}"
    os.mkdir(report_dir1)
    # change the path to match the location of your PyCharm executable
    pycharm_path = r"terminal/pycharm64.exe"
    # change the path to match the location of your PyCharm project directory
    project_path = r"pythonProject2"
    # construct the command to run pytest with Allure reports
    cmd = f' pytest -v -s --alluredir="{report_dir1}" "{script_path}"'
    # construct the command to open the PyCharm terminal window in PowerShell
    ps_cmd = f'start powershell.exe "{pycharm_path}" terminal "{project_path}"'
    # open the PyCharm terminal window in PowerShell
    os.system(ps_cmd)
    # send the command to the PyCharm terminal window
    os.system(cmd)
    return report_dir1,folderReportname

def run_pytest_with_allure_reports_in_HTML(report_dir,folderReportname):
    # change the path to match the location of your PyCharm executable
    pycharm_path = r"terminal/pycharm64.exe"
    # change the path to match the location of your PyCharm project directory
    project_path = r"C:\Users\Shreyank M\PycharmProjects\pythonProject2"
    # construct the command to generate Allure HTML report
    cmd = f'allure generate "{report_dir}"'
    # construct the command to open the PyCharm terminal window in PowerShell
    ps_cmd = f'start powershell.exe "{pycharm_path}" terminal "{project_path}"'
    # open the PyCharm terminal window in PowerShell
    os.system(ps_cmd)
    # change the directory to allurereportsdemo\Report
    os.chdir(os.path.join(project_path, 'allurereportsdemo', 'Report',folderReportname))
    # send the command to the PyCharm terminal window
    os.system(cmd)
report_dir,folderReportname =run_pytest_with_allure_reports_in_JSON(r"C:\\Users\\Shreyank M\\PycharmProjects\\pythonProject2\\allurereportsdemo", r"C:\\Users\\Shreyank M\\PycharmProjects\\pythonProject2\\allurereportsdemo\\Report","Rantcell_report")
run_pytest_with_allure_reports_in_HTML(report_dir,folderReportname)