# import pytest_html
# from selenium import webdriver
#
#
# import pytest
#
#
# driver = None
#
# # screenshot only failed
# # @pytest.mark.hookwrapper
# # def pytest_runtest_makereport(item):
# #     """
# #     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
# #     :param item:
# #     """
# #     pytest_html = item.config.pluginmanager.getplugin('html')
# #     outcome = yield
# #     report = outcome.get_result()
# #     extra = getattr(report, 'extra', [])
# #
# #     if report.when == 'call' or report.when == "setup":
# #         xfail = hasattr(report, 'wasxfail')
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             file_name = "../reports/" + report.nodeid.replace("::", "_") + ".png"
# #             report_name = report.nodeid.replace("::", "_") + ".png"
# #             _capture_screenshot(file_name)
# #             if file_name:
# #                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
# #                        'onclick="window.open(this.src)" align="right"/></div>' % report_name
# #                 extra.append(pytest_html.extras.html(html))
# #         report.extra = extra
# #
# #
# # def _capture_screenshot(name):
# #     print(name)
# #     driver.get_screenshot_as_file(name)
#
# # screenshot for both pass and fail
# # @pytest.mark.hookwrapper
# # def pytest_runtest_makereport(item):
# #     """
# #     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails or passes.
# #     :param item:
# #     """
# #     pytest_html = item.config.pluginmanager.getplugin('html')
# #     outcome = yield
# #     report = outcome.get_result()
# #     extra = getattr(report, 'extra', [])
# #
# #     if report.when == 'call' or report.when == "setup":
# #         xfail = hasattr(report, 'wasxfail')
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             file_name = "../reports/" + report.nodeid.replace("::", "_") + ".png"
# #             report_name = report.nodeid.replace("::", "_") + ".png"
# #             _capture_screenshot(file_name)
# #             if file_name:
# #                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
# #                        'onclick="window.open(this.src)" align="right"/></div>' % report_name
# #                 extra.append(pytest_html.extras.html(html))
# #         elif report.passed:
# #             # Attach the same screenshot to the "passed" report
# #             file_name = "../reports/" + report.nodeid.replace("::", "_") + ".png"
# #             report_name = report.nodeid.replace("::", "_") + ".png"
# #             if file_name:
# #                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
# #                        'onclick="window.open(this.src)" align="right"/></div>' % report_name
# #                 extra.append(pytest_html.extras.html(html))
# #         report.extra = extra
# #
# #
# # def _capture_screenshot(name):
# #     print(name)
# #     driver.get_screenshot_as_file(name)
# #
#
#
#
#
#
# @pytest.fixture(scope="function")
# def driver(request):
#     global driver
#     driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
#     driver.get("https://demo.guru99.com/V1/index.php")
#     # driver.maximize_window()
#     request.cls.driver = driver
#     yield driver
#     driver.quit()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     # Capture screenshot for each step
#     if report.when == 'call':
#         file_name = "../reports/" + report.nodeid.replace("::", "_") + ".png"
#         report_name = report.nodeid.replace("::", "_") + ".png"
#         _capture_screenshot(file_name)
#         if file_name:
#             html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                    'onclick="window.open(this.src)" align="mid"/></div>' % report_name
#             extra.append(pytest_html.extras.html(html))
#
#     report.extra = extra
#
# def _capture_screenshot(name):
#     print(name)
#     driver.get_screenshot_as_file(name)
