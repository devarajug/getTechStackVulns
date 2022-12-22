from scantechstackvulns import __version__
from scantechstackvulns import TechStack

def test_version():
    assert __version__ == '1.0.0'

def test_xls():
    techstack = [
        "postgresql 11.11", 
        "spring framework vmware 4.3.25",
        "spring framework pivotal 4.3.25",
        "apache tomcat 9.0.58",
        "oracle jdk 1.8.0 update 252",
    ]
    data = TechStack.scan(techstack, "sample.xlsx")
    assert True