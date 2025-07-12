from fastapi import APIRouter
from pydantic import BaseModel
from .robot import RobotArm
from .controller import interpolate_angles, interpolate_frames

router = APIRouter()
robot = RobotArm()

class MoveRequest(BaseModel):
    target_angles: list[float]
    speed: float | None = 30.0   # deg/s; higher = faster
    # you could also add duration instead of speed if you prefer

@router.post("/move")
def move_robot(req: MoveRequest):
    current = robot.get_joint_angles()
    robot.set_joint_angles(req.target_angles)          # validate
    frames, step_time = interpolate_frames(
        current,
        req.target_angles,
        speed_deg_s=req.speed
    )
    return {"frames": frames, "step_time": step_time}

