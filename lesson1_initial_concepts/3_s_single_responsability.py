class SystemRegister:
    
    def register(self, nome : str, idade : int) -> None:
        if self.__validade_input(nome, idade):
            self.__register_user(nome, idade)
        else:
            self._error_handle()
            
    def __validade_input(self, nome : str, idade : int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome : str, idade : int) -> None:
        print("Acessando banco de dados")
        print(f"Cadastrar usuario {nome}, idade {idade}")
    
    def _error_handle(self) -> None:
        print("Invalid data")
        
        
system = SystemRegister()
system.register("Gabriel", 23)