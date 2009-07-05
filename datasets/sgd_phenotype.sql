create table via syncdb
open mysql shell
alter table datasets_sgd_phenotypes drop id;
load data local infile 'H:\phenotype_data.tab' into table datasets_sgd_phenotypes fields terminated by '\t' lines terminated by '\n' ;
alter table datasets_sgd_phenotypes add `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY;

alter table datasets_sgd_interactions drop id;
load data local infile 'H:\interaction_data.tab' into table datasets_sgd_interactions fields terminated by '\t' lines terminated by '\n' ;
alter table datasets_sgd_interactions add `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY;

load data local infile 'H:\registry.genenames.tab' into table datasets_sgd_genenames fields terminated by '\t' lines terminated by '\n' ;

