from sqlalchemy import column, Integer, String, ForeignKey
from database import Base



class Blog(Base):
    
    id = column(Integer, primary_key=True, index=True)
    
    title = column(String)
    
    body = column(String)