<div align="center">

🔮 Diff-OCR

OCR Benchmark & Text Comparison Tool

<p align="center">
<b>Công cụ tự động đánh giá độ chính xác của mô hình OCR / Text Generation</b>




So sánh kết quả Prediction (<code>.md</code>) với dữ liệu Ground Truth (<code>.txt</code>) một cách chính xác và hiệu quả.
</p>

Tính năng • Cài đặt • Cấu trúc • Sử dụng • Kết quả

</div>

🚀 Tính năng chính

Tính năng

Mô tả chi tiết

🔄 So sánh đa định dạng

Hỗ trợ so sánh chéo giữa file .txt (nhãn gốc) và file .md (kết quả model).

🧹 Smart Preprocessing

Tự động loại bỏ cú pháp Markdown (ảnh, link, header, bold...) và chuẩn hóa văn bản (lowercase, strip spaces) trước khi so sánh.

📊 Metrics chuyên sâu

Tính toán tự động CER (Character Error Rate), WER (Word Error Rate) và Accuracy.

📈 Báo cáo trực quan

Hiển thị bảng tóm tắt trên Terminal và xuất file .csv chi tiết cho từng cặp dữ liệu để tiện debug.

📦 Yêu cầu cài đặt

Đảm bảo bạn đã cài đặt Python. Cài đặt các thư viện phụ thuộc bằng lệnh sau:

pip install pandas jiwer tqdm tabulate


📚 Tech Stack

Pandas: Xử lý dữ liệu bảng và xuất CSV.

Jiwer: Thư viện lõi tính toán khoảng cách Levenshtein (CER/WER).

Tqdm: Hiển thị thanh tiến trình (Progress bar).

Tabulate: Format bảng kết quả đẹp mắt trên console.

📂 Cấu trúc thư mục

Để tool hoạt động chính xác, hãy tổ chức thư mục dự án theo cây dưới đây:

Project_Root/
├── 📜 compare_md_txt.py              # <--- File code chính
│
├── 🗃️ datatest/                      # (ROOT_DATASET - Chứa nhãn gốc)
│   ├── datatest_in/
│   │   └── txt/                      # Chứa các file .txt chuẩn
│   └── datatest_tay/
│       └── txt/                      # Chứa các file .txt chuẩn
│
└── 🤖 evaluation_olm/                # (ROOT_EVALUATION - Chứa kết quả model)
    ├── evaluation_output_dataset_in/ # Chứa file .md model sinh ra
    └── evaluation_output_dataset_tay/ # Chứa file .md model sinh ra


⚠️ Lưu ý quan trọng:
File kết quả và file gốc phải có cùng tên (Ví dụ: data_01.txt so khớp với data_01.md).

⚙️ Hướng dẫn sử dụng

1️⃣ Cấu hình đường dẫn

Mở file compare_md_txt.py và chỉnh sửa biến đường dẫn ở cuối file nếu cần:

if __name__ == "__main__":
    ROOT_DATASET = "datatest"          # Folder chứa Ground Truth
    ROOT_EVALUATION = "evaluation_olm" # Folder chứa Prediction


2️⃣ Chạy đánh giá

Chạy lệnh sau tại thư mục gốc của dự án:

python compare_md_txt.py


3️⃣ Tùy chỉnh nâng cao

Để thêm tập dữ liệu mới, sửa biến tasks trong hàm auto_benchmark:

tasks = {
    "DATASET_MOI": (
        os.path.join("folder_goc", "sub_path"), # Đường dẫn file gốc
        "folder_ket_qua"                        # Tên folder kết quả
    ),
}


📊 Báo cáo kết quả

Sau khi chạy, tool sẽ xuất file CSV với các trường thông tin sau:

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

Văn bản gốc (Ground Truth)

Dùng để kiểm tra nhanh

Pred_Preview

Văn bản dự đoán (Prediction)

Đã qua xử lý làm sạch

<div align="center">

Developed for Internal Benchmarking





Made with ❤️ using Python

</div>
