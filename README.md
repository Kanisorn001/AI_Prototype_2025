# 🤖 AI_Prototype_2025

> **SC664401** — Prototyping for Artificial Intelligence and Machine Learning System  
> การสร้างต้นแบบสำหรับระบบปัญญาประดิษฐ์และการเรียนรู้ของเครื่อง

**Kanisorn Kudklang · 653020202-7 · คณิศร กุดกลาง**

🌐 **[Web Page](#)** · 📱 **[Web App](#)** · 

---

## 📅 Calendar

| CLASS | DESCRIPTION | LECTURE |
|:---:|---|:---:|
| I | Ubuntu Command Line | [📄 Notes](./lectures/Lecture_Class_I.md) |
| II | Virtual Machines | [📄 Notes](./lectures/Lecture_Class_II.md) |
| III | Cloud VM | [📄 Notes](./lectures/Lecture_Class_III.md) |
| IV | Web Page | [📄 Notes](./lectures/Lecture_Class_IV.md) |
| V | Environment & Conda | [📄 Notes](./lectures/Lecture_Class_V.md) |
| VI | Web Service | [📄 Notes](./lectures/Lecture_Class_VI.md) |

---

## 📔 Contents

<details>
<summary><b>🐧 Class I — Ubuntu Command Line</b></summary>
<br>

คลาสแรกเรียนการใช้งาน Terminal บน Linux (Ubuntu) ซึ่งเป็นพื้นฐานสำคัญสำหรับการทำงานบน Server และ Cloud

### 📍 Navigation

```bash
pwd              # แสดง path ของตำแหน่งปัจจุบัน
ls               # แสดงรายการไฟล์/โฟลเดอร์
ls -l            # แสดงแบบละเอียด (long format)
ls -ltr          # เรียงตามเวลา จากเก่าไปใหม่
cd <folder>      # เข้าโฟลเดอร์
cd ..            # ออก 1 ขั้น
cd ../..         # ออก 2 ขั้น
```

### 📁 จัดการไฟล์และโฟลเดอร์

```bash
mkdir <name>           # สร้างโฟลเดอร์ใหม่
vi <filename>          # สร้าง/เปิดไฟล์ด้วย editor
  # กด i        → เข้าโหมดแก้ไข
  # กด Esc      → ออกจากโหมดแก้ไข
  # กด :wq      → บันทึกและออก
  # กด :q!      → ออกโดยไม่บันทึก
cat <filename>         # อ่านเนื้อหาในไฟล์
mv <src> <dest>        # ย้าย หรือเปลี่ยนชื่อไฟล์
cp <src> <dest>        # คัดลอกไฟล์
rm <filename>          # ลบไฟล์
rm -r <folder>         # ลบโฟลเดอร์ทั้งหมด (recursive)
```

### 🔧 คำสั่งอื่นที่มีประโยชน์

```bash
man <command>    # ดูคู่มือการใช้งานของคำสั่งนั้นๆ
htop             # ดู RAM / CPU usage แบบ real-time (ต้องติดตั้งก่อน)
```

> 💡 **Tip:** ถ้าชื่อโฟลเดอร์มีช่องว่าง เช่น `Class 4` ให้พิมพ์ `cd Class\ 4` หรือ `cd "Class 4"`

</details>

---

<details>
<summary><b>🖥️ Class II — Virtual Machines</b></summary>
<br>

เรียนการสร้างและจัดการ Virtual Machine รวมถึงการเพิ่มผู้ใช้เข้าสู่ระบบ

### 🔐 เชื่อมต่อ Server ด้วย SSH

> SSH ย่อมาจาก **Secure Shell** — ช่องทางการเชื่อมต่อที่เข้ารหัสข้อมูลตลอดการส่ง

```bash
ssh username@IPaddress       # เชื่อมต่อ Server
exit                         # ออกจาก session
```

### 👥 จัดการผู้ใช้

```bash
sudo adduser <username>              # เพิ่มผู้ใช้ใหม่
sudo adduser <username> sudo         # ให้สิทธิ์ superuser
sudo groups <username>               # เช็คว่าอยู่ใน group ไหน
sudo usermod <friend> <myname>       # ย้าย group
htop                                 # ดูการเคลื่อนไหวบน server
```

> 💡 **Tip:** ควรให้สิทธิ์ `sudo` เฉพาะคนที่ไว้วางใจเท่านั้น เพราะสามารถสั่งได้ทุกอย่างในระบบ

</details>

---

<details>
<summary><b>☁️ Class III — Cloud VM (Microsoft Azure)</b></summary>
<br>

เรียนการสร้าง Virtual Machine บน Cloud ผ่าน Microsoft Azure และการส่งไฟล์ระหว่างเครื่องกับ Cloud

### 🚀 สร้าง VM บน Azure

1. เข้า **Portal Azure** → **Education** → **Virtual Machines** → **Create**
2. ตั้งชื่อ VM, username, และ password
3. คัดลอก **Public IP Address** ที่ได้มา
4. เชื่อมต่อด้วย SSH: `ssh username@<IP>`

### 📤 ส่งไฟล์ด้วย SCP (Secure Copy)

```bash
# รูปแบบ: scp <ต้นทาง> <ปลายทาง>

# ส่งไฟล์จากเครื่องเราไป Cloud
scp ./script.py user@IP:~/code/.

# ส่งทั้งโฟลเดอร์ไป Cloud
scp -r myfolder/ user@IP:~/code/.

# ดึงไฟล์จาก Cloud มาเครื่องเรา
scp user@IP:/home/user/code/script.py /Users/me/Desktop
```

### 🖥️ จัดการ Session ด้วย Screen

```bash
screen -S <session_name>    # สร้าง session ใหม่
screen -R                   # กลับเข้า session ที่มีอยู่
# Ctrl + A, D               → ออกจาก session (แต่ยังทำงานอยู่)
# Ctrl + A, K, Y            → ออกและลบ session
```

> 💡 **Tip:** `screen` มีประโยชน์มากเวลารัน process ที่ใช้เวลานาน เพราะถ้าปิด terminal ไป process จะยังทำงานต่อได้

</details>

---

<details>
<summary><b>🌐 Class IV — Web Page Development</b></summary>
<br>

เรียนพื้นฐานการพัฒนาเว็บ ทั้ง Frontend และ Backend

### 🔄 HTTP Methods

| Method | คำอธิบาย | ใช้เมื่อ |
|---|---|---|
| **GET** | ดึงข้อมูลจาก server, ข้อมูลแนบมากับ URL | ค้นหาข้อมูล, เปิดหน้าเว็บ |
| **POST** | ส่งข้อมูลใน request body | ส่งฟอร์ม, login, สร้างข้อมูล |

### 🎨 Frontend

**HTML** — กำหนดโครงสร้างหน้าเว็บ
```html
<!DOCTYPE html>
<html>
  <head>  <!-- ส่วนหัว: title, meta, CSS links -->
  <body>  <!-- ส่วนเนื้อหาที่แสดงบนหน้าจอ -->
</html>
```

**CSS** — ตกแต่งและจัดรูปแบบหน้าเว็บ

| ประเภท | คำอธิบาย |
|---|---|
| Responsive | ปรับขนาดอัตโนมัติตาม screen size |
| Adaptive (AWD) | มีหลาย layout สำหรับแต่ละขนาดหน้าจอ |
| Static | เนื้อหาคงที่ ไม่เปลี่ยนแปลง |
| Dynamic | เนื้อหาเปลี่ยนได้จาก database |
| SPA | โหลดหน้าเดียว เปลี่ยน content ไม่ reload |
| PWA | ผสมเว็บกับ mobile app |
| Mobile-first | ออกแบบสำหรับมือถือเป็นหลัก |

**JavaScript** — เพิ่มการโต้ตอบและ logic ให้หน้าเว็บ
- Dynamic Typing — ไม่ต้องระบุ data type
- Event-driven — ทำงานตาม event เช่น click, input
- รองรับ Node.js สำหรับ server-side

### ⚙️ Backend (Python + Flask)

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

</details>

---

<details>
<summary><b>🐍 Class V — Environment & Conda</b></summary>
<br>

เรียนการจัดการ Python Environment ด้วย Conda เพื่อแยก dependencies ของแต่ละโปรเจคออกจากกัน

### 📦 ติดตั้ง Conda

- **Miniconda** (แนะนำ — เบากว่า) → [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Anaconda** (ครบ แต่หนักกว่า) → [anaconda.com](https://www.anaconda.com)

```bash
conda --version    # ตรวจสอบว่าติดตั้งสำเร็จ
```

### 🛠️ จัดการ Environment

```bash
conda create -n <env_name> python=3.10   # สร้าง environment ใหม่
conda activate <env_name>                # เข้าใช้งาน
conda deactivate                         # ออกจาก environment
conda remove --name <env_name> --all     # ลบ environment
```

### 📥 ติดตั้ง Package

```bash
conda install pandas          # ติดตั้ง package
conda install numpy scikit-learn flask   # ติดตั้งหลายตัวพร้อมกัน
pip install <package>         # ใช้ pip แทน conda ได้
```

> 💡 **Tip:** ควรสร้าง environment แยกสำหรับแต่ละโปรเจค เพื่อป้องกัน library conflicts

### 🐍 Python Main Function

```python
def main():
    print("Hello from main!")

if __name__ == "__main__":
    main()
```

> `if __name__ == "__main__"` คือเงื่อนไขที่บอกว่า "ถ้าไฟล์นี้ถูกรันโดยตรง (ไม่ใช่ถูก import) ให้เรียก main()"

### 📨 รับ Input จาก Command Line (argparse)

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', default='World')
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

```bash
python script.py --name Kanisorn   # Output: Hello, Kanisorn!
```

</details>

---

<details>
<summary><b>🔌 Class VI — Web Service & REST API</b></summary>
<br>

เรียนการสร้าง Web Service ด้วย Flask เพื่อรับ-ส่งข้อมูลระหว่างระบบต่างๆ ผ่าน HTTP

### 🔄 Web Service ทำงานอย่างไร?

```
Client  →  [Request]  →  Server
Client  ←  [Response] ←  Server
```

1. **Request** — ส่งคำขอพร้อมข้อมูลไปยัง server
2. **Process** — Server รับและประมวลผล
3. **Response** — Server ส่งผลลัพธ์กลับมา

### 🖥️ สร้าง API ด้วย Flask

```python
from flask import Flask, request
import json

app = Flask(__name__)

# GET — รับข้อมูลจาก URL parameter
@app.route('/api', methods=['GET'])
def get_data():
    name = request.args.get('name')
    return f"Hello, {name}!"

# POST — รับข้อมูลจาก request body
@app.route('/api', methods=['POST'])
def post_data():
    payload = json.loads(request.data.decode("utf-8"))
    print(payload)
    return json.dumps({'status': 'received!'})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

### 📡 เรียกใช้ API ด้วย Python

```python
import requests
import json

# GET request
response = requests.get('http://localhost:5001/api?name=Kanisorn')

# POST request
payload = {'name': 'Kanisorn', 'age': 22}
response = requests.post('http://localhost:5001/api', data=json.dumps(payload))
print(response.json())
```

> 💡 **Tip:** ใช้ [Postman](https://www.postman.com/) หรือ `curl` เพื่อทดสอบ API ได้สะดวกขึ้น



## 🗂️ Projects

| # | Project | Description | Link |
|:---:|---|---|:---:|
| 1 | 🌸 Iris AI Expert System | จำแนกสายพันธุ์ดอกไอริสด้วย Random Forest + Flask | [web_app.py](./web_app.py) |
| 2 | ⚗️ Model Training | Train และบันทึก ML Model ด้วย scikit-learn | [train.py](./train.py) |
| 3 | 🔌 Flask API Demo | ตัวอย่าง REST API ด้วย Flask (GET / POST) | [myfristflask.py](./myfristflask.py) |

---
