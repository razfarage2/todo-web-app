from enum import Enum


class Status(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    STUCK = "Stuck"
    DELAYED = "Delayed"
    COMPLETED = "Completed"


class Priority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    URGENT = "Urgent"

