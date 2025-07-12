import pytest
from app.robot import RobotArm

def test_robot_set_and_get_angles():
    robot = RobotArm()
    target = [10, 20, 30, 40, 50, 60]
    robot.set_joint_angles(target)
    assert robot.get_joint_angles() == target

def test_angle_out_of_bounds():
    robot = RobotArm()
    with pytest.raises(ValueError):
        robot.set_joint_angles([999, 0, 0, 0, 0, 0])
