import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_jobs
import json
class CliTests(unittest.TestCase):
    def test_input_and_output(self):

        input_data = [
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

        script_path = Path(__file__).resolve().parent / "main.py"
        with TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
            input_path = Path(folder) / "jobs_for_test_input.json"
            with open(input_path,"w",encoding="utf-8") as f:
                json.dump(input_data, f)

            output_path = Path(folder) / "jobs_for_test_output.json"

            result = subprocess.run(
                [
                    sys.executable,
                    str(script_path),
                    "--input", str(input_path),
                    "--output", str(output_path)
                ],
                capture_output=True,
                text=True
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            output_data = load_jobs(output_path)
            self.assertEqual(input_data, output_data)