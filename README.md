📄 Diff-OCR: OCR Benchmark & Text Comparison Tool
Diff-OCR là công cụ tự động hóa việc đánh giá độ chính xác của các mô hình OCR hoặc Text Generation. Tool thực hiện so sánh đối chiếu giữa kết quả đầu ra (Prediction - .md) và dữ liệu nhãn gốc (Ground Truth - .txt).
📑 Mục lục
Tính năng nổi bật
Yêu cầu cài đặt
Cấu trúc thư mục
Hướng dẫn sử dụng
Giải thích báo cáo
Tùy chỉnh nâng cao
🚀 Tính năng nổi bật
Tính năng
Mô tả
⚡ So sánh đa định dạng
Hỗ trợ so sánh nội dung giữa file Text thuần (.txt) và file Markdown (.md).
🧹 Smart Preprocessing
Tự động lọc bỏ cú pháp Markdown (ảnh, link, header, bold...) và chuẩn hóa văn bản (lowercase, xóa khoảng trắng thừa).
📊 Metrics chuẩn xác
Tính toán các chỉ số quan trọng: CER (Character Error Rate), WER (Word Error Rate), Accuracy.
📝 Báo cáo tự động
Hiển thị bảng tóm tắt trên Terminal và xuất file .csv chi tiết cho từng cặp file.

📦 Yêu cầu cài đặt
Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt Python và các thư viện cần thiết:
pip install pandas jiwer tqdm tabulate


Thư viện sử dụng:
pandas: Xử lý dữ liệu và xuất báo cáo CSV.
jiwer: Thư viện lõi để tính toán CER và WER.
tqdm: Hiển thị thanh tiến trình xử lý.
tabulate: Vẽ bảng kết quả đẹp mắt trên console.
📂 Cấu trúc thư mục (Quan trọng)
Để tool hoạt động chính xác, dữ liệu cần được tổ chức theo cấu trúc cây thư mục dưới đây.
⚠️ Lưu ý: Tên file .txt (gốc) và .md (kết quả model) phải trùng tên nhau để tool có thể ghép cặp (Ví dụ: file_01.txt sẽ được so sánh với file_01.md).
Project_Root/
├── compare_md_txt.py                # 📜 File code chính
│
├── datatest/                        # 🗃️ ROOT_DATASET (Chứa nhãn gốc - Ground Truth)
│   ├── datatest_in/
│   │   └── txt/                     # Chứa các file .txt chuẩn
│   └── datatest_tay/
│       └── txt/                     # Chứa các file .txt chuẩn
│
└── evaluation_olm/                  # 🤖 ROOT_EVALUATION (Chứa kết quả từ Model)
    ├── evaluation_output_dataset_in/   # Chứa file .md do model sinh ra
    └── evaluation_output_dataset_tay/  # Chứa file .md do model sinh ra


⚙️ Hướng dẫn sử dụng
Bước 1: Cấu hình đường dẫn
Mở file compare_md_txt.py, tìm đến đoạn code cuối file (khoảng dòng 120) và cập nhật tên thư mục nếu cần:
if __name__ == "__main__":
    # Tên thư mục chứa dữ liệu gốc (Ground Truth)
    ROOT_DATASET = "datatest"
    
    # Tên thư mục chứa kết quả đánh giá (Prediction)
    ROOT_EVALUATION = "evaluation_olm"


Bước 2: Chạy đánh giá
Mở Terminal tại thư mục dự án và chạy lệnh:
python compare_md_txt.py


Bước 3: Xem kết quả
Tool sẽ hiển thị bảng tóm tắt trên màn hình và xuất file CSV vào thư mục ROOT_EVALUATION.
Kết quả màn hình (Ví dụ):
+-------------------+------------+-----------+-------+
| Dataset           | Char Acc % | Word Acc %| CER   |
+-------------------+------------+-----------+-------+
| dataset_in        | 98.50      | 95.20     | 0.015 |
| dataset_tay       | 92.10      | 88.40     | 0.079 |
+-------------------+------------+-----------+-------+


📈 Giải thích báo cáo CSV
File báo cáo (ví dụ benchmark_dataset_in.csv) sẽ có các cột sau:
Tên cột
Ý nghĩa
Ghi chú
Filename
Tên file được đánh giá


Char_Acc
Độ chính xác ký tự
1 - CER
Word_Acc
Độ chính xác từ
1 - WER
CER
Character Error Rate
Càng thấp càng tốt
GT_Preview
Đoạn đầu của văn bản gốc
Ground Truth
Pred_Preview
Đoạn đầu của văn bản dự đoán
Prediction (đã làm sạch)

🛠 Tùy chỉnh nâng cao
Nếu cấu trúc thư mục con của bạn khác với mặc định, hãy tìm hàm auto_benchmark và sửa biến tasks.
tasks = {
    "TÊN_NHIỆM_VỤ_MỚI": (
        # Đường dẫn con tới file gốc .txt (tính từ ROOT_DATASET)
        os.path.join("folder_goc", "sub_folder_txt"), 
        
        # Tên folder chứa kết quả .md (tính từ ROOT_EVALUATION)
        "folder_ket_qua_md"
    ),
}


Developed for internal benchmarking tool.
