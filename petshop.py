import mysql.connector

def main():
    # Configurações da conexão
    conn = mysql.connector.connect(
        host='localhost',  # ou o IP do seu servidor MySQL
        user='root',  # substitua pelo seu usuário do MySQL
        password='admin',  # substitua pela sua senha do MySQL
        database='petshopdb'  # o nome do seu banco de dados
    )

    try:
        if conn.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
    finally:
        if conn.is_connected():
            conn.close()
            print("Conexão fechada.")

if __name__ == "__main__":
    main()