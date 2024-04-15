import logging
import inspect

class RLogger:
    @staticmethod
    def start(fname='execution.log', level=logging.DEBUG):
        logging.basicConfig(filename=fname, level=level)
    
    def __init__(self, module_header, class_header='', sep=':'):
        self.sep = sep
        if class_header == '':
            self.header = module_header
        else:
            self.header = self.sep.join([module_header, class_header])

    def __call__(self, msg, exception=False):
        logger = logging.getLogger(self.sep.join([self.header,
                                                  inspect.stack()[1][3]]))
        if exception:
            logger.exception(msg)
        else:
            logger.error(msg)
