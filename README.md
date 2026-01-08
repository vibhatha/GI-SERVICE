# GI-SERVICE

**General Information Service** - API Adapter for OpenGIN (Open General Information Network)

## 🚀 Quick Start

**All project files are located in the `src/` directory.**

```bash
cd src
```

Please refer to [`src/README.md`](src/README.md) for complete documentation, installation instructions, and usage examples.

## 📁 Project Structure

```
GI-SERVICE/
├── LICENSE                   # License file
├── Procfile                  # Deployment configuration
├── chartFactory/             # Chart generation utilities
├── venv/                     # Virtual environment (git-ignored)
│
└── src/                      # 🎯 ALL PROJECT CODE IS HERE
    ├── main.py               # FastAPI application
    ├── README.md             # Full documentation
    ├── requirements.txt      # Dependencies
    ├── pyproject.toml        # Package configuration
    └── opendata/             # Python package
        ├── models/
        ├── services/
        ├── routers/
        └── dependencies/
```

## 🔗 Quick Links

- **Full Documentation**: [src/README.md](src/README.md)
- **Package Info**: [src/PACKAGE_INFO.md](src/PACKAGE_INFO.md)
- **API Documentation** (when running): http://localhost:8000/docs

## ⚡ Quick Commands

```bash
# Navigate to project directory
cd src

# Install dependencies
pip install -r requirements.txt

# Install the opendata package
pip install -e .

# Run the application
uvicorn main:app --reload

# Test the package
python test_package.py
```

---

**📖 For detailed information, please see [src/README.md](src/README.md)**

