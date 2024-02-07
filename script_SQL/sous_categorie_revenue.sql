SELECT SUBSTR(FK_CATEGORIE, INSTR(FK_CATEGORIE, '|') + 2) AS SOUS_CATEGORIE,
    SUM(MONTANT) AS TOTAL_CREDIT
FROM F_TRANSACTION
WHERE FK_CODE = 'C'
GROUP BY FK_CATEGORIE
ORDER BY TOTAL_CREDIT DESC
FETCH FIRST 1 ROW ONLY;

