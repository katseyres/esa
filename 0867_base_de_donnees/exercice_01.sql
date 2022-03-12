/* 1.1 */
select *
from client;

/* 1.2 */
select localite
from client;


/* 1.3 */
select ncli, nom, localite 
from client c
where
    cat = 'C1'
	and localite != 'Toulouse';

/* 1.4 */
select * from produit
where
    libelle like '%ACIER%';

/* 1.5 */
select *
from client
where 
	localite in ('Poitiers', 'Bruxelles')
	and compte >== 0;

/* 1.6 */
select cat
from client
where 
	localite = 'Toulouse'
	and cat is not null;

/* 1.7 */
select localite, ncli
from client
where
	nom < localite;

/* 1.8 */
select
	sum(compte),
	min(compte),
	avg(compte),
	max(compte)
from client;

/* 1.9 */
select ncli
from commande
where ncom in (
    select ncom
	from detail
	where npro = 'CS464'
);

/* 1.10 */
select localite
from client
where ncli in (
	select ncli
	from commande
	where ncom in (
		select ncom
		from detail
		where npro = 'CS464'
	)
);

/* 1.11 */
select ncli, nom
from client
where
	localite = 'Namur'
	and ncli not in (
		select ncli
		from commande
);

/* 1.12 */
select npro
from detail
where npro in (
	select npro
	from produit
	where libelle like '%SAPIN%'
);

/* 1.13.1 */
select *
from client
where
	localite = 'Lille'
	or localite = 'Namur';

/* 1.13.2 */
select *
from client
where
	localite = 'Lille';

/* 1.13.3 */
select *
from client
where
	localite = 'Lille'
	or localite != 'Namur';

/* 1.13.4*/
select *
from client
where
	localite != 'Lille'
	and localite != 'Namur';

/* 1.13.5 */
select *
from client;

/* 1.13.6 */
select *
from client
where
	cat = 'C1'
	and localite = 'Namur';

/* 1.13.7 */
select *
from client
where
	cat = 'C1'
	or localite = 'Namur';

/* 1.13.8 */
select *
from client
where
	cat = 'C1'
	and localite != 'Namur';

/* 1.13.9 */
select *
from client
where ncli not in (
	select ncli
	from client
	where
		cat = 'C1'
		and localite != 'Namur'
);
 /* 1.13.10 */
select *
from client
where
	cat in ('B1', 'C1')
	or localite in ('Lille', 'Namur');
	
/* 1.13.11 */
select * 
from client
where
	(localite in ('Namur', 'Lille')
	and cat not in ('B1', 'C1'))
	or(cat in ('B1', 'C1')
		and localite not in ('Namur', 'Lille'));

/* 1.13.12 */
select *
from client
where 
	cat in ('B1', 'C1')
	and localite in ('Lille', 'Namur');
	
/* 1.13.13 */
select *
from client
where ncli not in (
	select ncli
	from client
	where 
		cat in ('B1', 'C1')
		and localite in ('Lille', 'Namur')
);

/* 1.14 */
select sum(prix * qstock)
from produit;

/* 1.15.1 */
select *
from produit
where 
	libelle like '%SAPIN%' and
	npro not in (select npro from detail);
	
/* 1.15.2 */
select p.npro
from client cl, commande co, detail d, produit p
where cl.ncli = co.ncli
	and cl.localite = 'Toulouse'
	and co.ncom = d.ncom
	and d.npro = p.npro
	and p.libelle like '%SAPIN%';

/* 1.15.3 */
select p.npro, p.libelle
from client cl, produit p, detail d, commande co
where cl.ncli = co.ncli and co.ncom = d.ncom and p.npro = d.npro
	and p.libelle like '%SAPIN%'
	and cl.localite != 'Toulouse';	

/* 1.15.4 */
select *
from produit
where npro not in (
		select npro
		from client cl, commande co, detail d
		where
			cl.ncli = co.ncli
			and co.ncom = d.ncom
			and cl.localite != 'Toulouse'
	)
	and npro in (select npro from detail)
	and libelle like '%SAPIN%';

/* 1.15.5 */
select npro, libelle
from produit
where npro not in (
	select p.npro
	from detail d, produit p, client cl, commande co
	where p.npro in (
		select npro from produit
		where libelle like '%SAPIN%'
	)
	and p.npro = d.npro
	and d.ncom = co.ncom
	and co.ncli = cl.ncli
	and localite != 'Toulouse'
	)
	and libelle like '%SAPIN%';

/* 1.15.6 */
select npro, libelle from produit
where libelle like '%SAPIN%';

/* 1.16 */
select count(ncom) from commande
where ncom in (
	select ncom from detail
	where npro in (
		select npro from produit
		where libelle like '%ACIER%'
	)
);

/* 1.17 */
select count(distinct localite) from client
where cat = 'C1';

/* 1.18 */
select * from produit
where npro not in (
	select npro from detail 
);

select * from produit
where not exists(select npro from detail
	where npro = produit.npro
);

select npro from produit
except select npro from detail;

/* 1.19 */
select ncli, nom from client
where ncli in (
	select ncli from commande
	where ncom not in (
		select ncom from detail
		where npro in (
			select npro from produit
			where libelle like '%SAPIN%'
		)
	)
);

/* 1.21 */
/*
	sélectionne la ligne
	de la commande
	où le numéro de commande n'est pas dans
		(sélectionne le numéro de commande
		 de détail
		 où le numéro de produit n'est pas du PA60
		)

	donc sélectionner la ligne qui ne commande que du PA60
*/

/* 1.22 */
select * from commande
where datecom >= '2008-12-01'
		and datecom <= '2008-12-31';

select distinct localite
from client cl, commande co
where cl.ncli = co.ncli
	and datecom between '2015-12-01' and '2015-12-31';

select distinct localite
from client cl
where ncli in (select ncli
	from commande
	where extract(year from datecom) = 2015
		and extract(month from datecom) = 12);

/* 1.23 */
select * from detail
where ncom not in (
	select ncom from commande
);

/* 1.24 */
select * from commande
where ncom not in (
	select ncom from detail
);

/* 1.25 */
select npro, libelle from produit
where npro in (
	select npro from detail
	where ncom in (
		select ncom from commande
		where datecom < '2008-12-01'
			and datecom > '2008-12-31'
	)
);

/* 1.26 */
select nom
from client c
where not exists (
	select npro
	from produit
	where npro not in (
		select npro
		from detail d, commande c
		where d.ncom = c.ncom
			and c.ncli = c.ncli
	)
);
















