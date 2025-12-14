# Diff-OCR
OCR Benchmark & Text Comparison Tool

Công cụ tự động đánh giá độ chính xác của mô hình OCR hoặc Text Generation bằng cách so sánh kết quả đầu ra (định dạng Markdown .md) với dữ liệu nhãn gốc (định dạng Text .txt).

🚀 Tính năng chính

So sánh đa định dạng: So sánh nội dung giữa file .txt (Ground Truth) và file .md (Prediction).

Làm sạch dữ liệu (Preprocessing):

Tự động loại bỏ cú pháp Markdown (ảnh, link, header, bold, italic, code block...).

Chuẩn hóa văn bản (lowercase, xóa khoảng trắng thừa) để so sánh nội dung thực tế.

Metrics đánh giá: Tính toán CER (Character Error Rate), WER (Word Error Rate), và độ chính xác (Accuracy).

Báo cáo tự động:

Hiển thị bảng kết quả tóm tắt trên terminal.

Xuất file CSV chi tiết cho từng cặp file.

📦 Yêu cầu cài đặt

Trước khi chạy, hãy đảm bảo bạn đã cài đặt Python và các thư viện cần thiết:

pip install pandas jiwer tqdm tabulate


pandas: Xử lý dữ liệu và xuất file CSV.

jiwer: Tính toán CER và WER.

tqdm: Hiển thị thanh tiến trình.

tabulate: Vẽ bảng kết quả đẹp trên console.

📂 Cấu trúc thư mục (Quan trọng)

Mặc định, code được cấu hình để quét theo cấu trúc thư mục sau. Bạn cần đảm bảo dữ liệu của mình khớp với cấu trúc này (hoặc xem phần Tùy chỉnh để sửa đổi):

Project_Root/
├── compare_md_txt.py          <-- File code chính
│
├── datatest/                  <-- (ROOT_DATASET - Chứa nhãn gốc)
│   ├── datatest_in/
│   │   └── txt/               <-- Chứa các file .txt chuẩn
│   └── datatest_tay/
│       └── txt/               <-- Chứa các file .txt chuẩn
│
└── evaluation_olm/            <-- (ROOT_EVALUATION - Chứa kết quả model)
    ├── evaluation_output_dataset_in/  <-- Chứa file .md model sinh ra
    └── evaluation_output_dataset_tay/ <-- Chứa file .md model sinh ra


Lưu ý: Tên file .txt và .md phải giống nhau để tool có thể ghép cặp (ví dụ: file_01.txt sẽ so sánh với file_01.md).

⚙️ Hướng dẫn sử dụng

Bước 1: Cấu hình đường dẫn

Mở file compare_md_txt.py, kéo xuống dưới cùng (dòng ~120) và chỉnh sửa 2 biến sau để trỏ đúng vào thư mục của bạn:

if __name__ == "__main__":
    # Tên thư mục chứa dữ liệu gốc (Ground Truth)
    ROOT_DATASET = "datatest" 
    
    # Tên thư mục chứa kết quả đánh giá (Prediction)
    ROOT_EVALUATION = "evaluation_olm"


Bước 2: Chạy đánh giá

Mở terminal tại thư mục chứa code và chạy lệnh:

python compare_md_txt.py


Bước 3: Xem kết quả

Trên màn hình: Tool sẽ hiển thị bảng tóm tắt độ chính xác trung bình.

File CSV: Kết quả chi tiết sẽ được lưu vào thư mục ROOT_EVALUATION với tên file dạng:

benchmark_dataset_in.csv

benchmark_dataset_tay.csv

Giải thích các cột trong file CSV:

Filename: Tên file được đánh giá.

Char_Acc: Độ chính xác ký tự (1 - CER).

Word_Acc: Độ chính xác từ (1 - WER).

CER: Character Error Rate (càng thấp càng tốt).

GT_Preview: Đoạn đầu của văn bản gốc.

Pred_Preview: Đoạn đầu của văn bản dự đoán (đã làm sạch).

🛠 Tùy chỉnh nâng cao

Nếu cấu trúc thư mục con của bạn khác mặc định, hãy tìm đến hàm auto_benchmark và sửa biến tasks:

tasks = {
    "TÊN_NHIỆM_VỤ": (
        # Đường dẫn con tới file gốc (tính từ ROOT_DATASET)
        os.path.join("folder_goc", "sub_folder"), 
        
        # Tên folder chứa kết quả (tính từ ROOT_EVALUATION)
        "folder_ket_qua"
    ),
}

