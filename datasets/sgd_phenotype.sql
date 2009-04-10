create table via syncdb
open mysql shell
alter table datasets_sgd_phenotypes drop id;
load data local infile 'phenotype_data.tab' into table datasets_sgd_phenotypes fields terminated by '\t' lines terminated by '\n' ;
alter table datasets_sgd_phenotypes add `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY;

