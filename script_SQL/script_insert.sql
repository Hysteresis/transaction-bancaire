INSERT INTO D_DATE (PK_DATE)
SELECT DISTINCT TO_DATE(DATE_COMPTA) FROM ODS_TRANSACTION;



INSERT INTO D_TYPE (PK_TYPE)
SELECT DISTINCT TYPE_OPERATION FROM ODS_TRANSACTION;

INSERT INTO D_CATEGORIE (PK_CATEGORIE, CATEGORIE, SOUS_CATEGORIE)
SELECT DISTINCT CATEGORIE || ' - ' || SOUS_CATEGORIE, CATEGORIE, SOUS_CATEGORIE
FROM ODS_TRANSACTION;
SELECT * FROM D_CATEGORIE;

INSERT INTO D_OPERATION (PK_CODE, LABEL)
SELECT 'D' AS PK_CODE, 'Debit' AS LABEL FROM ODS_TRANSACTION WHERE DEBIT != 0
UNION
SELECT 'C' AS PK_CODE, 'Credit' AS LABEL FROM ODS_TRANSACTION WHERE CREDIT != 0;


-----------------------------------------------------------------------------------------------
INSERT INTO F_TRANSACTION (PK_REFERENCE, FK_DATE, FK_TYPE, FK_CATEGORIE, FK_CODE, MONTANT)
SELECT 
    REFERENCE,
    TO_DATE(DATE_COMPTA),
    TYPE_OPERATION,
    CATEGORIE || ' - ' || SOUS_CATEGORIE AS FK_CATEGORIE,
    CASE WHEN DEBIT != 0 THEN 'D'
         WHEN CREDIT != 0 THEN 'C'
         ELSE NULL
    END AS FK_CODE,
    CASE WHEN DEBIT != 0 THEN DEBIT
         WHEN CREDIT != 0 THEN CREDIT
         ELSE NULL
    END AS MONTANT
FROM ODS_TRANSACTION;



SELECT * FROM F_TRANSACTION;