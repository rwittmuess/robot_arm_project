# robot_arm_project

## 📌 Project Overview: Simple 6-Axis Robot Arm Control Demo

This project implements a control system for a stationary 6-axis robot arm using Python in the backend and a simple web-based frontend interface for visualization and interaction. The robot arm simulates joint movement with angle constraints and executes smooth transitions between positions.

The application is fully containerized using Docker 🐳 for easy deployment and portability.

## 🛠️ Features

- 6-Axis Robot Arm Simulation:
    - Define and simulate a robot arm with 6 joints, each representing an axis of movement.
- Smooth Movement:
    - Implement smooth transitions between positions using simple linear interpolation.
- Interactive Web GUI:
    - Manual Control: Adjust joint angles via a user-friendly browser interface.
    - Live Visualization: View real-time updates of the robot's joint states and movement.
- Cross-Platform Execution:
    - Both frontend and backend are containerized with Docker for easy deployment and portability.

## 📁 Project Structure
1. **Robot Arm Setup**:
A RobotArm class was implemented with six joints, each defined with a valid angle range (±180°) and a current angle.

2. **User Input**:
Sliders on the frontend collect target angles, which are sent to the backend; the backend checks if they respect joint limits before applying them.

3. **Simplified Smooth Movement**:
A simple interpolation function generates intermediate steps from current to target angles, enabling smooth transitions.

4. **Execution and Visualization**:
The movement sequence is animated in a browser using a canvas-based stick model with colored segments and joint markers.

5. Dockerization:
Backend and frontend are packaged using Docker and launched together via Docker Compose.


## 🚀 Installation & Usage

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (make sure it's **running**)

### Usage 
#### 1. Clone the Repo
Clone the repo and navigate into it:
```bash
git clone <...>
cd \robot_arm_project
```

#### 2. Start Docker containers
Make sure Docker Desktop is running, then in the terminal run:
```bash
docker compose up --build
```

#### 3. Open Frontend 
Open the control panel at ``http://localhost:8080``.

#### 4. Have Fun
Use the control panel to adjust the target joint angles. Then hit "Move Robot" and watch as each joint smoothly aligns with the new position.

## Next Steps and Further ToDo's

- [ ] **Obstacle Avoidance**:
Currently not implemented. Potential future enhancement could involve validating planned paths to prevent self-collisions or interactions with environmental obstacles.