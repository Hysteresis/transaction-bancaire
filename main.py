import tkinter as tk
import matplotlib.pyplot as plt
import oracledb

def grosse_categorie_de_depense():
    conn = oracledb.connect(user='system', password='root', host="localhost", port=1521)
    cursor = conn.cursor()
    cursor.execute('''SELECT FK_CATEGORIE, SUM(MONTANT) AS TOTAL_DEPENSE
    FROM F_TRANSACTION
    GROUP BY FK_CATEGORIE
    ORDER BY TOTAL_DEPENSE
    FETCH FIRST 1 ROW ONLY''')
    results = cursor.fetchall()
    for row in cursor.fetchall():
        print(row)
    label_depense.config(text=f"Grosse catégorie de dépense : {results[0][0]}, Total : {results[0][1]} €")
    cursor.close()
    conn.close()

def sous_categorie_revenue():
    conn = oracledb.connect(user='system', password='root', host="localhost", port=1521)
    cursor = conn.cursor()
    cursor.execute('''
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
    ''')
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def evolution_solde():
    conn = oracledb.connect(user='system', password='root', host="localhost", port=1521)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT FK_DATE, MONTANT AS SOLDE
        FROM F_TRANSACTION
        ORDER BY FK_DATE
    ''')
    results = cursor.fetchall()

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

    cursor.close()
    conn.close()

root = tk.Tk()
root.title("Transaction bancaire")

btn_depense = tk.Button(root, text="grosse_categorie_de_depense", command=grosse_categorie_de_depense)
btn_depense.pack()

label_depense = tk.Label(root, )
label_depense.pack()


btn_revenue = tk.Button(root, text="sous_categorie_revenue", command=sous_categorie_revenue)
btn_revenue.pack()

btn_evolution = tk.Button(root, text="évolution du solde", command=evolution_solde)
btn_evolution.pack()

root.mainloop()

