from logfile import Logclass

class TestExample(Logclass):
    def test2(self):
        log = self.getlog()
        log.info("this is my first test case")
        if 'nikita' in 'nikitaneti':
            assert True
            log.info("test case pass")
        else:
            log.error("test case fail")
            assert False