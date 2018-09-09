from day12  import orm_many_fk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_many_fk.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例  #cursor

# addr1 = orm_many_fk.Address(street="Tiantongyuan",city="ChangPing",state="BJ")
# addr2 = orm_many_fk.Address(street="Wudaokou",city="Haidian",state="BJ")
# addr3 = orm_many_fk.Address(street="Yanjiao",city="LangFang",state="HB")
#
# session.add_all([addr1,addr2,addr3])
# #ctrl+D复制当前行到下一行,ctrl+Z撤销
# c1 = orm_many_fk.Customer(name="Alex",billing_address=addr1,shipping_address=addr2)
# c2 = orm_many_fk.Customer(name="Jack",billing_address=addr3,shipping_address=addr3)
#
# session.add_all([c1,c2])

obj = session.query(orm_many_fk.Customer).filter(orm_many_fk.Customer.name=="alex").first()
print(obj.name,obj.billing_address,obj.shipping_address)

session.commit()