"""
实现的功能:
1.把测试的结果.改成√，F改成x,Error改成0
2.命令行加个--change参数开关，默认不开启，当加上参数`—change on·的时候才生效

"""


def pytest_addoption(parser):
    parser.addoption(
        "--change",
        action="store",
        default="off",
        help="'Default 'off' for change, option: on or off"
    )


def pytest_report_teststatus(report, config):
    '''turn . into √，turn F into x, turn E into 0'''
    if config.getoption("--change") == "on":
        if report.when == 'call' and report.failed:
            return (report.outcome, 'x', 'failed')
        if report.when == 'call' and report.passed:
            return (report.outcome, '√', 'passed')
        if report.when == 'setup' and report.failed:
            return (report.outcome, '0', 'error')
