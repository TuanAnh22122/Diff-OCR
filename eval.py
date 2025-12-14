import os
import glob
import re
import pandas as pd
from jiwer import wer, cer
from tqdm import tqdm
from tabulate import tabulate

# ================= 1. HÀM XỬ LÝ TEXT (GIỮ NGUYÊN) =================
def advanced_clean_text(text):
    if not isinstance(text, str):
        text = str(text) if text is not None else ""
    text = text.lower()
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'[#*`>\-_]', ' ', text)
    text = " ".join(text.split())
    return text

def load_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return ""

# ================= 2. ENGINE TỰ ĐỘNG QUÉT =================
def auto_benchmark(root_dataset, root_evaluation):
    """
    Tự động ghép cặp các folder con dựa trên quy tắc đặt tên.
    """
    # Cấu hình quy tắc ghép cặp folder (Mapping)
    # Key: Tên hiển thị báo cáo
    # Value: (Đường dẫn con trong dataset gốc, Đường dẫn con trong kết quả)
    tasks = {
        "DATASET IN": (
            os.path.join("datatest_in", "txt"), 
            "evaluation_output_dataset_in"
        ),
        "DATASET TAY": (
            os.path.join("datatest_tay", "txt"), 
            "evaluation_output_dataset_tay"
        )
    }

    print(f"📡 ĐANG CẤU HÌNH TỰ ĐỘNG...")
    print(f"   📂 Root Dataset: {root_dataset}")
    print(f"   📂 Root Eval   : {root_evaluation}\n")

    for task_name, (sub_gt, sub_pred) in tasks.items():
        # Tạo đường dẫn tuyệt đối
        gt_dir = os.path.join(root_dataset, sub_gt)
        pred_dir = os.path.join(root_evaluation, sub_pred)

        # Kiểm tra tồn tại
        if not os.path.exists(gt_dir):
            print(f"⚠️  Bỏ qua {task_name}: Không tìm thấy folder gốc '{sub_gt}'")
            continue
        if not os.path.exists(pred_dir):
            print(f"⚠️  Bỏ qua {task_name}: Không tìm thấy folder kết quả '{sub_pred}'")
            continue

        # --- CHẠY LOGIC ĐÁNH GIÁ (Phần này giống code cũ) ---
        print(f"{'='*60}")
        print(f"🚀 RUNNING: {task_name}")
        
        # Lấy file
        gt_files = {os.path.splitext(f)[0]: os.path.join(gt_dir, f) for f in os.listdir(gt_dir) if f.endswith('.txt')}
        pred_files = {os.path.splitext(f)[0]: os.path.join(pred_dir, f) for f in os.listdir(pred_dir) if f.endswith('.md')}
        
        common = sorted(list(gt_files.keys() & pred_files.keys()))
        
        if not common:
            print("❌ Không có file chung để so sánh.")
            continue

        results = []
        for name in tqdm(common, desc="Evaluating"):
            gt_txt = advanced_clean_text(load_file(gt_files[name]))
            pred_txt = advanced_clean_text(load_file(pred_files[name]))
            
            if not gt_txt: continue
            
            try:
                c_err = cer(gt_txt, pred_txt)
                w_err = wer(gt_txt, pred_txt)
                results.append({
                    "Filename": name,
                    "Char_Acc": max(0, 1 - c_err),
                    "Word_Acc": max(0, 1 - w_err),
                    "CER": c_err,
                    "GT_Preview": gt_txt[:30],
                    "Pred_Preview": pred_txt[:30]
                })
            except: pass
            
        # Xuất báo cáo
        if results:
            df = pd.DataFrame(results)
            print(f"\n✅ KẾT QUẢ {task_name}:")
            headers = ["Metric", "Result"]
            data = [
                ["Avg Char Accuracy", f"{df['Char_Acc'].mean()*100:.2f}%"],
                ["Avg Word Accuracy", f"{df['Word_Acc'].mean()*100:.2f}%"]
            ]
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
            
            # Lưu file
            csv_name = f"benchmark_{task_name.lower().replace(' ', '_')}.csv"
            # Sửa lỗi: dùng biến root_evaluation được truyền vào hàm thay vì biến global
            csv_path = os.path.join(root_evaluation, csv_name)
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            print(f"   -> Đã lưu: {csv_path}")

# ================= 3. NHẬP INPUT TẠI ĐÂY (RẤT GỌN) =================
if __name__ == "__main__":
    
    # Bạn chỉ cần sửa đúng 2 dòng này:
    ROOT_DATASET = "datatest" 
    ROOT_EVALUATION = "evaluation_chandra"

    # Chạy
    if os.path.exists(ROOT_DATASET) and os.path.exists(ROOT_EVALUATION):
        auto_benchmark(ROOT_DATASET, ROOT_EVALUATION)
    else:
        # Nếu thư mục chưa tồn tại, in thông báo hướng dẫn thay vì báo lỗi cứng
        print(f"❌ Không tìm thấy thư mục gốc.")
        print(f"Vui lòng tạo thư mục hoặc cập nhật đường dẫn trong code:")
        print(f"- Dataset: {ROOT_DATASET}")
        print(f"- Eval   : {ROOT_EVALUATION}")