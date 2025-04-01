from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(150), index=False)
    email = Column(String(100), unique=True, index=True)

    # 将对象转换为字典, 并删除密码字段
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
