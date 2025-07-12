from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List
from .robot import RobotArm
from .controller import interpolate_angles, interpolate_frames

router = APIRouter()
robot = RobotArm()

class MoveRequest(BaseModel):
    # exactly six floats
    target_angles: List[float] = Field(..., min_items=6, max_items=6)
    # positive speed, default 30 deg/s
    speed: float = Field(30.0, gt=0)

    @validator("target_angles")
    def within_limits(cls, v):
        # Cap the angles at ±180° and ensure they are within the range
        return [max(min(a, 180), -180) for a in v]


@router.post("/move")
def move_robot(req: MoveRequest):
    current = robot.get_joint_angles()
    try:
        robot.set_joint_angles(req.target_angles)  # secondary guard
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    frames, step_time = interpolate_frames(
        current, req.target_angles, speed_deg_s=req.speed
    )
    return {"frames": frames, "step_time": step_time}
