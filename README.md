# FitMate - Final Project PBKK

FitMate adalah aplikasi web pencatat gaya hidup sehat yang berfokus pada pelacakan BMI, TDEE, jurnal kalori harian, serta menyediakan rekomendasi menu sehat dan panduan diet. Proyek ini dikembangkan menggunakan arsitektur pemisahan Frontend dan Backend.

## Struktur Direktori Proyek

```text
fp-pbkk-fitmate/
├── .venv/                 # Environment uv (Tidak di-push ke git!)
├── .gitignore             # Mengabaikan .venv/ dan *.db
├── requirements.txt       # Daftar dependencies
│
├── backend/               # Area Kerja Tim BE
│   ├── main.py            # Entry point FastAPI (hanya routing & setup app)
│   ├── database.py        # Setup engine & session SQLAlchemy
│   ├── models.py          # Definisi tabel database (ORM)
│   ├── schemas.py         # Pydantic models untuk validasi input/output
│   ├── crud.py            # Logika eksekusi Insert, Update, Delete, Select
│   │
│   └── routers/           # Pengelompokan Endpoint API
│       ├── auth.py        # /api/auth/login, /api/auth/register
│       ├── kalkulator.py  # /api/kalkulator/bmi, /api/kalkulator/tdee
│       ├── resep.py       # /api/resep/
│       └── tracker.py     # /api/tracker/weight, /api/tracker/food
│
└── frontend/              # Area Kerja Tim FE
    ├── app.py             # Entry point Streamlit (Halaman utama/Login)
    ├── pages/             # Multi-page Streamlit
    │   ├── 1_Kalkulator_Kesehatan.py
    │   ├── 2_Rekomendasi_Menu.py
    │   ├── 3_Panduan_Diet.py
    │   └── 4_Dashboard_Jurnal.py
    │
    └── utils/             
        └── api_client.py  # Fungsi requests (GET/POST) untuk komunikasi ke Backend