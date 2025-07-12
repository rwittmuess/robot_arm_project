import pytest
from app.robot import RobotArm

def test_set_valid_angles():
    """All six angles inside +-180degr should be accepted."""
    arm = RobotArm()
    target = [10, -20, 30, 40, -50, 60]
    arm.set_joint_angles(target)
    assert arm.get_joint_angles() == target


@pytest.mark.parametrize("bad_angles", [
    [999, 0, 0, 0, 0, 0],      # way too high
    [-181, 0, 0, 0, 0, 0],     # just below min
    [0, 0, 0, 0, 0],           # wrong length
])
def test_reject_invalid_angles(bad_angles):
    """RobotArm should raise ValueError on invalid input."""
    arm = RobotArm()
    with pytest.raises(ValueError):
        arm.set_joint_angles(bad_angles)
