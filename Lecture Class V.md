# 🌐 Class V — Deploy Web App on Azure VM

> การนำ Flask Web Application ขึ้นรันบน Azure Virtual Machine  
> เพื่อให้เข้าถึงได้จากภายนอกผ่าน Public IP Address

---

## 📋 สารบัญ

1. [ภาพรวมการ Deploy](#-1-ภาพรวมการ-deploy)
2. [เชื่อมต่อ VM และเตรียมโปรเจค](#-2-เชื่อมต่อ-vm-และเตรียมโปรเจค)
3. [ตั้งค่า Flask App สำหรับ Production](#-3-ตั้งค่า-flask-app-สำหรับ-production)
4. [ตั้งค่า Port บน Azure Portal](#-4-ตั้งค่า-port-บน-azure-portal)
5. [ติดตั้ง Environment และรัน App](#-5-ติดตั้ง-environment-และรัน-app)
6. [รัน App ค้างไว้ด้วย Screen](#️-6-รัน-app-ค้างไว้ด้วย-screen)
7. [ใช้งานครั้งต่อไป](#-7-ใช้งานครั้งต่อไป)
8. [สรุปขั้นตอนทั้งหมด](#-สรุปขั้นตอนทั้งหมด)

---

## 🗺️ 1. ภาพรวมการ Deploy

```
เครื่องเรา  ──ssh──▶  Azure VM  ──port──▶  Internet
                       Flask App              http://IP:PORT
```

**สิ่งที่ต้องเตรียม:**
- Azure VM ที่รันอยู่ และ Public IP Address
- โปรเจค Flask บน GitHub
- Port ที่ไม่ซ้ำกับเพื่อนที่ใช้ VM เครื่องเดียวกัน

> ⚠️ **สำคัญ:** ถ้าใช้ VM เครื่องเดียวกันหลายคน ต้องตั้ง port คนละหมายเลขเสมอ เช่น 5001, 5002, 5003 ...

---

## 🔌 2. เชื่อมต่อ VM และเตรียมโปรเจค

### Login เข้า VM

```bash
ssh username@IPaddress
# ตัวอย่าง
ssh kanisorn@23.101.7.184
```

### Pull โปรเจคจาก GitHub

```bash
# ถ้ายังไม่เคย clone
git clone <repository_url>
cd <project_folder>

# ถ้า clone แล้ว ให้ดึงเวอร์ชันล่าสุด
cd <project_folder>
git pull
```

---

## ⚙️ 3. ตั้งค่า Flask App สำหรับ Production

Flask ที่รันด้วย `localhost` หรือ `127.0.0.1` จะเข้าถึงได้เฉพาะภายในเครื่องเท่านั้น  
ต้องเปลี่ยนเป็น `0.0.0.0` เพื่อให้รับ request จากภายนอกได้

### แก้ไขไฟล์ด้วย vi

```bash
vi web_app.py
```

**ค้นหาและแก้ไขบรรทัดนี้:**

```python
# ❌ ก่อนแก้ไข — เข้าถึงได้เฉพาะภายในเครื่อง
app.run(host='localhost', port=5000, debug=True)

# ✅ หลังแก้ไข — เปิดให้เข้าถึงจากภายนอกได้
app.run(host='0.0.0.0', port=5002, debug=True)
```

**คำสั่งพื้นฐานใน vi:**

```
i         → เข้าโหมดแก้ไข
Esc       → ออกจากโหมดแก้ไข
:wq       → บันทึกและออก
:q!       → ออกโดยไม่บันทึก
```

> 💡 **Tip:** เลือก port ที่ไม่ซ้ำกับเพื่อน เช่น ใช้ 4 หลักสุดท้ายของรหัสนักศึกษา

---

## 🔓 4. ตั้งค่า Port บน Azure Portal

Port ที่ Flask ใช้ต้องถูกเปิดบน Azure ด้วย ไม่เช่นนั้น request จากภายนอกจะถูก block

```
Azure Portal
  → Virtual Machines
    → เลือก VM ของเรา
      → Networking
        → Add inbound port rule
```

**ตั้งค่า Inbound Port Rule:**

| Field | ค่าที่ใส่ |
|---|---|
| Source | Any |
| Destination port ranges | `5002` (port ที่เราใช้) |
| Protocol | TCP |
| Action | Allow |
| Priority | 310 (หรือตัวเลขที่ไม่ซ้ำ) |
| Name | `port-5002` |

> ⚠️ รอสักครู่หลังกด Save เพราะ Azure ใช้เวลาอัปเดต rule ประมาณ 1-2 นาที

---

## 🐍 5. ติดตั้ง Environment และรัน App

### ครั้งแรก — ติดตั้ง Environment

```bash
# สร้าง environment ใหม่
conda create -n ai_env python=3.10

# เข้าใช้งาน
conda activate ai_env

# ติดตั้ง dependencies
pip install flask scikit-learn joblib numpy pandas

# หรือถ้ามี requirements.txt
pip install -r requirements.txt
```

### รัน Flask App

```bash
python web_app.py
```

**ถ้าทุกอย่างถูกต้อง จะเห็น output แบบนี้:**
```
 * Running on http://0.0.0.0:5002
 * Running on http://23.101.7.184:5002
 * Press CTRL+C to quit
```

### เข้าถึง Web App

เปิดเบราว์เซอร์แล้วไปที่:
```
http://<YOUR_IP>:<YOUR_PORT>

# ตัวอย่าง
http://23.101.7.184:5002
```

> 💡 **อย่าลืมเปลี่ยน IP เป็น Public IP ของ VM ตัวเอง**

---

## 🖥️ 6. รัน App ค้างไว้ด้วย Screen

ถ้ารัน `python web_app.py` แบบปกติ เมื่อปิด Terminal หรือหลุด SSH — App จะหยุดทำงานทันที  
ใช้ `screen` เพื่อให้ App ทำงานต่อแม้จะออกจาก SSH แล้ว

### สร้าง Screen Session และรัน App

```bash
# สร้าง session
screen -S myapp

# ภายใน screen — activate env และรัน app
conda activate ai_env
python web_app.py

# Detach ออกจาก session (App ยังทำงานอยู่)
# กด Ctrl + A แล้วกด D
```

### ตรวจสอบและจัดการ Session

```bash
screen -ls                    # ดู session ทั้งหมดที่มีอยู่
screen -R myapp               # กลับเข้า session
screen -R <id.session_name>   # กลับเข้าด้วย ID (กรณีชื่อซ้ำ)
```

**Keyboard Shortcuts:**

| ปุ่ม | ความหมาย |
|---|---|
| `Ctrl + A, D` | Detach — ออกจาก session (App ยังทำงาน) |
| `Ctrl + A, K → Y` | Kill — หยุด App และลบ session |
| `Ctrl + C` | หยุด process ที่รันอยู่ใน session |

---

## 🔄 7. ใช้งานครั้งต่อไป

เมื่อกลับมาใช้งานใหม่หลังจาก logout ไปแล้ว:

```bash
# 1. Login เข้า VM
ssh username@IPaddress

# 2. เข้าโปรเจค
cd <project_folder>

# 3. ดึงโค้ดล่าสุดจาก GitHub
git pull

# 4. สร้าง screen session
screen -S myapp

# 5. Activate environment
conda activate ai_env

# 6. รัน App
python web_app.py

# 7. Detach (Ctrl + A, D)
# App พร้อมใช้งานแล้วที่ http://<IP>:<PORT>
```

---

## 📝 สรุปขั้นตอนทั้งหมด

```
1. ssh username@IP                     ← login VM
2. git clone / git pull                ← เตรียมโค้ด
3. vi web_app.py                       ← แก้ host='0.0.0.0', port=XXXX
4. Azure Portal → เปิด inbound port   ← เปิด firewall
5. screen -S myapp                     ← สร้าง session
6. conda activate ai_env               ← เข้า environment
7. python web_app.py                   ← รัน App
8. Ctrl + A, D                         ← detach (App ยังทำงาน)
9. exit                                ← logout VM
```

**เข้าถึง Web App ได้ที่:**
```
http://<PUBLIC_IP>:<YOUR_PORT>
```

---

← [Class IV — Environment & Version Control](./Lecture_Class_IV.md) · [README](../README.md) · [Class VI — Web Service →](./Lecture_Class_VI.md)
