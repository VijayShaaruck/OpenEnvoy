from abc import ABC, abstractmethod


class CodeEstimatorAbstract(ABC):

    @abstractmethod
    def check_is_blank(self, line):
        raise NotImplementedError("check_is_blank method not implemented")

    @abstractmethod
    def check_single_line_comments(self, line):
        raise NotImplementedError("check_is_comments method not implemented")

    @abstractmethod
    def check_multiline_comment_start(self, line):
        raise NotImplementedError("check_is_comments method not implemented")

    @abstractmethod
    def check_multiline_comment_end(self, line):
        raise NotImplementedError("check_is_comments method not implemented")

    @abstractmethod
    def check_is_code(self, line):
        raise NotImplementedError("check_is_code method not implemented")
