import tkinter as tk
import matplotlib.pyplot as plt
import oracledb


def connecter_base_de_donnees():
    conn = oracledb.connect(user='system', password='root', host="localhost", port=1521)
    cursor = conn.cursor()
    return conn, cursor


def fermer_base_de_donnees(conn, cursor):
    cursor.close()
    conn.close()


def executer_requete_sql(requete):
    conn, cursor = connecter_base_de_donnees()
    cursor.execute(requete)
    resultats = cursor.fetchall()
    fermer_base_de_donnees(conn, cursor)
    return resultats


def grosse_categorie_de_depense():
    requete = '''SELECT FK_CATEGORIE, SUM(MONTANT) AS TOTAL_DEPENSE
    FROM F_TRANSACTION
    GROUP BY FK_CATEGORIE
    ORDER BY TOTAL_DEPENSE
    FETCH FIRST 1 ROW ONLY'''
    results = executer_requete_sql(requete)
    for row in results:
        print(row)
    label_depense.config(text=f"Grosse catégorie de dépense : {results[0][0]}, Total : {results[0][1]} €")


def sous_categorie_revenue():
    requete = '''
    SELECT
        SUBSTR(FK_CATEGORIE, INSTR(FK_CATEGORIE, '|') + 2) AS SOUS_CATEGORIE,
        SUM(MONTANT) AS TOTAL_CREDIT
    FROM
        F_TRANSACTION
    WHERE
        FK_CODE = 'C' -- Sélectionner seulement les opérations de crédit
    GROUP BY
        FK_CATEGORIE
    ORDER BY
        TOTAL_CREDIT DESC
    FETCH FIRST 1 ROWS ONLY
    '''
    results = executer_requete_sql(requete)
    for row in results:
        print(row)
    label_revenue.config(text=f"Sous catégorie: {results[0][0]}, Total : {results[0][1]} €")


def evolution_solde():
    requete = '''
        SELECT FK_DATE, MONTANT AS SOLDE
        FROM F_TRANSACTION
        ORDER BY FK_DATE
    '''
    results = executer_requete_sql(requete)

    dates = []
    soldes = []

    for row in results:
        dates.append(row[0])
        soldes.append(row[1])
    plt.plot(dates, soldes)
    plt.xlabel('Date')
    plt.ylabel('Crédit')
    plt.title('Évolution du solde')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("Transaction bancaire")

btn_depense = tk.Button(root, text="grosse_categorie_de_depense", command=grosse_categorie_de_depense)
btn_depense.pack()
label_depense = tk.Label(root)
label_depense.pack()

btn_revenue = tk.Button(root, text="sous_categorie_revenue", command=sous_categorie_revenue)
btn_revenue.pack()
label_revenue = tk.Label(root)
label_revenue.pack()

btn_evolution = tk.Button(root, text="évolution du solde", command=evolution_solde)
btn_evolution.pack()

root.mainloop()
