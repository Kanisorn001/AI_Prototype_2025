# 🐍 Class III — Python Environment Setup

> การตั้งค่า Python Environment บน Linux Server  
> ใช้ Miniconda สำหรับจัดการ package และ environment แยกสำหรับแต่ละโปรเจค

---

## 📋 สารบัญ

1. [ติดตั้ง Miniconda](#-1-ติดตั้ง-miniconda)
2. [Activate & Initialize Conda](#-2-activate--initialize-conda)
3. [จัดการ Environment](#-3-จัดการ-environment)
4. [ติดตั้ง Package](#-4-ติดตั้ง-package)
5. [Python Command Line](#-5-python-command-line)
6. [Screen Session](#️-6-screen-session)
7. [สรุปคำสั่งที่ใช้บ่อย](#-สรุปคำสั่งที่ใช้บ่อย)

---

## 📦 1. ติดตั้ง Miniconda

Miniconda คือ package manager ขนาดเล็กสำหรับจัดการ Python environment  
เหมาะสำหรับ Server เพราะเบากว่า Anaconda และมีทุกอย่างที่จำเป็น

### ขั้นตอนการติดตั้ง (Linux — x86_64)

รันคำสั่งต่อไปนี้ **ทีละบรรทัด**:

```bash
# 1. สร้างโฟลเดอร์สำหรับติดตั้ง
mkdir -p ~/miniconda3

# 2. ดาวน์โหลด installer จากเว็บไซต์ทางการ
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
     -O ~/miniconda3/miniconda.sh

# 3. ติดตั้งแบบ batch mode (ไม่ต้องตอบคำถาม)
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# 4. ลบไฟล์ installer เมื่อติดตั้งเสร็จ
rm ~/miniconda3/miniconda.sh
```

| Option | ความหมาย |
|---|---|
| `-b` | Batch mode — ข้ามคำถามทั้งหมด |
| `-u` | Update — อัปเดตถ้ามี conda อยู่แล้ว |
| `-p ~/miniconda3` | ระบุ path ที่ต้องการติดตั้ง |

> 💡 **Tip:** ลิงก์ดาวน์โหลดเวอร์ชันล่าสุดได้ที่ [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)

---

## ✅ 2. Activate & Initialize Conda

### Activate Conda

หลังติดตั้งเสร็จให้ **ปิดแล้วเปิด Terminal ใหม่** หรือรันคำสั่งนี้:

```bash
source ~/miniconda3/bin/activate
```

### Initialize Conda

ตั้งค่าให้ `conda` ใช้งานได้กับทุก shell โดยอัตโนมัติ:

```bash
conda init --all
```

จากนั้น **ปิดแล้วเปิด Terminal ใหม่อีกครั้ง**  
ถ้าติดตั้งสำเร็จ จะเห็น `(base)` แสดงอยู่หน้า prompt เสมอ:

```
(base) kanisorn@vm:~$
```

### ตรวจสอบการติดตั้ง

```bash
conda --version      # ตรวจสอบ version ของ conda
python --version     # ตรวจสอบ version ของ Python
which python         # ดูว่า Python ที่ใช้อยู่มาจากที่ไหน
```

---

## 🛠️ 3. จัดการ Environment

Environment คือพื้นที่แยกสำหรับแต่ละโปรเจค ทำให้ package ไม่ปนกัน

```bash
# สร้าง environment ใหม่
conda create -n <env_name> python=3.10

# เข้าใช้งาน environment
conda activate <env_name>

# ออกจาก environment (กลับสู่ base)
conda deactivate

# ดู environment ทั้งหมดที่มี
conda env list

# ลบ environment
conda remove --name <env_name> --all
```

**ตัวอย่าง:**
```bash
conda create -n ai_project python=3.10
conda activate ai_project
# (ai_project) จะแสดงหน้า prompt แทน (base)
```

> 💡 **Tip:** ควรสร้าง environment แยกทุกโปรเจค ไม่ทำงานบน `(base)` โดยตรง

---

## 📥 4. ติดตั้ง Package

```bash
# ติดตั้งด้วย conda
conda install <package_name>
conda install numpy pandas scikit-learn matplotlib   # ติดตั้งหลายตัวพร้อมกัน

# ติดตั้งด้วย pip (ใช้เมื่อ conda หาไม่เจอ)
pip install <package_name>
pip install flask joblib

# ดู package ที่ติดตั้งอยู่ใน environment ปัจจุบัน
conda list
pip list
```

**Package พื้นฐานสำหรับงาน AI/ML:**

| Package | ใช้สำหรับ |
|---|---|
| `numpy` | คำนวณตัวเลข / array |
| `pandas` | จัดการข้อมูลตาราง |
| `scikit-learn` | Machine Learning |
| `matplotlib` | วาดกราฟ |
| `flask` | สร้าง Web App / API |
| `jupyter` | Python Notebook |
| `joblib` | บันทึก/โหลด model |

> 💡 **Tip:** บันทึก package ของโปรเจคไว้ใน `requirements.txt` เพื่อให้คนอื่น install ตามได้ง่าย
> ```bash
> pip freeze > requirements.txt        # บันทึก
> pip install -r requirements.txt      # ติดตั้งตาม
> ```

---

## 🐍 5. Python Command Line

```bash
python3 script.py          # รัน Python script
python3 -i script.py       # รันแล้วเปิด interactive shell ต่อ
python3                    # เข้า Python interactive shell
exit()                     # ออกจาก Python shell (ต้องมีวงเล็บ)
```

### เปิด VS Code จาก Terminal

```bash
code                       # เปิด VS Code ที่ directory ปัจจุบัน
code <filename>            # เปิดหรือสร้างไฟล์ใน VS Code
code .                     # เปิดทั้งโฟลเดอร์ปัจจุบันใน VS Code
```

> 💡 **Tip:** `exit()` ต้องมีวงเล็บเสมอ ถ้าพิมพ์ `exit` อย่างเดียวจะเห็นแค่ข้อความแต่ไม่ออก

---

## 🖥️ 6. Screen Session

`screen` ช่วยให้ process ทำงานต่อเนื่องบน server ได้  
แม้จะ **ปิด Terminal** หรือ **หลุดจาก SSH** โปรแกรมก็ยังทำงานอยู่

> 💡 เหมาะมากสำหรับการ train model หรือรัน server ระยะยาวบน VM

### สร้างและจัดการ Session

```bash
screen -S <session_name>      # สร้าง session ใหม่
screen -ls                    # ดูรายการ session ทั้งหมด
screen -R <session_name>      # กลับเข้า session (กด Tab ดูชื่อได้)
screen -R <id.session_name>   # กลับเข้า session โดยระบุ ID
```

**ตัวอย่าง:**
```bash
screen -S train_model         # สร้าง session ชื่อ train_model
python3 train.py              # รัน script ภายใน session
# กด Ctrl + A, D             # detach ออกมา (train ยังทำงานอยู่)
screen -R train_model         # กลับเข้าไปดูผลได้ทีหลัง
```

### Keyboard Shortcuts

| ปุ่ม | ความหมาย |
|---|---|
| `Ctrl + A, D` | **Detach** — ออกจาก session (โปรแกรมยังทำงานอยู่) |
| `Ctrl + A, K → Y` | **Kill** — ออกและลบ session ทิ้ง |
| `Ctrl + A, C` | สร้าง window ใหม่ภายใน session |
| `Ctrl + A, [` | **Freeze** — เข้าโหมด scroll ดู log ย้อนหลัง |
| `q + Enter` | ออกจากโหมด freeze |
| `Ctrl + C` | หยุด process ที่กำลังรันอยู่ |

### ลบ Session ที่ชื่อซ้ำ

เมื่อมี session ชื่อเดิมหลายตัว ให้ระบุด้วย ID:

```bash
# ขั้นตอนที่ 1 — ดูรายการ session ทั้งหมด
screen -ls
# Output: 12107.testscreen1  (Detached)

# ขั้นตอนที่ 2 — เข้า session ด้วย ID
screen -R 12107.testscreen1

# ขั้นตอนที่ 3 — ลบ session
# กด Ctrl + A, K แล้วกด Y เพื่อยืนยัน
```

---

## 📝 สรุปคำสั่งที่ใช้บ่อย

| คำสั่ง | ความหมาย |
|---|---|
| `source ~/miniconda3/bin/activate` | Activate conda |
| `conda init --all` | Initialize conda สำหรับทุก shell |
| `conda create -n <n> python=3.10` | สร้าง environment ใหม่ |
| `conda activate <n>` | เข้าใช้ environment |
| `conda deactivate` | ออกจาก environment |
| `conda env list` | ดู environment ทั้งหมด |
| `conda install <pkg>` | ติดตั้ง package |
| `pip freeze > requirements.txt` | บันทึก dependencies |
| `python3 script.py` | รัน Python script |
| `exit()` | ออกจาก Python shell |
| `screen -S <n>` | สร้าง screen session |
| `screen -ls` | ดู session ทั้งหมด |
| `screen -R <n>` | กลับเข้า session |
| `Ctrl + A, D` | Detach จาก session |

---

← [Class II — Cloud Virtual Machines](./Lecture_Class_II.md) · [README](../README.md) · [Class IV — Web Page →](./Lecture_Class_IV.md)
