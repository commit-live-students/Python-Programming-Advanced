from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed
import pandas


class TestCleanup_csv(TestCase):
    dataframe = None

    def setup(self):
        try:
            from olympics import cleanup_csv
        except ImportError:
            self.assertFalse(no_function_found("cleanup_csv"))
        self.dataframe = cleanup_csv()

    def test_output_object_type(self):
        self.setup()
        if not isinstance(self.dataframe, pandas.DataFrame):
            self.assertFalse(incorrect_output())

    def test_drop_first_row_and_totals(self):
        self.setup()
        self.assertEqual(146, len(self.dataframe.index), "You failed to drop First Row / Totals")

    def test_column_renaming(self):
        self.setup()
        columns_list = list(self.dataframe.columns.values)
        self.assertEqual(15, len(columns_list))
        self.assertEqual("# Summer", columns_list[0])
        self.assertEqual("Gold", columns_list[1])
        self.assertEqual("Silver", columns_list[2])
        self.assertEqual("Bronze", columns_list[3])
        self.assertEqual("Total", columns_list[4])
        self.assertEqual("# Winter", columns_list[5])
        self.assertEqual("Gold.1", columns_list[6])
        self.assertEqual("Silver.1", columns_list[7])
        self.assertEqual("Bronze.1", columns_list[8])
        self.assertEqual("Total.1", columns_list[9])
        self.assertEqual("# Games", columns_list[10])
        self.assertEqual("Gold.2", columns_list[11])
        self.assertEqual("Silver.2", columns_list[12])
        self.assertEqual("Bronze.2", columns_list[13])
        self.assertEqual("Combined total", columns_list[14])

    def test_country_name_code_split(self):
        self.setup()
        for index in self.dataframe.index:
            self.assertEqual(False, "(" in index)

    def test_first_country(self):
        try:
            from olympics import first_country
        except ImportError:
            self.assertFalse(no_function_found("first_country"))
        self.setup()
        series = first_country(self.dataframe)
        try:
            self.assertEqual(13, series["# Summer"])
            self.assertEqual(0, series["Gold"])
            self.assertEqual(0, series["Silver"])
            self.assertEqual(2, series["Bronze"])
            self.assertEqual(2, series["Total"])
            self.assertEqual(0, series["# Winter"])
            self.assertEqual(0, series["Gold.1"])
            self.assertEqual(0, series["Silver.1"])
            self.assertEqual(0, series["Bronze.1"])
            self.assertEqual(0, series["Total.1"])
            self.assertEqual(13, series["# Games"])
            self.assertEqual(0, series["Gold.2"])
            self.assertEqual(0, series["Silver.2"])
            self.assertEqual(2, series["Bronze.2"])
            self.assertEqual(2, series["Combined total"])
        except KeyError:
            self.assertFalse(incorrect_output())

    def test_gold_medal(self):
        try:
            from olympics import gold_medal
        except ImportError:
            self.assertFalse(no_function_found("gold_medal"))
        self.setup()
        series = gold_medal(self.dataframe)
        self.assertEqual("United States", series.strip())

    def test_biggest_different_in_gold_medal(self):
        try:
            from olympics import biggest_different_in_gold_medal
        except ImportError:
            self.assertFalse(no_function_found("biggest_different_in_gold_medal"))
        self.setup()
        series = biggest_different_in_gold_medal(self.dataframe)
        self.assertEqual("United States", series.strip())


    def test_get_points(self):
        try:
            from olympics import get_points
        except ImportError:
            self.assertFalse(no_function_found("get_points"))
        self.setup()

        self.dataframe.index = self.dataframe.index.str.strip()
        series = get_points(self.dataframe)
        try:
            self.assertEqual(2, series["Afghanistan"])
            self.assertEqual(27, series["Algeria"])
            self.assertEqual(130, series["Argentina"])
            self.assertEqual(16, series["Armenia"])
            self.assertEqual(22, series["Australasia"])
            self.assertEqual(923, series["Australia"])
            self.assertEqual(569, series["Austria"])
            self.assertEqual(43, series["Azerbaijan"])
            self.assertEqual(24, series["Bahamas"])
            self.assertEqual(1, series["Bahrain"])
            self.assertEqual(1, series["Barbados"])
            self.assertEqual(154, series["Belarus"])
            self.assertEqual(276, series["Belgium"])
            self.assertEqual(1, series["Bermuda"])
            self.assertEqual(5, series["Bohemia"])
        except KeyError:
            self.assertFalse(incorrect_output())