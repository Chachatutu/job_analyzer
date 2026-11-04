import re

def search_jobs_by_key(jobs: list, keyword: str) -> list:
    keyword = re.sub(r'\s+', '', keyword).lower()
    
    if keyword == "":
        return jobs.copy()

    result: list = []
    for job in jobs:
        for e in job.values():
            if isinstance(e,str) and keyword in re.sub(r'\s+', '', e).lower():
                result.append(job)
                break
    return result

def filter_jobs_by_city(jobs: list,city: str)->list:
    if re.sub(r'\s+', '', city) == "":
        return jobs.copy()
    
    result=[]
    for job in jobs:
        if job["city"]==city:
            result.append(job)
    return result

def count_jobs_by_city(jobs: list) -> dict:
    counts: dict={}
    for job in jobs:
        city=job["city"]
        if not city in counts:
            counts[city]=0
        counts[city]+=1
    return counts

def deduplicate_jobs(jobs: list) -> list:
    result: list = []
    for job in jobs:
        if not job in result:
            result.append(job)

    return result