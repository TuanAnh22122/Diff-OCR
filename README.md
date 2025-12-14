# 📊 Automatic ASR Benchmark Tool

Công cụ Python dùng để **đánh giá chất lượng ASR (Automatic Speech Recognition)** bằng cách so sánh text ground-truth (`.txt`) và kết quả nhận dạng (`.md`) thông qua các chỉ số **CER** và **WER**.

---

## 🚀 Tính năng chính

- 🔍 Tự động quét & ghép cặp dataset – output theo quy tắc đặt tên
- 📐 Tính **Character Error Rate (CER)** và **Word Error Rate (WER)**
- 📊 Xuất báo cáo CSV chi tiết cho từng dataset
- 🧹 Làm sạch text nâng cao trước khi đánh giá
- 🧩 Dễ mở rộng cho nhiều bộ dữ liệu khác nhau

---

## 📂 Cấu trúc thư mục

```text
project_root/
├── datatest/
│   ├── datatest_in/
│   │   └── txt/            # Ground truth (.txt)
│   └── datatest_tay/
│       └── txt/
│
├── evaluation_chandra/
│   ├── evaluation_output_dataset_in/   # Prediction (.md)
│   └── evaluation_output_dataset_tay/
│
├── eval.py
└── README.md
```

---

## ⚙️ Cài đặt môi trường

```bash
pip install pandas jiwer tqdm tabulate
```

Khuyến nghị Python **>= 3.8**

---

## ▶️ Cách sử dụng

### 1️⃣ Cấu hình đường dẫn

Mở file `eval.py` và chỉnh 2 dòng sau:

```python
ROOT_DATASET = "datatest"
ROOT_EVALUATION = "evaluation_chandra"
```

### 2️⃣ Chạy đánh giá

```bash
python eval.py
```

---

## 📈 Kết quả đầu ra

- Hiển thị **độ chính xác trung bình** trên terminal
- Sinh file CSV:

```text
benchmark_dataset_in.csv
benchmark_dataset_tay.csv
```

Mỗi file bao gồm:

| Column | Ý nghĩa |
|------|--------|
| Filename | Tên file | 
| Char_Acc | Độ chính xác ký tự | 
| Word_Acc | Độ chính xác từ | 
| CER | Character Error Rate | 
| GT_Preview | Preview ground truth | 
| Pred_Preview | Preview prediction |

---

## 🧠 Nguyên lý đánh giá

- **CER** = số lỗi ký tự / tổng ký tự
- **WER** = số lỗi từ / tổng từ

Độ chính xác:

```text
Accuracy = 1 - Error Rate
```

---

## 🛠 Mở rộng

Bạn có thể thêm dataset mới trong biến `tasks`:

```python
tasks = {
    "DATASET ABC": ("datatest_abc/txt", "evaluation_output_dataset_abc")
}
```

---

## 🧑‍💻 Tác giả

- Internal ASR Evaluation Tool
- Dành cho nghiên cứu & kiểm thử mô hình nhận dạng tiếng nói

---

## 📄 License

MIT License (tuỳ chỉnh nếu cần)
