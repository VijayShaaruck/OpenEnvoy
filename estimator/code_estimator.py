import os

from java.java_estimator import JavaEstimator


class CodeEstimator(JavaEstimator):

    def __init__(self, folder_name):
        self.estimator = None
        self.folder_name = folder_name
        self.isMultiline = False
        self.result = {}

    def __is_file_supported(self, file):
        """
        Functionality:
            Check if the given file is supported
        Args:
            file: str
        Returns:
            True or False
        """
        result = False
        supported_files = {".java": JavaEstimator}
        filename, file_extension = os.path.splitext(file)
        if file_extension in supported_files:
            result = True
            self.estimator = supported_files[file_extension]
        return result

    def __identify_line_type(self, file, line):
        """
        Functionality:
            Check the type of given line
        Args:
            file: str,line: str
        Returns:
            None
        """
        self.result[file]["Total"] += 1

        if self.estimator.check_multiline_comment_start(self, line):
            self.isMultiline = True
        elif self.estimator.check_multiline_comment_end(self, line):
            self.result[file]["Comments"] += 1
            self.isMultiline = False

        if self.isMultiline:
            self.result[file]["Comments"] += 1
            return

        if self.estimator.check_is_blank(self, line):
            self.result[file]["Blank"] += 1
        elif self.estimator.check_single_line_comments(self, line):
            self.result[file]["Comments"] += 1
        elif self.estimator.check_is_code(self, line):
            self.result[file]["Code"] += 1
        return

    def __parse_input_files(self):
        """
        Functionality:
            Parse the files in the specified folder
        Args:
            None
        Returns:
            None
        """
        for file in os.listdir(self.folder_name):
            if self.__is_file_supported(file):
                with open(os.path.join(self.folder_name, file), 'r') as FileObj:
                    lines = FileObj.readlines()
                    if self.result.get(file) is None:
                        self.result[file] = {"Blank": 0, "Comments": 0, "Code": 0, "Total": 0}

                    for line in lines:
                        self.__identify_line_type(file, line)
            else:
                print(f"File Type : {file} Not Supported")

    def get_estimation(self):
        """
        Functionality:
            Get estimation of lines of code present in the files.
        Args:
            None
        Returns:
            None
        """
        self.__parse_input_files()
        return self.result
