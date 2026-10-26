class ConnectDataBase:
    def __init__(self):
        self.connection = None
        
    def conect_db(self):
        self.connection = True
        

class DataRepository:
    def __init__(self, connect_db: ConnectDataBase):
        self.__connect_db = connect_db
        
    def search_data(self):
        if self.__connect_db.connection:
            return [1, 2, 3, 4, 5]
        
        return None


class BusinessRule:
    def __init__(self, repo = DataRepository):
        self.__repo = repo
        
    def compute_results(self):
        data_base = self.__repo.search_data()
        if not data_base:
            print("Data not found. Check your connection to the database.")
        else:
            db_return = lambda data: sum(data)
            
            print(f'The answer is: {db_return(data_base)}')
            
            
conn = ConnectDataBase()
# conn.conect_db()

repo = DataRepository(conn)

rule = BusinessRule(repo)
rule.compute_results()