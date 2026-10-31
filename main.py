from pathlib import Path
from storage import load_jobs, save_jobs
import  json
import argparse
from analysis import(
    filter_jobs_by_city,
    search_jobs_by_key,
    count_jobs_by_city
)
            

def main() ->None :

    parser = argparse.ArgumentParser(description="岗位筛选助手")
    parser.add_argument("--city", default="", help="筛选城市")
    parser.add_argument("--keyword", default="", help="关键词搜索")
    parser.add_argument("--input", type=Path, default=None, help="导入岗位文件")
    parser.add_argument("--output", type=Path, default=None, help="导出筛选结果")
    
    args = parser.parse_args()
    
    if args.input == None:
        data_path = Path(__file__).resolve().parent / "jobs.json"
    else:
        data_path = args.input

    try:
        data = load_jobs(data_path)
    except FileNotFoundError:
        print("岗位文件不存在")
        return
    except json.JSONDecodeError as error:
        print("JSON文件格式错误")
        print(f"错误行：{error.lineno}\n错误列：{error.colno}")
        return
    except ValueError as error:
        print(error)
        return
    
    matched_jobs = data
    if args.city or args.keyword:
        if args.city :
            matched_jobs = filter_jobs_by_city(matched_jobs,args.city)
        if args.keyword :
            matched_jobs = search_jobs_by_key(matched_jobs, args.keyword)
        if not matched_jobs:
            print("\n没有符合条件的岗位")
        else:
            print("\n符合条件的岗位有：")
            for matched_job in matched_jobs:
                print(matched_job["title"], matched_job["company"])
        print(count_jobs_by_city(matched_jobs))

    if args.output is not None:
        if args.output.resolve() == data_path.resolve():
            print("输出路径不能与输入路径相同，未保存")
        else:
            try:
                save_jobs(matched_jobs, args.output)
                print(f"已成功保存到{args.output}")
            except OSError as e:
                print(f"保存失败：{e}")
        





if __name__ == "__main__":
    main()
