import re
import matplotlib.pyplot as plt

def parse_log_file(file_path, epoch_interval=1):
    """解析日志文件，可自定义Epoch间隔"""
    epochs, mae_e = [], []
    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(r'Epoch (\d+):.*RMSE_E=([\d.]+) meV', line)
            if match:
                epoch = int(match.group(1))
                if epoch % epoch_interval == 0 and epoch > 0:  # 按指定间隔过滤
                    epochs.append(epoch)
                    mae_e.append(float(match.group(2)))
    return epochs, mae_e

def plot(settings):
    molecule = settings["MOLECULE_NAME"]
    molecule = molecule.title()

    log_scratch = settings["LOG_PATHS"]["scratch"]
    log_full_param = settings["LOG_PATHS"]["full_param"]
    log_lora = settings["LOG_PATHS"]["lora"]

    output_dir = settings["OUTPUT_DIR"]
        
    # 解析三个日志文件（注意不同间隔）
    epochs_scratch, mae_scratch = parse_log_file(f"{log_scratch}", epoch_interval=100)
    epochs_lora, mae_lora = parse_log_file(f"{log_lora}", epoch_interval=100)  # LoRA间隔
    epochs_full_param, mae_full_param = parse_log_file(f"{log_full_param}", epoch_interval=100)  # PACE间隔

    # 调整横坐标（保持原始比例关系）
    epochs_scratch = [e*10 for e in epochs_scratch]  # From Scratch放大10倍
    epochs_lora = [e*10 for e in epochs_lora]   # LoRA放大10倍并偏移8000
    epochs_full_param = [e*10 for e in epochs_full_param]      # PACE放大2000倍

    # 筛选LoRA组指定坐标点
    """lora_target_points = [9000, 10000, 20000, 28000]
    filtered_lora_epochs = []
    filtered_lora_mae = []

    for epoch, mae in zip(epochs_lora, mae_lora):
        if epoch in lora_target_points:
            filtered_lora_epochs.append(epoch)
            filtered_lora_mae.append(mae)"""

    filtered_lora_epochs = epochs_lora
    filtered_lora_mae = mae_lora

    # 创建图表
    plt.figure(figsize=(8, 7))
    plt.plot(epochs_scratch, mae_scratch, "#FF6600", marker='o', linestyle='-', label='From scratch training(50DFT)', markersize=10, linewidth=3)
    plt.plot(epochs_full_param, mae_full_param, "#660099", marker='^', linestyle='-', label='Full parameter finetuning(50DFT)', markersize=10, linewidth=3)
    plt.plot(filtered_lora_epochs, filtered_lora_mae, "#0066CC", marker='^', linestyle='-', label='LoRA finetuning(50DFT)', markersize=10, linewidth=3)

    # 坐标轴设置
    plt.xlabel("Iteration", fontsize=24)
    plt.ylabel("Energy loss(meV)", fontsize=24)
    plt.title(f"{molecule}", fontsize=30, pad=15)

    # 智能刻度设置
    all_epochs = epochs_scratch + filtered_lora_epochs + epochs_full_param
    plt.xticks(sorted(list(set(all_epochs))), rotation=45, fontsize=20)  # 间隔显示刻度
    plt.yticks(fontsize=20)
    plt.grid(True, linestyle='--', alpha=0.5)

    # 图例和样式优化
    plt.legend(fontsize=17, framealpha=1)
    plt.tight_layout()

    # 保存和显示
    plt.savefig(f"{output_dir}/{molecule}_energy_loss.png", dpi=300, bbox_inches='tight')