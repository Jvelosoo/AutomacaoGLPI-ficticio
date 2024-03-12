from conector import conectar_banco_de_dados, fechar_conexao

def consultaBanco():
    resultados_consulta = []
    
    conexao = conectar_banco_de_dados()
    if conexao:
        try:
            cursor = conexao.cursor()

            consulta = ("SELECT glpi_tickets.name, glpi_tickets.date, glpi_tickets.id, glpi_locations.name AS locations_name "
                    "FROM glpi_tickets "
                    "JOIN glpi_locations ON glpi_tickets.locations_id = glpi_locations.id "
                    "WHERE glpi_tickets.status = 5")

            cursor.execute(consulta)

            resultados = cursor.fetchall()

            for resultado in resultados:
                # Atribua cada coluna a uma variável
                name_ticket = resultado[0]
                data_ticket = resultado[1]
                id_ticket = resultado[2]
                location_name = resultado[3]

                resultados_consulta.append({
                    "name_ticket": name_ticket,
                    "data_ticket": data_ticket,
                    "id_ticket": id_ticket,
                    "location_name": location_name
                })

        finally:
            cursor.close()
            fechar_conexao(conexao)

    return resultados_consulta
