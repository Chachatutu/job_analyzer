import json
from pathlib import Path

def validate_jobs(jobs: list) -> None:
    for index,job in enumerate(jobs,start=1):
        if type(job)!=dict:
            raise ValueError(f"第{index}个工作不是字典")
        for field in ["title", "company", "city", "description"]:
            value = job.get(field)
            if value==None:
                raise ValueError(f"第{index}个岗位的{field}不存在")
            if not isinstance(value,str) or not value.strip():
                raise ValueError(f"第{index}个岗位的{field}必须为非空字符串")

def save_jobs(jobs: list ,path: Path) -> None:
    if not isinstance(jobs,list):
         raise ValueError("岗位数据必须是列表")
    validate_jobs(jobs)
    with open(path,"w",encoding="utf-8") as f:
        json.dump(jobs,f,ensure_ascii=False,indent=2)

def load_jobs(path: Path):
    with open(path,"r",encoding="utf-8") as f:
        data=json.load(f)
        
        if not isinstance(data,list):
            raise ValueError("岗位数据必须是列表")
        validate_jobs(data)

    return data 




