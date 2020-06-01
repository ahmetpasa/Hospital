insert into Doctor values (111,'Paul Watts','Immunologists','111 11 11', 1, 'Bronx, NY');
insert into Doctor values (222,'Leona Aldred','Anesthesiologists','121 12 12', 0, 'SoHo, NY');
insert into Doctor values (333,'Wil Redmond','Cardiologists','131 14 13', 1, 'Harlem, NY');
insert into Doctor values (444,'Lukas Amos','Dermatologists','141 15 14', 1, 'Tribeca, NY');
insert into Doctor values (555,'Anja Smyth','Endocrinologists','151 12 15', 0, 'Nolita, NY');
insert into Doctor values (666,'Cyrus Mercado','Family Physicians','161 31 16', 0, 'Manhattan, NY');
insert into Doctor values (777,'Jozef Wilks','Neurologists','171 11 17', 1, 'Little Italy, NY');
insert into Doctor values (888,'Vanessa Kelly','Family Physicians','181 41 18', 0, 'Chelsea, NY');
insert into Doctor values (999,'Finn Cunningham','Hematologists','191 71 19', 1, 'Bushwick, NY');
insert into Doctor values (500,'Mikhail Arroyo','Nephrologists','101 81 20', 1, 'Crown Heights, NY');

insert into Patient values (11, 111, 'Hadassah Friedman','199 55 78',0,'Brooklyn, NY','33');
insert into Patient values (22, 222, 'Nikola Kouma','199 44 77',1,'Queens, NY','45');
insert into Patient values (33, 333, 'Nico Pitts','199 77 76',1,'Chelsea, NY','28');
insert into Patient values (44, 444, 'Katharine Deleon','199 66 75',0,'Tribeca, NY','53');
insert into Patient values (55, 555, 'Cristian Lugo','199 44 74',1,'Brooklyn, NY','43');
insert into Patient values (66, 666, 'Johnnie Mack','199 33 73',1,'SoHo, NY','29');
insert into Patient values (77, 777, 'Jessie Rosario','199 66 72',0,'Staten Island, NY','66');
insert into Patient values (88, 888, 'Maria Arias','199 55 71',0,'Bronx, NY','35');
insert into Patient values (99, 999, 'Taya Mendez','199 44 70',1,'Bushwick, NY','48');
insert into Patient values (10, 500, 'Monika Kane','199 11 69',0,'Brooklyn, NY','41');

insert into Nurse values (151,'Denis Cano','188 65 41',1,'Brooklyn, NY');
insert into Nurse values (152,'Ellie Page','188 64 40',0,'Bushwick, NY');
insert into Nurse values (153,'Karl Fisher','188 55 42',1,'Tribeca, NY');
insert into Nurse values (154,'Naomi Cole','188 67 43',0,'Queens, NY');
insert into Nurse values (155,'Earl Couch','188 61 44',1,'SoHo, NY');

insert into Meeting values (1,11,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));
insert into Meeting values (2,22,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));
insert into Meeting values (3,33,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));
insert into Meeting values (4,44,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));
insert into Meeting values (5,55,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));
insert into Meeting values (6,66,1,'Initial Appointment',STR_TO_DATE('1-01-2020', '%d-%m-%Y'));

insert into Room values (1,null,151,'service');
insert into Room values (2,11,152,'intensive care');
insert into Room values (3,null,153,'service');
insert into Room values (4,22,153,'intensive care');
insert into Room values (5,33,154,'service');
insert into Room values (6,null,155,'intensive care');

insert into Record values (1,11,STR_TO_DATE('1-01-2020', '%d-%m-%Y'),STR_TO_DATE('1-05-2020', '%d-%m-%Y'), 'surgery');
insert into Record values (2,22,STR_TO_DATE('1-01-2020', '%d-%m-%Y'),STR_TO_DATE('1-05-2020', '%d-%m-%Y'), 'medicine');
insert into Record values (3,33,STR_TO_DATE('1-01-2020', '%d-%m-%Y'),STR_TO_DATE('1-05-2020', '%d-%m-%Y'), 'medicine');
insert into Record values (4,44,STR_TO_DATE('1-01-2020', '%d-%m-%Y'),STR_TO_DATE('1-05-2020', '%d-%m-%Y'), 'surgery');

insert into Medicine values (1156984,5,22,'Parol');
insert into Medicine values (1155566,50,2,'Depakin');
insert into Medicine values (1156941,15,10,'Agumentin');
insert into Medicine values (1156315,40,33,'Beloc');
insert into Medicine values (1156777,13,7,'Norvasc');

insert into Diagnosis values (1,'Healthy');
insert into Diagnosis values (2,'Lung Cancer');
insert into Diagnosis values (3,'Diabetes');
insert into Diagnosis values (4,'Kidney Failure');
insert into Diagnosis values (5,'Hearth Attack');

insert into Has values (3,11);
insert into Has values (2,22);
insert into Has values (5,33);
insert into Has values (1,44);
insert into Has values (1,55);
insert into Has values (1,66);

insert into Given values (1156941,11);
insert into Given values (1156315,22);
insert into Given values (1156777,33);


insert into Users values ('Paul Watts','93e4a7ef57dedbe286be0d9ccfac54f47a89578a343f86a46d8b9dbdf7d2bbf9','doctor');
insert into Users values ('Leona Aldred','969553b158b6467d73c1bc042f050b24bff289290dd46fcf00de0c1254c3f790','doctor');
insert into Users values ('Wil Redmond','7c7b80fb1f558806e749bdf4820d83a8618c9ddb3afb007ef75459f5d83a03f7','doctor');
insert into Users values ('Lukas Amos','505c85eea66d960ed421ccfbfc3e88daf06055eb1bea146b189c87f0e47a7063','doctor');
insert into Users values ('Anja Smyth','07045301748ae87f2c7d05f1fe6c705f9b81d16f48de200ce2475915ddecc618','doctor');
insert into Users values ('Cyrus Mercado','71fc8c75a526c21e5d1126ea154e3cc585202a3aeb28301b2234c78fe204f595','doctor');
insert into Users values ('Jozef Wilks','b7cd80b4d7278ac804b066550fd5eabfbab1a6e88f6ec894cdf1cf678952cdfb','doctor');
insert into Users values ('Vanessa Kelly','a226a2084c6d83e72278aa2c0544817a6b22f4b76cfbf502178c6364abadc75f','doctor');
insert into Users values ('Finn Cunningham','e353f49e5e8ac9e675baa6729d72602fbe32488b5d3b6f373fad11fc8f30aa64','doctor');
insert into Users values ('Mikhail Arroyo','c1b36dbdc536553d15a55ab3a33cb7808b4a78fd21deb3ff6e87fd3e36467231','doctor');

insert into Users values ('Hadassah Friedman','bd48194b5e0e73523ce66b1ec49834059531b4ccb2c0ded9db754c9830750d25','patient');
insert into Users values ('Nikola Kouma','4cbbbd84ba7b6dfe3d475f3d600bef68fe042876f9892165fefbd43ac8896222','patient');
insert into Users values ('Nico Pitts','bc06652a70c88f471bfa250e7309d84d8c753d5cd3dec86e4838e21ce94b9fff','patient');
insert into Users values ('Katharine Deleon','dc198b9b65be72875918f767fd72ec0ff0ca8d739064ac810f443781cf30edcc','patient');
insert into Users values ('Cristian Lugo','6ec4365f03f10e708241762dac5813c11a7e26e679c103b2b1fdd213cd793b9c','patient');
insert into Users values ('Johnnie Mack','402ccfacd78484dea5743421f23ad67c2cc5eb2eb1abf6693428c51dfa792276','patient');
insert into Users values ('Jessie Rosario','5ccf91569e2dd46a8a12be00fe0f2a1d7c8236ea4e95b0f31035ea57b3e10b79','patient');
insert into Users values ('Maria Arias','531b34617e2da6ed23dcfe85e1feeafc3179dbb56fff1df620905907f74d1b9d','patient');
insert into Users values ('Taya Mendez','692c48e010c7158f7ce8d97c0901c310bda516c35305bafc3dbc39efa7e2b5db','patient');
insert into Users values ('Monika Kane','a3a7e7773e0bbe94360fa3dedce73212c074cc76590e6304dfa5934b7e38c178','patient');

insert into Users values ('Denis Cano','5eb223843130692fb5304629160301b3d165b9cdb809f3b882e1030e0bd8a2a8','nurse');
insert into Users values ('Ellie Page','0a30a815d67d7dd2018fe18f4e995a26f3b753369cd4327e9b6034b50a2cd153','nurse');
insert into Users values ('Karl Fisher','ea49f5ee27409740ce7f74997ccf0184f3bbe9a72a86c0faa76db872d9a741f1','nurse');
insert into Users values ('Naomi Cole','47b57de0c88d01209f9cd7f7be8c5ac1718add9bafdbe89b4eb894fcb5a477fb','nurse');
insert into Users values ('Earl Couch','5423762c67c6132604dc4fc686e98ebafc9905eade003e0a8efad6a1624df6f4','nurse');

