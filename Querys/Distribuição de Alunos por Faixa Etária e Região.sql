SELECT 
    distrito_escola,
    CASE 
        WHEN idade_aluno BETWEEN 0 AND 5 THEN '0-5'
        WHEN idade_aluno BETWEEN 6 AND 10 THEN '6-10'
        WHEN idade_aluno BETWEEN 11 AND 15 THEN '11-15'
        WHEN idade_aluno BETWEEN 16 AND 20 THEN '16-20'
        ELSE '21+'
    END AS faixa_etaria,
    COUNT(*) AS numero_de_alunos
FROM 
    alunos_regioes
GROUP BY 
    distrito_escola, faixa_etaria
ORDER BY 
    distrito_escola, faixa_etaria;
