import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import save_jobs,load_jobs

class StorageTests(unittest.TestCase):
    #往返测试
    def test_round_trip(self):
        with TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            path = Path(folder) / "jobs.json"
            test_data: list = [
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
            save_jobs(test_data,path)
            round_data = load_jobs(path)
            self.assertEqual(test_data, round_data)

    def test_invalid_save_preserves_file(self):
        with TemporaryDirectory(dir = Path(__file__).resolve().parent) as folder:
            path = Path(folder) / "jobs.json"
            test_data = [
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
            
            save_jobs(test_data,path)
            before=path.read_bytes()

            invalid_data=[
                {
                    "source": "manual",
                    "source_id": None,
                    
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
            with self.assertRaises(ValueError):
                save_jobs(invalid_data,path)
            self.assertEqual(before,path.read_bytes())

            


if __name__=="__main__":
    unittest.main()