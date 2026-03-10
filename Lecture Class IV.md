# 🔧 Class IV — Environment & Version Control

> การจัดการ Python Environment ด้วย Conda  
> และการควบคุมเวอร์ชันโค้ดด้วย Git & GitHub

---

## 📋 สารบัญ

1. [ติดตั้ง Conda](#-1-ติดตั้ง-conda)
2. [จัดการ Conda Environment](#-2-จัดการ-conda-environment)
3. [ติดตั้ง Package](#-3-ติดตั้ง-package)
4. [Git & GitHub เบื้องต้น](#-4-git--github-เบื้องต้น)
5. [บันทึกโค้ดขึ้น GitHub](#-5-บันทึกโค้ดขึ้น-github)
6. [GitHub Personal Access Token](#-6-github-personal-access-token)
7. [Tips & Shortcuts](#-7-tips--shortcuts)
8. [สรุปคำสั่งที่ใช้บ่อย](#-สรุปคำสั่งที่ใช้บ่อย)

---

## 📦 1. ติดตั้ง Conda

Conda มีให้เลือก 2 แบบตามความต้องการ:

| | Miniconda | Anaconda |
|---|---|---|
| **ขนาด** | เล็ก (~400 MB) | ใหญ่ (~3 GB) |
| **เหมาะกับ** | Server, VM | เครื่อง local ทั่วไป |
| **GUI** | ❌ | ✅ |
| **Pre-installed packages** | น้อย (conda เท่านั้น) | ครบถ้วน |
| **Download** | [miniconda](https://docs.conda.io/en/latest/miniconda.html) | [anaconda](https://www.anaconda.com/products/distribution) |

> 💡 **แนะนำ:** ใช้ **Miniconda** บน Server เพราะเบาและติดตั้งเฉพาะที่ต้องการได้

### ตรวจสอบการติดตั้ง

```bash
conda --version      # แสดง version เช่น conda 24.1.2
python --version     # แสดง Python version ปัจจุบัน
```

---

## 🛠️ 2. จัดการ Conda Environment

Environment คือพื้นที่แยกสำหรับแต่ละโปรเจค ทำให้ package และ Python version ไม่ปนกัน  
เมื่อเปิด Terminal ใหม่จะอยู่ที่ environment ชื่อ `(base)` เสมอ

### สร้าง Environment ใหม่

```bash
conda create --name <env_name> python=<version>
```

**ตัวอย่าง:**
```bash
conda create --name testpy38 python=3.8
conda create --name ai_project python=3.11
```

### เข้า / ออก Environment

```bash
conda activate <env_name>     # เข้าใช้งาน environment
conda deactivate              # ออกกลับสู่ (base)
```

เมื่อ activate สำเร็จ จะเห็นชื่อ environment แสดงหน้า prompt:
```
(base) user@host:~$           # ก่อน activate
(ai_project) user@host:~$     # หลัง activate
```

### จัดการ Environment

```bash
conda env list                          # ดู environment ทั้งหมด
conda remove --name <env_name> --all    # ลบ environment
conda env export > environment.yml      # export environment เป็นไฟล์
conda env create -f environment.yml     # สร้าง environment จากไฟล์
```

> 💡 **Tip:** `environment.yml` ใช้แชร์ให้ทีมสร้าง environment เหมือนกันได้ทันที

---

## 📥 3. ติดตั้ง Package

> ⚠️ ต้อง `conda activate <env_name>` ก่อนติดตั้ง Package ทุกครั้ง

```bash
# ติดตั้งด้วย conda
conda install <package_name>
conda install pandas numpy matplotlib    # ติดตั้งหลายตัวพร้อมกัน

# ติดตั้งด้วย pip (เมื่อหาใน conda ไม่เจอ)
pip install <package_name>

# ดู package ที่ติดตั้งอยู่ใน environment ปัจจุบัน
conda list
pip list
```

**บันทึกและแชร์ dependencies:**
```bash
pip freeze > requirements.txt        # บันทึก package ทั้งหมด
pip install -r requirements.txt      # ติดตั้งตาม requirements
```

---

## 🐙 4. Git & GitHub เบื้องต้น

**Git** คือระบบ Version Control บนเครื่อง — ติดตามการเปลี่ยนแปลงของโค้ด  
**GitHub** คือ platform เก็บโค้ดบน Cloud — แชร์และ backup โค้ดได้

```
Working Directory  →  Staging Area  →  Local Repo  →  GitHub (Remote)
     (แก้ไขไฟล์)      (git add)        (git commit)    (git push)
```

### ตั้งค่า Git (ทำครั้งเดียว)

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# ตรวจสอบการตั้งค่า
git config --list
```

### Clone Repository

```bash
git clone <repository_url>
git clone https://github.com/username/repo-name.git
```

---

## 💾 5. บันทึกโค้ดขึ้น GitHub

### ลำดับขั้นตอน: `pull → add → commit → push`

```bash
# 1. ดึงเวอร์ชันล่าสุดจาก GitHub ก่อนเสมอ
git pull

# 2. เพิ่มไฟล์เข้า staging area
git add <file_name>        # เพิ่มไฟล์เดี่ยว
git add .                  # เพิ่มทุกไฟล์ที่มีการเปลี่ยนแปลง

# 3. Commit พร้อมข้อความอธิบาย
git commit -m "อธิบายการเปลี่ยนแปลง"

# 4. Push ขึ้น GitHub
git push
```

### ตรวจสอบสถานะ

```bash
git status
```

| สีของไฟล์ | ความหมาย |
|---|---|
| 🔴 แดง | ไฟล์มีการเปลี่ยนแปลงแต่ยังไม่ได้ `git add` |
| 🟢 เขียว | ไฟล์อยู่ใน staging แล้ว รอ `git commit` |
| ไม่แสดง | ทุกอย่าง commit แล้ว ไม่มีการเปลี่ยนแปลง |

### คำสั่งอื่นที่มีประโยชน์

```bash
git log --oneline          # ดูประวัติ commit แบบย่อ
git diff <file_name>       # ดูว่าไฟล์เปลี่ยนแปลงอะไรบ้าง
git restore <file_name>    # ยกเลิกการเปลี่ยนแปลง (ก่อน add)
git reset HEAD <file_name> # นำไฟล์ออกจาก staging (หลัง add)
```

> 💡 **Tip:** เขียน commit message ให้สื่อความหมาย เช่น `"add iris prediction feature"` ดีกว่า `"update"` หรือ `"fix"`

---

## 🔑 6. GitHub Personal Access Token

GitHub ไม่รับ password ธรรมดาแล้ว ต้องใช้ **Personal Access Token (PAT)** แทน

### สร้าง Token

```
GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic) → Generate new token
```

**ตั้งค่าที่แนะนำ:**
- **Note:** ตั้งชื่อให้จำได้ เช่น `vm-server-token`
- **Expiration:** 90 days หรือ No expiration
- **Scope:** เลือก `repo` เพื่อ push/pull ได้

> ⚠️ **สำคัญ:** Token จะแสดงเพียง **ครั้งเดียว** หลังสร้าง ควร copy เก็บไว้ทันที

### ใช้ Token แทน Password

เมื่อ `git push` แล้วถาม password ให้วาง Token แทน:
```
Username: your-github-username
Password: <วาง Personal Access Token ตรงนี้>
```

### บันทึก Token ให้ไม่ต้องพิมพ์ทุกครั้ง

```bash
git config --global credential.helper store
# หลังจาก push ครั้งแรก Git จะจำ token ไว้ให้อัตโนมัติ
```

---

## ⚡ 7. Tips & Shortcuts

### ค้นหาคำสั่งที่เคยใช้

```bash
Ctrl + R        # ค้นหาคำสั่งย้อนหลัง — พิมพ์ keyword แล้วกด Enter
history         # แสดงคำสั่งทั้งหมดที่เคยใช้
history | grep git   # กรองเฉพาะคำสั่ง git
```

### Tab Completion

```bash
conda activate test<Tab>    # กด Tab เพื่อเติมชื่อ environment อัตโนมัติ
git che<Tab>                # เติมเป็น git checkout
```

### .gitignore — ไฟล์ที่ไม่ต้องการ push ขึ้น GitHub

สร้างไฟล์ `.gitignore` ที่ root ของโปรเจค:
```
# Python
__pycache__/
*.pyc
*.pyo
venv/
.env

# Model files
*.pkl
*.h5

# System
.DS_Store
```

> 💡 **Tip:** ใช้ [gitignore.io](https://www.toptal.com/developers/gitignore) เพื่อ generate `.gitignore` อัตโนมัติ

---

## 📝 สรุปคำสั่งที่ใช้บ่อย

**Conda:**

| คำสั่ง | ความหมาย |
|---|---|
| `conda create -n <n> python=3.10` | สร้าง environment |
| `conda activate <n>` | เข้าใช้ environment |
| `conda deactivate` | ออกจาก environment |
| `conda env list` | ดู environment ทั้งหมด |
| `conda install <pkg>` | ติดตั้ง package |
| `conda list` | ดู package ที่ติดตั้ง |

**Git:**

| คำสั่ง | ความหมาย |
|---|---|
| `git config --global user.name` | ตั้งชื่อผู้ใช้ |
| `git clone <url>` | clone repository |
| `git pull` | ดึงเวอร์ชันล่าสุด |
| `git add <file>` | เพิ่มไฟล์เข้า staging |
| `git commit -m "msg"` | บันทึกการเปลี่ยนแปลง |
| `git push` | push ขึ้น GitHub |
| `git status` | ดูสถานะไฟล์ |
| `git log --oneline` | ดูประวัติ commit |

---

← [Class III — Python Environment Setup](./Lecture_Class_III.md) · [README](../README.md) · [Class V — Web Page →](./Lecture_Class_V.md)
