/* 3.2 */
select distinct ncom
from detail d, produit p
where d.npro = p.npro
	and	p.libelle like '%ACIER%';

/* 3.3 */
select d.npro, co.datecom
from commande co, detail d
where co.ncom = d.ncom 
	and extract(year from co.datecom) = 2015;

/* 3.4 */
select cl.ncli, d.npro
from client cl, commande co, detail d
where cl.ncli = co.ncli
	and co.ncom = d.ncom 
	and d.npro = 'CS464';

/* 3.5 */
select d.qcom * p.prix
from commande co, detail d, produit p
where co.ncom = d.ncom 
	and d.npro = p.npro
	and co.ncli = 'C400';

/* 3.6 */
select sum(d.qcom * p.prix)
from detail d, produit p
where d.npro = p.npro
	and p.libelle like '%SAPIN%';

/* 3.7 */
select count(distinct(d.ncom))
from detail d, produit p
where d.npro = p.npro
	and p.libelle like '%ACIER%';

/* 3.8 */
select distinct(localite)
from client cl, commande co, detail d
where cl.ncli = co.ncli
	and co.ncom = d.ncom
	and d.npro = 'CS464';

/* 3.9 */
select distinct d.npro
from detail d, produit p
where d.npro = p.npro
	and p.libelle like '%SAPIN%';

/* 3.10 */
select count(distinct d.ncom)
from detail d, produit p
where d.npro = p.npro
	and p.libelle like '%ACIER%';

/* 3.11 */
select ncli, nom
from client
where ncli not in (
	select cl.ncli
	from client cl, commande co, detail d, produit p
	where cl.ncli = co.ncli
		and co.ncom = d.ncom
		and d.npro = p.npro
		and p.libelle like '%SAPIN%');

/* 3.12 */
select distinct(localite)
from client
where ncli not in (
	select cl.ncli
	from client cl, commande co, detail d
	where cl.ncli = co.ncli
		and co.ncom = d.ncom
		and d.npro = 'PA60'
);

/* 3.13 */
select distinct(localite)
from client cl, commande co
where cl.ncli = co.ncli
	and extract(year from datecom) = 2015
	and extract(month from datecom) = 12;

/* 3.14 */
select npro, libelle
from produit
where npro not in (
	select npro
	from client cl, commande co, detail d
	where cl.ncli = co.ncli
		and co.ncom = d.ncom
		and extract(year from datecom) = 2015
);

/* 3.15 */
