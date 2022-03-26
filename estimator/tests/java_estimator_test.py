
import unittest

from estimator.java.java_estimator import JavaEstimator


class JavaEstimatorTest(unittest.TestCase):
    def setUp(self):
        self.obj = JavaEstimator()

    def test_check_is_blank(self):
        self.assertTrue(self.obj.check_is_blank("  "))
        self.assertFalse(self.obj.check_is_blank("  /"))
        self.assertFalse(self.obj.check_multiline_comment_end("public class Main {"))

    def test_check_single_line_comments(self):
        self.assertTrue(self.obj.check_single_line_comments("//"))
        self.assertFalse(self.obj.check_single_line_comments("/*"))
        self.assertFalse(self.obj.check_multiline_comment_start(" "))
        self.assertFalse(self.obj.check_multiline_comment_end("public class Main {"))

    def test_check_multiline_comment_start(self):
        self.assertTrue(self.obj.check_multiline_comment_start("/*"))
        self.assertFalse(self.obj.check_multiline_comment_start("//"))
        self.assertFalse(self.obj.check_multiline_comment_start(" "))
        self.assertFalse(self.obj.check_multiline_comment_end("public class Main {"))

    def test_check_multiline_comment_end(self):
        self.assertTrue(self.obj.check_multiline_comment_end("*/"))
        self.assertFalse(self.obj.check_multiline_comment_end("//"))
        self.assertFalse(self.obj.check_multiline_comment_end(" "))
        self.assertFalse(self.obj.check_multiline_comment_end("public class Main {"))

    def test_check_is_code(self):
        self.assertTrue(self.obj.check_is_code("import java"))
        self.assertFalse(self.obj.check_is_code("//"))
        self.assertFalse(self.obj.check_is_code(" "))
        self.assertFalse(self.obj.check_is_code("*/"))
        self.assertFalse(self.obj.check_is_code("/*"))

if __name__ == "__main__":
    unittest.main()
