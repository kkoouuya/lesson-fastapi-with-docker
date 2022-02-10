from fastapi import APIRouter
from typing import List
import api.schemas.task as task_sc

router = APIRouter()


@router.get("/tasks", response_model=List[task_sc.Task])
async def list_tasks():
    return [task_sc.Task(id=1, title="test1")]


@router.post("/tasks", response_model=task_sc.TaskCreateResponse)
async def create_task(task_body: task_sc.TaskCreate):
  # **をつけることでdictをキーワード引数として展開
  return task_sc.TaskCreateResponse(id=1, **task_body.dict())


@router.put("/tasks/{task_id}", response_model=task_sc.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_sc.TaskCreate):
    return task_sc.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return


@router.put("/tasks/{task_id}/done", response_model=None)
async def mark_task_as_done(task_id: int):
    return


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(task_id: int):
    return