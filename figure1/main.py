import importlib
from pathlib import Path

# 全局配置（支持多分子循环）
MOLECULES = ["aspirin", "Azobenzene", "Benzene", "Ethanol", "Malonaldehyde", 
             "Naphthalene", "Paracetamol", "Salicylic_acid", "Uracil", 
             "Toluene"
            ]  # 需要处理的分子列表
BASE_LOG_DIR = "logs"
BASE_OUTPUT_DIR = "results"

def run_for_molecule(molecule):
    """处理单个分子的所有绘图任务"""
    settings = {
        "MOLECULE_NAME": molecule,
        "LOG_PATHS": {
            "scratch": f"{BASE_LOG_DIR}/{molecule}_from_scartch.txt",
            "lora": f"{BASE_LOG_DIR}/{molecule}_lora.txt",
            "full_param": f"{BASE_LOG_DIR}/{molecule}_full_param.txt"
        },
        "OUTPUT_DIR": f"{BASE_OUTPUT_DIR}/{molecule}"
    }
    
    # 创建分子专属输出目录
    Path(settings["OUTPUT_DIR"]).mkdir(parents=True, exist_ok=True)
    
    # 动态调用所有figure_*.py模块
    plot_modules = [f.stem for f in Path(".").glob("figure_*.py")]
    for module in plot_modules:
        importlib.import_module(module).plot(settings)

if __name__ == "__main__":
    for molecule in MOLECULES:  # 自动循环处理每个分子
        print(f"Processing {molecule}...")
        run_for_molecule(molecule)
    
    print(f"所有分子处理完成！结果保存在 {BASE_OUTPUT_DIR}/ 目录下")