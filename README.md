🔮 Diff-OCR: OCR Benchmark & Text Comparison ToolCông cụ tự động đánh giá độ chính xác của mô hình OCR / Text GenerationSo sánh kết quả Prediction (.md) với dữ liệu Ground Truth (.txt) một cách chính xác và hiệu quả.📑 Mục lụcTính năng chínhYêu cầu cài đặtCấu trúc thư mụcHướng dẫn sử dụngBáo cáo kết quả🚀 Tính năng chínhTính năngMô tả chi tiết🔄 So sánh đa định dạngHỗ trợ so sánh chéo giữa file .txt (nhãn gốc) và file .md (kết quả model).🧹 Smart PreprocessingTự động loại bỏ cú pháp Markdown (ảnh, link, header, bold...) và chuẩn hóa văn bản (lowercase, strip spaces) trước khi so sánh.📊 Metrics chuyên sâuTính toán tự động CER (Character Error Rate), WER (Word Error Rate) và Accuracy.📈 Báo cáo trực quanHiển thị bảng tóm tắt trên Terminal và xuất file .csv chi tiết cho từng cặp dữ liệu để tiện debug.📦 Yêu cầu cài đặtĐảm bảo bạn đã cài đặt Python. Cài đặt các thư viện phụ thuộc bằng lệnh sau:pip install pandas jiwer tqdm tabulate
📚 Tech StackPandas: Xử lý dữ liệu bảng và xuất CSV.Jiwer: Thư viện lõi tính toán khoảng cách Levenshtein (CER/WER).Tqdm: Hiển thị thanh tiến trình (Progress bar).Tabulate: Format bảng kết quả đẹp mắt trên console.📂 Cấu trúc thư mụcĐể tool hoạt động chính xác, hãy tổ chức thư mục dự án theo cấu trúc cây dưới đây:Project_Root/
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
[!IMPORTANT] Lưu ý quan trọng: File kết quả và file gốc phải có cùng tên để thuật toán ghép cặp hoạt động chính xác. Ví dụ: data_01.txt sẽ được so khớp với data_01.md.⚙️ Hướng dẫn sử dụng1️⃣ Cấu hình đường dẫnMở file compare_md_txt.py và chỉnh sửa biến đường dẫn ở cuối file nếu cần:if __name__ == "__main__":
    # Tên thư mục chứa dữ liệu gốc (Ground Truth)
    ROOT_DATASET = "datatest"
    
    # Tên thư mục chứa kết quả đánh giá (Prediction)
    ROOT_EVALUATION = "evaluation_olm"
2️⃣ Chạy đánh giáChạy lệnh sau tại thư mục gốc của dự án:python compare_md_txt.py
3️⃣ Tùy chỉnh nâng caoĐể thêm tập dữ liệu mới, sửa biến tasks trong hàm auto_benchmark:tasks = {
    "DATASET_MOI": (
        # Đường dẫn tới file gốc (join path từ ROOT_DATASET)
        os.path.join("folder_goc", "sub_path"), 
        
        # Tên folder kết quả (nằm trong ROOT_EVALUATION)
        "folder_ket_qua"
    ),
}
📊 Báo cáo kết quảSau khi chạy, tool sẽ xuất file CSV với các trường thông tin sau:Tên cộtÝ nghĩaGhi chúFilenameTên file được đánh giáChar_AccĐộ chính xác ký tự1 - CERWord_AccĐộ chính xác từ1 - WERCERCharacter Error RateCàng thấp càng tốtGT_PreviewVăn bản gốc (Ground Truth)Dùng để kiểm tra nhanhPred_PreviewVăn bản dự đoán (Prediction)Đã qua xử lý làm sạchDeveloped for Internal Benchmarking
