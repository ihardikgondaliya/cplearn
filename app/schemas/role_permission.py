from pydantic import BaseModel

class RolePermissionBase(BaseModel):
    role_id: int
    permission_id: int

class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermission(RolePermissionBase):
    class Config:
        orm_mode = True