# ☁️ Class II — Cloud Virtual Machines

> Virtual Machine (VM) คือ Server เสมือนที่ทำงานอยู่บนคลาวด์  
> ใช้งานได้เหมือนเครื่อง Linux จริง แต่เข้าถึงได้จากทุกที่ผ่านอินเทอร์เน็ต

---

## 📋 สารบัญ

1. [สร้าง VM บน Azure](#-1-สร้าง-vm-บน-azure)
2. [เชื่อมต่อ Server ด้วย SSH](#-2-เชื่อมต่อ-server-ด้วย-ssh)
3. [จัดการ User บน Server](#-3-จัดการ-user-บน-server)
4. [ส่งไฟล์ด้วย SCP](#-4-ส่งไฟล์ด้วย-scp)
5. [จัดการ Python Environment ด้วย Miniconda](#-5-จัดการ-python-environment-ด้วย-miniconda)
6. [Screen — รัน Process ในพื้นหลัง](#-6-screen--รัน-process-ในพื้นหลัง)
7. [ออกจาก VM](#-7-ออกจาก-vm)
8. [สรุปคำสั่งที่ใช้บ่อย](#-สรุปคำสั่งที่ใช้บ่อย)

---

## 🚀 1. สร้าง VM บน Azure

```
Azure Portal → Education → Virtual Machines → Create a virtual machine
```

**ขั้นตอน:**
1. เลือก **OS Image** — แนะนำ `Ubuntu Server 22.04 LTS`
2. เลือก **Size** — ตามความต้องการ (เช่น Standard_B1s สำหรับงานทั่วไป)
3. ตั้ง **Username** และ **Password** สำหรับการ login
4. เปิด Port **22 (SSH)** เพื่อให้เชื่อมต่อจากภายนอกได้
5. กด **Review + Create** และรอ VM ถูก deploy
6. คัดลอก **Public IP Address** ที่ได้มาเพื่อใช้เชื่อมต่อ

> 💡 **Tip:** จด Username และ IP Address ไว้เสมอ จะได้ใช้ตอน SSH

---

## 🔐 2. เชื่อมต่อ Server ด้วย SSH

SSH (**S**ecure **Sh**ell) คือโปรโตคอลที่ใช้เชื่อมต่อเครื่องของเราไปยัง VM แบบเข้ารหัส

```bash
ssh username@IPaddress
```

| ส่วน | ความหมาย |
|---|---|
| `username` | ชื่อผู้ใช้ที่ตั้งไว้ตอนสร้าง VM |
| `IPaddress` | Public IP Address ของ VM |

**ตัวอย่าง:**
```bash
ssh kanisorn@20.10.123.45
```

**Login / Logout:**
```bash
ssh username@IP     # เข้า VM
exit                # ออกจาก VM (จบ session)
```

> 💡 **Tip:** ครั้งแรกที่ SSH ระบบจะถามว่าเชื่อถือ host นี้ไหม ให้พิมพ์ `yes` แล้วกด Enter

---

## 👥 3. จัดการ User บน Server

### เพิ่ม User ใหม่

ใช้เมื่อต้องการให้เพื่อนหรือผู้ร่วมงานเข้าใช้งาน VM เดียวกัน

```bash
sudo adduser <username>
```

ระบบจะถามให้ตั้ง Password และข้อมูลเพิ่มเติม กด Enter ข้ามได้

### ตรวจสอบ User และ Group

```bash
sudo groups <username>     # ดูว่า user อยู่ใน group ใดบ้าง
who                        # ดูว่าใครกำลัง login อยู่บน server ขณะนี้
```

### ย้าย User เข้า Group

```bash
sudo usermod -aG <groupname> <username>
```

> ⚠️ ควรใช้ `-aG` (append to Group) เสมอ ไม่เช่นนั้น user จะถูกลบออกจาก group เดิมทั้งหมด

### เพิ่มสิทธิ์ SuperUser (sudo)

ให้ user สามารถรันคำสั่งระดับผู้ดูแลระบบได้

```bash
sudo adduser <username> sudo
```

### ตรวจสอบการทำงานของ Server

```bash
htop      # ดู CPU / RAM แบบ real-time (ต้องติดตั้งก่อน)
who       # ดูว่ามีใครใช้งาน server อยู่บ้าง
uptime    # ดูว่า server เปิดมานานแค่ไหน
```

**ติดตั้ง htop:**
```bash
sudo apt update
sudo apt install htop -y
```

> ⚠️ **Warning:** ให้สิทธิ์ `sudo` เฉพาะคนที่ไว้วางใจเท่านั้น เพราะสามารถสั่งได้ทุกอย่างในระบบ

---

## 📤 4. ส่งไฟล์ด้วย SCP

SCP (**S**ecure **C**o**p**y) ใช้ส่งไฟล์ระหว่าง **เครื่องเรา ↔ VM** ผ่านการเชื่อมต่อแบบเข้ารหัส

> ⚠️ **สำคัญ:** ต้องรันคำสั่ง `scp` บน **เครื่องของเรา** เท่านั้น ไม่ใช่ภายใน VM

**รูปแบบพื้นฐาน:**
```bash
scp <source_path> <destination_path>
```

### ส่งไฟล์ เครื่องเรา → VM

```bash
# ส่งไฟล์เดี่ยว
scp ./script.py username@IP:~/code/.

# ส่งทั้งโฟลเดอร์ (-r = recursive)
scp -r ./myfolder username@IP:~/code/.
```

### ดึงไฟล์ VM → เครื่องเรา

```bash
# ดึงไฟล์มาที่ directory ปัจจุบัน
scp username@IP:~/code/script.py .

# ระบุปลายทาง
scp username@IP:~/code/script.py /Users/me/Desktop/.

# ดึงทั้งโฟลเดอร์
scp -r username@IP:~/code/myfolder ./local_backup
```

### Example Workflow

```
# ส่งไฟล์จากเครื่อง → VM แล้วรัน

1. (เครื่องเรา) scp ./app.py kanisorn@20.10.123.45:~/project/.
2. (เครื่องเรา) ssh kanisorn@20.10.123.45
3. (VM)         cd ~/project
4. (VM)         ls              # ตรวจสอบว่าไฟล์มาถึงแล้ว
5. (VM)         python3 app.py  # รัน script
```

> 💡 **Tip:** ใช้ `-P <port>` ถ้า SSH ใช้ port ที่ไม่ใช่ 22 เช่น `scp -P 2222 ./file.py user@IP:~/`

---

## 🐍 5. จัดการ Python Environment ด้วย Miniconda

Miniconda ช่วยจัดการ Python environment แยกสำหรับแต่ละโปรเจค ป้องกัน package conflicts

### ติดตั้ง Miniconda บน VM

```bash
# ดาวน์โหลด installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# รัน installer
bash Miniconda3-latest-Linux-x86_64.sh

# โหลด config ใหม่
source ~/.bashrc
```

### จัดการ Environment

```bash
conda create -n <env_name> python=3.10   # สร้าง environment
conda activate <env_name>                # เข้าใช้งาน
conda deactivate                         # ออกจาก environment
conda env list                           # ดู environment ทั้งหมด
conda remove --name <env_name> --all     # ลบ environment
```

### ติดตั้ง Package

```bash
conda install <package_name>
conda install numpy pandas scikit-learn flask   # ติดตั้งหลายตัวพร้อมกัน
pip install <package_name>                      # ใช้ pip แทน conda ได้
```

**ตรวจสอบ Package ที่ติดตั้ง:**
```bash
conda list            # แสดง package ทั้งหมดใน environment
pip list              # แสดง package ที่ติดตั้งผ่าน pip
```

> 💡 **Tip:** ควรสร้าง environment แยกสำหรับแต่ละโปรเจค เพื่อป้องกัน library conflicts

---

## 🖥️ 6. Screen — รัน Process ในพื้นหลัง

`screen` ช่วยให้ process ทำงานต่อได้แม้จะปิด terminal หรือหลุด SSH

```bash
screen -S <session_name>    # สร้าง session ใหม่
screen -ls                  # ดู session ทั้งหมดที่มีอยู่
screen -r <session_name>    # กลับเข้า session ที่มีอยู่
```

**Keyboard Shortcuts ภายใน screen:**

| ปุ่ม | ความหมาย |
|---|---|
| `Ctrl + A, D` | Detach — ออกจาก session (แต่ยังทำงานอยู่) |
| `Ctrl + A, K, Y` | Kill — ออกและลบ session |
| `Ctrl + A, C` | สร้าง window ใหม่ภายใน session |

> 💡 **Tip:** ใช้ `screen` ทุกครั้งที่รัน process ที่ใช้เวลานาน เช่น train model เพราะถ้า SSH หลุด process จะยังทำงานต่อได้

---

## 🚪 7. ออกจาก VM

```bash
exit            # logout ออกจาก VM (จบ SSH session)
exit()          # ออกจาก Python interactive shell (ต้องมีวงเล็บ)
Ctrl + C        # หยุด process ที่กำลังรันอยู่
```

---

## 📝 สรุปคำสั่งที่ใช้บ่อย

| คำสั่ง | ความหมาย |
|---|---|
| `ssh user@IP` | เชื่อมต่อ VM |
| `exit` | ออกจาก VM |
| `sudo adduser <user>` | เพิ่ม user ใหม่ |
| `sudo adduser <user> sudo` | ให้สิทธิ์ superuser |
| `sudo groups <user>` | ดู group ของ user |
| `htop` | ดูการใช้งาน CPU/RAM |
| `who` | ดูว่าใครกำลัง login อยู่ |
| `scp <src> <dest>` | คัดลอกไฟล์ระหว่างเครื่อง |
| `scp -r <folder> <dest>` | คัดลอกทั้งโฟลเดอร์ |
| `conda create -n <name>` | สร้าง environment |
| `conda activate <name>` | เข้าใช้ environment |
| `screen -S <name>` | สร้าง screen session |
| `screen -r` | กลับเข้า session |

---

← [Class I — Ubuntu Command Line](./Lecture_Class_I.md) · [README](../README.md) · [Class III — Web Page →](./Lecture_Class_III.md)
