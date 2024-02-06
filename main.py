import tkinter as tk
import oracledb

conn = oracledb.connect(user='system', password='root', host="localhost", port=1521)
cursor = conn.cursor()

# Quelle est la plus grosse catégorie de dépense ?
# cursor.execute('SELECT FK_CATEGORIE, SUM(MONTANT) AS TOTAL_DEPENSE FROM F_TRANSACTION GROUP by FK_CATEGORIE ORDER BY TOTAL_DEPENSE FETCH FIRST 1 ROW ONLY')
# Quelle est la plus grosse sous catégorie de source de revenue ?
cursor.execute('''
SELECT 
    CASE 
        WHEN INSTR(FK_CATEGORIE, '-') > 0 THEN
            SUBSTR(FK_CATEGORIE, INSTR(FK_CATEGORIE, '-', 1, 2) + 2)
        ELSE
            SUBSTR(FK_CATEGORIE, INSTR(FK_CATEGORIE, '-') + 2)
    END AS SOUS_CATEGORIE,
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
# Quelles est l’évolution du solde client à travers le temps ? Faire un graphique


# Execute a SELECT statement


# Fetch the results
results = cursor.fetchall()

# Loop through the results
for row in results:
    print(row)


root = tk.Tk()
root.title("Transaction bancaire")





root.mainloop()



