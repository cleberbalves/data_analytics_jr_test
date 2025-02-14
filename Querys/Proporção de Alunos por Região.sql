SELECT 
    distrito_escola,
    COUNT(*) AS numero_de_alunos,
    (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM alunos_regioes)) AS proporcao
FROM 
    alunos_regioes
GROUP BY 
    distrito_escola
ORDER BY 
    proporcao DESC;
