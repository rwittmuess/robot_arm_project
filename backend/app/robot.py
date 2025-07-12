class Joint:
    def __init__(self, name, min_angle, max_angle, current_angle=0):
        self.name = name
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = current_angle

    def set_angle(self, angle):
        if not (self.min_angle <= angle <= self.max_angle):
            raise ValueError(f"{self.name}: {angle} out of range ({self.min_angle}, {self.max_angle})")
        self.current_angle = angle

class RobotArm:
    def __init__(self):
        self.joints = [Joint(f"Joint{i+1}", -180, 180) for i in range(6)]

    def get_joint_angles(self):
        return [j.current_angle for j in self.joints]

    def set_joint_angles(self, angles):
        if len(angles) != len(self.joints):
            raise ValueError("Incorrect number of angles")
        for joint, angle in zip(self.joints, angles):
            joint.set_angle(angle)
