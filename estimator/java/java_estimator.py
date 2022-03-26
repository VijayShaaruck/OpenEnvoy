from estimator import CodeEstimatorAbstract


class JavaEstimator(CodeEstimatorAbstract):

    def check_is_blank(self, line):
        """
        Functionality:
            Check if the given line is blank
        Args:
            line: str
        Returns:
            True or False
        """
        return line.isspace()

    def check_single_line_comments(self, line):
        """
        Functionality:
            Check if the given line is single line comment
        Args:
            line: str
        Returns:
            True or False
        """
        return line.strip().startswith("//")

    def check_multiline_comment_start(self, line):
        """
        Functionality:
            Check if the given line is a multiline comment start
        Args:
            line: str
        Returns:
            True or False
        """
        return line.strip().startswith("/*")

    def check_multiline_comment_end(self, line):
        """
        Functionality:
            Check if the given line is a multiline comment end
        Args:
            line: str
        Returns:
            True or False
        """
        return line.strip().endswith("*/")

    def check_is_code(self, line):
        """
        Functionality:
            Check if the given line is code
        Args:
            line: str
        Returns:
            True or False
        """
        return not (self.check_is_blank(line)
                    or self.check_single_line_comments(line)
                    or self.check_multiline_comment_start(line)
                    or self.check_multiline_comment_end(line))

    def __init__(self):
        pass
