SELECT
    prd.*,
    comp.name AS company_name
FROM products AS prd,
     companies AS comp
WHERE comp.id = prd.company_id;
