# Mobile-Robot-Project-on-Linux-Arduino-Application-with-live-simulation-on-Gazebo

The project Demo: 

https://github.com/user-attachments/assets/390f7a5b-6f3b-4f7d-a2bb-409690f299ca










# 🤖 Omnidirectional Mobile Robot with ROS2 & Arduino

## 📌 Project Description

This project presents the full design and implementation of an **omnidirectional mobile robot** using **Mecanum wheels**, developed as part of the Mobile Robots course.

The goal was to gain hands-on experience in:
- Kinematic modeling,
- Hardware integration,
- Simulation using **URDF in ROS2**,
- Real-time control using **Python and Arduino Uno**.

The final result is a fully functional mobile robot that can perform precise movements in all directions, with complete ROS2 integration and hardware control.

---

## 🎯 Objectives

1. **Kinematic Analysis**
   - Build the kinematic model for Mecanum wheel configuration.
   - Calculate transformation matrices to map velocity commands to wheel speeds.

2. **URDF Development**
   - Define robot geometry and structure using modular `.xacro` files.
   - Enable full simulation in **Gazebo** using ROS2.

3. **Control System Development**
   - Translate velocity commands from `cmd_vel` into wheel speeds using Python.
   - Establish USB serial communication with **Arduino Uno** to control motors.

---

## 🧰 Hardware Used

- 🔘 **4x Mecanum Wheels**
- ⚙️ **4x Geared DC Motors**
- 🔌 **L293D Motor Driver**
- 💻 **Arduino Uno**
- 🔋 **Battery Pack**
- 🔗 **USB Cable for Serial Communication**

---

## 🧪 Project Phases

### Phase 1 – Kinematic Design
- Selected 4-wheeled Mecanum configuration.
- Python script used to calculate wheel speeds from linear/angular inputs.

### Phase 2 – Mechanical Assembly
- Built robot structure and integrated motors, driver, Arduino, and battery.

### Phase 3 – Software Development
- URDF files created:
  - `base.xacro`, `motor.xacro`, `lidar.xacro`, `wheel.xacro`, `robot.urdf.xacro`, etc.
- ROS2 control node:
  - Python script listens to `cmd_vel` and sends computed wheel speeds to Arduino via serial.

### Phase 4 – Integration and Testing
- Tested URDF in **Gazebo**.
- Verified motor movement through commands.
- Calibrated motion accuracy and control responses.

---

## ✅ Outcome

- A fully functional omnidirectional robot.
- Real-time movement in response to ROS2 velocity commands.
- Simulation-ready model in ROS2/Gazebo.
- Smooth integration between Python control and Arduino motor actuation.

---

