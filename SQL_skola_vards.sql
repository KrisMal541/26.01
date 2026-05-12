insert or ignore into audzekni values ("A_103", "Marija", "Zālīte", "10b", 17, "01.09.2024.", 50.50);
insert or ignore into audzekni values ("A_104", "Elmārs", "Egle", "10c", 16, "01.09.2023.", 30.01);

select * from audzekni;

select sum(Stipendija) from audzekni;

select max(Stipendija) from audzekni;

select avg(Vecums) from audzekni;

select min(Vecums) from audzekni;

select Vards, Uzvards, Stipendija from audzekni;

