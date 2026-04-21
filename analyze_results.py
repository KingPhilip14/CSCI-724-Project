# Imports below
import json 
from pathlib import Path 
from statistics import mean 
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from typing import Dict, List, Any


# The data file directory
DATA_DIR = Path("data")
ALGO_FOLDERS = ["astar", "bfs", "dijk", "gbfs", "human"]

# Load the json data from path
def load_json(file_path: Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding='utf-8') as file:
        return json.load(file)
    
# next collect the metrics
def collect_metrics() -> Dict[str, Dict[str, float]]:
    # results hasmap to store the results
    results: Dict[str, Dict[str, float]] = {}
    
    # iterate through the folders
    for folder_name in ALGO_FOLDERS:
        print(f"Checking folder: {folder_name}")
        folder_path = DATA_DIR / folder_name
        
        if not folder_path.exists():
            # print(f"Skipping missing folder: {folder_path}")
            continue 
        
        json_files: List[Path] = list(folder_path.glob("*.json"))
        
        if not json_files:
            print(f"No JSON files found in: {folder_path}")
            continue 
        
        # tracking scores, turns, mem_spaces and exec_times in array
        scores: List[float] = []
        turns: List[float] = []
        mem_spaces: List[float] = []
        exec_times: List[float] = []
        
        for json_file in json_files:
            data = load_json(json_file)
            
            scores.append(data.get("score", 0))
            turns.append(data.get("turns", 0))
            mem_spaces.append(data.get("mem_space", 0))
            exec_times.append(data.get("exec_time", 0))
            
        results[folder_name] = {
            "avg_score": mean(scores),
            "avg_turns": mean(turns),
            "avg_mem_space": mean(mem_spaces),
            "avg_exec_time": mean(exec_times),
            "num_trials": len(json_files)
        }
        
    # print("Final result keys:", list(results.keys()))
    return results

# print the summary results 
def print_summary(results: Dict[str, Dict[str, float]]) -> None:
    print("\n=====METRIC SUMMARY ======")
    for algorithm, metrics in results.items():
        print(f"\n{algorithm.upper()}")
        print(f"   Trials       :  {metrics['num_trials']}")
        print(f"   Avg Score    :  {metrics['avg_score']:.2f}")
        print(f"   Avg Turns    :  {metrics['avg_turns']:.2f}")
        print(f"   Avg Mem Space   :  {metrics['avg_mem_space']:.2f}")
        print(f"   Avg Exec Time   : {metrics['avg_exec_time']:.6f}")
        
def plot_metric(results: Dict[str, Dict[str, float]], metric_key: str, title: str, ylabel: str, output_file: str) -> None:
    # store algorithms in array
    algorithms: List[str] = list(results.keys())
    values: List[float] = [results[algorithm][metric_key] for algorithm in algorithms]
    
    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, values)
    plt.title(title)
    plt.xlabel("Algorithm")
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(output_file)
    # plt.show()
    plt.close()
    
    
def generate_charts(results: Dict[str, Dict[str, float]]) -> None:
    plot_metric(results, "avg_score", "Avergae Score by Algorithm", "Average Score", "avg_score_chart.png")
    plot_metric(results, "avg_turns", "Average Turns by Algorithm", "Average Turns", "avg_turns_chart.png")
    plot_metric(results, "avg_mem_space", "Average Memory Space by Algorithm", "Average Memory Space", "avg_mem_space_chart.png")
    plot_metric(results, "avg_exec_time", "Average Execution Time in Algorithm", "Average Execution Time", "avg_exec_time_chart.png")
    
def main() -> None:
    if not DATA_DIR.exists():
        print("The directory does not exist.")
        return
    
    results = collect_metrics()
    
    if not results:
        print("No results found.")
        return 
    
    print_summary(results)
    generate_charts(results)
    

if __name__ == "__main__":
    main()
    
    
        

        