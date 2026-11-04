from analysis import (
    filter_jobs_by_city, 
    count_jobs_by_city, 
    search_jobs_by_key,
    deduplicate_jobs
    )
import unittest

class AnalysisTests(unittest.TestCase):

    def test_filter_jobs_by_city(self) -> None:
        test_data=[
            {
                "source": "manual",
                "source_id": None,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "AI 应用开发实习生",
                "company": "示例智能",
                "city": "上海",
                "url": None,
                "description": "招聘 AI 应用开发实习生，工作地点上海。要求熟悉 Python，了解大模型 API，有个人项目者优先。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "游戏开发实习生",
                "company": "示例互动",
                "city": "杭州",
                "url": None,
                "description": "招聘游戏开发实习生，工作地点杭州。要求掌握 C++，熟悉数据结构，有游戏开发经验者优先。"
            }
        ]
        test_city="杭州"
        expect_result=[test_data[0],test_data[2]]
        actual_result=filter_jobs_by_city(test_data,test_city)
        self.assertEqual(expect_result,actual_result)

        test_city="北京"
        expect_result=[]
        actual_result=filter_jobs_by_city(test_data,test_city)
        self.assertEqual(expect_result,actual_result)


    def test_count_jobs_by_city(self) -> None:
        test_data=[
            {
                "source": "manual",
                "source_id": None,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "AI 应用开发实习生",
                "company": "示例智能",
                "city": "上海",
                "url": None,
                "description": "招聘 AI 应用开发实习生，工作地点上海。要求熟悉 Python，了解大模型 API，有个人项目者优先。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "游戏开发实习生",
                "company": "示例互动",
                "city": "杭州",
                "url": None,
                "description": "招聘游戏开发实习生，工作地点杭州。要求掌握 C++，熟悉数据结构，有游戏开发经验者优先。"
            }
        ]

        expect_result={
            "杭州" : 2,
            "上海" : 1
        }
        actual_result=count_jobs_by_city(test_data)        
        self.assertEqual(expect_result,actual_result)


    def test_count_empty_by_city(self) -> None:
        test_data: list=[]
        result: dict={}
        self.assertEqual(result, count_jobs_by_city(test_data))


    def test_search_jobs_by_key(self):
        test_data=[
            {
                "source": "manual",
                "source_id": 12345,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "AI 应用开发实习生",
                "company": "示例智能",
                "city": "上海",
                "url": None,
                "description": "招聘 AI 应用开发实习生，工作地点上海。要求熟悉 Python，了解大模型 API，有个人项目者优先。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "游戏开发实习生",
                "company": "示例互动",
                "city": "杭州",
                "url": None,
                "description": "招聘游戏开发实习生，工作地点杭州。要求掌握 C++，熟悉数据结构，有游戏开发经验者优先。"
            }
        ]
        
        self.assertEqual(search_jobs_by_key(test_data, "test"), [])
        
        test_key = " P Y T H O N "
        expected_result = [test_data[0], test_data[1]]
        actual_result = search_jobs_by_key(test_data, test_key)
        self.assertEqual(expected_result, actual_result)

        test_key = "langchain"
        expected_result = []
        actual_result = search_jobs_by_key(test_data, test_key)
        self.assertEqual(expected_result, actual_result)

        test_key = "  "
        expected_result = test_data
        actual_result = search_jobs_by_key(test_data, test_key)
        self.assertEqual(expected_result, actual_result)

        test_key = "AI 应用"
        expected_result = [test_data[1]]
        actual_result = search_jobs_by_key(test_data, test_key)
        self.assertEqual(expected_result, actual_result)

    def test_deduplicate_jobs(self):
        test_data=[
            {
                "source": "manual",
                "source_id": None,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "招聘游戏开发实习生，工作地点杭州。要求掌握 C++，熟悉数据结构，有游戏开发经验者优先。"
            },
            {
                "source": "manual",
                "source_id": None,
                "title": "Python 开发实习生",
                "company": "示例科技",
                "city": "杭州",
                "url": None,
                "description": "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
            }
        ]



        before = test_data.copy()
        result = deduplicate_jobs(test_data)
        self.assertEqual(test_data, before)
        self.assertIsNot(result, test_data)

        expected_result = [test_data[0], test_data[1]]
        actual_result = deduplicate_jobs(test_data)
        self.assertEqual(expected_result, actual_result)

        test_data = []
        expected_result = []
        actual_result = deduplicate_jobs(test_data)
        self.assertEqual(expected_result, actual_result)

