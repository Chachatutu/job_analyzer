from storage import save_jobs
from pathlib import Path  
def main() -> None:
    job1={
        "source" : "manual",
        "source_id" : None,
        "title" : "Python 开发实习生",
        "company" : "示例科技",
        "city" : "杭州",
        "url" : None,
        "description" : "示例科技招聘 Python 开发实习生，工作地点杭州。要求熟悉 Python，了解 SQL，有 FastAPI 项目经验者优先。每周到岗至少 4 天，连续实习至少 3 个月。"
    }

    job2={
        "source" : "manual",
        "source_id" : None,
        "title" : "AI 应用开发实习生",
        "company" : "示例智能",
        "city" : "上海",
        "url" : None,
        "description" : "招聘 AI 应用开发实习生，工作地点上海。要求熟悉 Python，了解大模型 API，有个人项目者优先。"
    }

    job3={
        "source" : "manual",
        "source_id" : None,
        "title" : "游戏开发实习生",
        "company" : "示例互动",
        "city" : "杭州",
        "url" : None,
        "description" : "招聘游戏开发实习生，工作地点杭州。要求掌握 C++，熟悉数据结构，有游戏开发经验者优先。"
    }
    data_path=Path(__file__).resolve().parent / "jobs.json"
    jobs=[job1,job2,job3]

    save_jobs(jobs,data_path)

if __name__=="__main__":
    main()