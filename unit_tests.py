import unittest
import numpy as np
import tools
import circle_tool
import matplotlib.pyplot as plt
import os
import circle_tool
import json
import app_api


class TestMathFunctions(unittest.TestCase):
    cos_result = [1.0, 0.9979866764718844, 0.9919548128307953, 0.9819286972627067, 0.9679487013963562, 0.9500711177409454, 0.9283679330160726, 0.9029265382866212, 0.8738493770697849, 0.8412535328311812, 0.8052702575310586, 0.766044443118978, 0.7237340381050701, 0.6785094115571322, 0.6305526670845225, 0.5800569095711982, 0.5272254676105024, 0.4722710747726827, 0.41541501300188644, 0.3568862215918719, 0.2969203753282749, 0.23575893550942728, 0.17364817766693041, 0.1108381999010111, 0.04758191582374218, -0.01586596383480803, -0.07924995685678854, -0.14231483827328523, -0.20480666806519074, -0.26647381369003503, -0.32706796331742166, -0.3863451256931287, -0.4440666126057741, -0.5000000000000002, -0.5539200638661103, -0.6056096871376668, -0.654860733945285, -0.7014748877063214, -0.7452644496757547, -0.7860530947427875, -0.8236765814298327, -0.8579834132349771, -0.8888354486549234, -0.9161084574320696, -0.9396926207859083, -0.9594929736144974, -0.975429786885407, -0.9874388886763943, -0.9954719225730846, -0.9994965423831851, -
                  0.9994965423831851, -0.9954719225730846, -0.9874388886763943, -0.975429786885407, -0.9594929736144974, -0.9396926207859084, -0.9161084574320696, -0.8888354486549235, -0.857983413234977, -0.8236765814298328, -0.7860530947427874, -0.7452644496757548, -0.7014748877063213, -0.6548607339452852, -0.6056096871376666, -0.5539200638661105, -0.4999999999999996, -0.44406661260577396, -0.3863451256931287, -0.3270679633174219, -0.26647381369003464, -0.20480666806519054, -0.14231483827328523, -0.07924995685678879, -0.01586596383480761, 0.04758191582374238, 0.11083819990101086, 0.17364817766692997, 0.23575893550942748, 0.2969203753282749, 0.35688622159187167, 0.4154150130018868, 0.4722710747726829, 0.5272254676105024, 0.5800569095711979, 0.6305526670845228, 0.6785094115571323, 0.7237340381050701, 0.7660444431189778, 0.8052702575310587, 0.8412535328311812, 0.8738493770697849, 0.9029265382866211, 0.9283679330160727, 0.9500711177409454, 0.9679487013963562, 0.9819286972627068, 0.9919548128307953, 0.9979866764718844, 1.0]

    sin_result = [0.0, 0.0634239196565645, 0.12659245357374926, 0.18925124436041021, 0.2511479871810792, 0.3120334456984871, 0.3716624556603276, 0.42979491208917164, 0.4861967361004687, 0.5406408174555976, 0.5929079290546404, 0.6427876096865393, 0.690079011482112, 0.7345917086575333, 0.7761464642917568, 0.8145759520503357, 0.8497254299495144, 0.8814533634475821, 0.9096319953545183, 0.9341478602651067, 0.9549022414440739, 0.9718115683235417, 0.984807753012208, 0.9938384644612541, 0.998867339183008, 0.9998741276738751, 0.9968547759519424, 0.9898214418809327, 0.9788024462147787, 0.963842158559942, 0.9450008187146685, 0.9223542941045814, 0.8959937742913359, 0.8660254037844385, 0.8325698546347714, 0.795761840530832, 0.7557495743542583, 0.7126941713788627, 0.6667690005162917, 0.6181589862206051, 0.5670598638627709, 0.5136773915734063, 0.4582265217274105, 0.4009305354066136, 0.3420201433256689, 0.28173255684142967, 0.2203105327865408, 0.1580013959733499, 0.09505604330418244, 0.031727933498067656, -0.03172793349806786, -
                  0.09505604330418263, -0.15800139597335008, -0.22031053278654056, -0.28173255684142984, -0.34202014332566866, -0.4009305354066138, -0.4582265217274103, -0.5136773915734064, -0.5670598638627706, -0.6181589862206053, -0.6667690005162915, -0.7126941713788629, -0.7557495743542582, -0.7957618405308321, -0.8325698546347713, -0.8660254037844388, -0.895993774291336, -0.9223542941045814, -0.9450008187146683, -0.9638421585599422, -0.9788024462147787, -0.9898214418809327, -0.9968547759519423, -0.9998741276738751, -0.998867339183008, -0.9938384644612541, -0.9848077530122081, -0.9718115683235417, -0.9549022414440739, -0.9341478602651068, -0.9096319953545182, -0.881453363447582, -0.8497254299495144, -0.8145759520503358, -0.7761464642917566, -0.7345917086575332, -0.690079011482112, -0.6427876096865396, -0.5929079290546402, -0.5406408174555974, -0.4861967361004688, -0.4297949120891719, -0.37166245566032724, -0.31203344569848707, -0.2511479871810794, -0.18925124436040974, -0.12659245357374904, -0.06342391965656452, -2.4492935982947064e-16]

    def setUp(self):
        app_api.app.config['TESTING'] = True
        self.app = app_api.app.test_client()
        self.image_size = os.stat("circle_plot.png").st_size

    def test_random_number_cos_populating_list(self):

        output = tools.get_cos_x([2, 8, 16, 1, 0], 3)
        self.assertIsNotNone(output)
        self.assertEqual(
            output, [-1.2484405096414273, -0.4365001014258406, -2.872978440970154, 1.6209069176044193, 3.0])

    def test_in_sequence_cos_populating_list(self):
        output = tools.get_cos_x([2, 3, 5, 7, 8], 1)
        self.assertIsNotNone(output)
        self.assertEqual(output, [-0.4161468365471424, -0.9899924966004454,
                         0.28366218546322625, 0.7539022543433046, -0.14550003380861354])

    def test_random_number_sin_populating_list(self):
        output = tools.get_sin_y([19, 2, 150, .5, 53], 5)
        self.assertIsNotNone(output)
        self.assertEqual(output, [0.7493860483147617, 4.546487134128409, -
                         3.574382148145823, 2.397127693021015, 1.9796257509091708])

    def test_in_sequence_sin_populating_list(self):
        output = tools.get_sin_y([2, 3, 5, 7, 8], 3)
        self.assertIsNotNone(output)
        self.assertEqual(output, [2.727892280477045, 0.4233600241796016, -
                         2.8767728239894153, 1.9709597961563672, 2.9680747398701453])

    def test_real_use_case_with_large_list(self):
        line_list = np.linspace(0, 2 * np.pi, 100)
        cos_output = tools.get_cos_x(line_list, 1)
        self.assertIsNotNone(cos_output)

        sin_output = tools.get_sin_y(line_list, 1)
        self.assertIsNotNone(sin_output)
        
        for actual, expected in zip(cos_output, self.cos_result):
            self.assertAlmostEqual(actual, expected, places=12)


        for actual, expected in zip(sin_output, self.sin_result):
            self.assertAlmostEqual(actual, expected, places=12)

    def test_plot_a_circle(self):
        line_list = np.linspace(0, 2 * np.pi, 100)
        cos_output = tools.get_cos_x(line_list, 1)
        sin_output = tools.get_sin_y(line_list, 1)
        result = plt.plot(cos_output, sin_output)

        line = result[0]
        x_data = line.get_xdata()
        y_data = line.get_ydata()

        self.assertTrue(np.allclose(x_data, cos_output))
        self.assertTrue(np.allclose(y_data, sin_output))

    def test_check_for_plt_show(self):
        with open("circle_tool.py", "r") as f:
            content = f.read()
            self.assertNotIn("plt.show()", content)

    def test_plot_a_circle_on_a_different_origin_point(self):
        line_list = np.linspace(0, 2 * np.pi, 100)
        cos_output = tools.get_cos_x(line_list, 3, 4)
        sin_output = tools.get_sin_y(line_list, 3, 2)
        result = plt.plot(cos_output, sin_output)

        line = result[0]
        x_data = line.get_xdata()
        y_data = line.get_ydata()

        self.assertTrue(np.allclose(x_data, cos_output))
        self.assertTrue(np.allclose(y_data, sin_output))

    def test_circle_tool_function_created(self):
        self.assertTrue(hasattr(circle_tool, "plot_a_circle_on_fig"))
        self.assertTrue(hasattr(circle_tool, "plot_the_circles"))

    def test_more_then_one_circle(self):
        with open("circle_data.json", "r") as f:
            data = json.load(f)
            self.assertGreater(len(data), 1)

    def test_check_for_circle_image(self):
        circle_tool.plot_the_circles()
        self.assertTrue(os.stat("circle_plot.png").st_size > 0)
        self.image_size = os.stat("circle_plot.png").st_size

    def test_api_call_image(self):
        response = self.app.get("/api/get_image")
        self.assertEqual(response.status_code, 200, "Expected status code 200 from path /api/get_image")

    def test_api_posts(self):
        with open("circle_data.json", "r") as f:
            data = json.load(f)

        request = {
            "name": "circle2",
            "x": 4,
            "y": -1,
            "radius": 4
        }

        response = self.app.post("/api/add_circle", json=request)

        with open("circle_data.json", "r") as f:
            data = json.load(f)
            self.assertEqual(response.status_code, 200, "Expected status code 200 from path /api/add_circle")
            self.assertGreater(len(data), 1)
            self.assertNotEqual(os.stat("circle_plot.png").st_size, self.image_size)
            self.image_size = os.stat("circle_plot.png").st_size

        response = self.app.post("/api/remove_circle",
                                 json={"name": "circle2"})

        with open("circle_data.json", "r") as f:
            data = json.load(f)
            self.assertEqual(response.status_code, 200, "Expected status code 200 from path /api/remove_circle")
            self.assertLess(len(data), 3)
            self.assertNotEqual(os.stat("circle_plot.png").st_size, self.image_size)
            self.image_size = os.stat("circle_plot.png").st_size

        response = self.app.get("/api/get_circles")

        with open("circle_data.json", "r") as f:
            data = json.load(f)
            self.assertEqual(response.status_code, 200, "Expected status code 200 from path /api/get_circles")
            self.assertEqual(response.json, data)


if __name__ == "__main__":
    unittest.main()
