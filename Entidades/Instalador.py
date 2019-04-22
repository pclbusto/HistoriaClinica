import os
from Entidades import Init
import Entidades.Grupo_Entidades

if __name__ == '__main__':
    Entidades.Grupo_Entidades.Base.metadata.create_all(engine)
    #
    # Init.recreateTables()
    # setup = Entidades.Agrupado_Entidades.Setup()
    # setup.directorioBase=os.getcwd()[:-10]
    # session = Init.Session()
    # session.add(setup)
    # session.commit()
    # Init.recreateTablesAll()






