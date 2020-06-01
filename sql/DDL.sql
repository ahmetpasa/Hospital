CREATE SCHEMA `hospital` ;
use hospital;
create table Doctor
	(Doctor_ID 		INT unsigned NOT NULL,
     Doctor_Name	varchar(40) NOT NULL,
     Speciality     varchar(20) NOT NULL,
     Phone_No		varchar(20),
     Gender			BIT NOT NULL,
     Address 		varchar(140) NOT NULL,
     primary key (Doctor_ID)
	);

create table Patient
	(Patient_ID 	INT unsigned NOT NULL,
	 Doctor_ID		INT unsigned,
     Patient_Name	varchar(40) NOT NULL,
     Phone_No		varchar(20),
     Gender			BIT NOT NULL,
     Address 		varchar(140),
     Age			INT unsigned NOT NULL,
     primary key (Patient_ID),
     foreign key (Doctor_ID) references Doctor (Doctor_ID)
		on delete set null
	);
    
create table Nurse
	(Nurse_ID 		INT unsigned NOT NULL,
     Nurse_Name		varchar(40) NOT NULL,
     Phone_No		varchar(20) NOT NULL,
     Gender			BIT NOT NULL,
     Address 		varchar(140),
     primary key (Nurse_ID)
	);

create table Meeting
	(Meeting_ID			INT unsigned NOT NULL,
	 Patient_ID			INT unsigned,
	 Record_No			INT unsigned,
	 DescriptionColumn	varchar(140) NOT NULL,
     Appointment		Date NOT NULL,
	 primary key (Meeting_ID),
     foreign key (Patient_ID) references Patient (Patient_ID)
		on delete set null
	);
    
create table Room
	(Room_ID  		INT unsigned NOT NULL,
	Patient_ID 		INT unsigned,
	Nurse_ID 		INT unsigned,
	RoomType 		varchar(20) NOT NULL,
	primary key (Room_ID),
	foreign key (Patient_ID) references Patient (Patient_ID)
			on delete set null,
	foreign key (Nurse_ID) references Nurse (Nurse_ID)
			on delete set null
);

create table Record
	(Record_ID 			INT unsigned NOT NULL,
	 Patient_ID 	 		INT unsigned,
	 Date_Admitted   	Date NOT NULL,
	 Date_Discharged 	Date NOT NULL,
	 Tratment 		 	varchar(140) NOT NULL,
	 primary key (Record_ID),
	 foreign key (Patient_ID) references Patient (Patient_ID)
			on delete set null
	);

create table Medicine
	(Medicine_ID	 		 INT unsigned NOT NULL,
	 Price 					 INT unsigned NOT NULL,
     Quantity 				 INT unsigned NOT NULL,
	 MedicineName 		 	 varchar(20) NOT NULL,
	primary key (Medicine_ID)
	);

create table Diagnosis
	(Diagnosis_ID	 INT unsigned NOT NULL,
	 Result 	 	 varchar(140) NOT NULL,
	primary key (Diagnosis_ID)
	);
    
create table Given
	(
    Medicine_ID 	INT unsigned,
    Patient_ID  	INT unsigned,
    primary key (Medicine_ID, Patient_ID),
    foreign key (Patient_ID) references Patient (Patient_ID),
	foreign key (Patient_ID) references Patient (Patient_ID)
    );

create table Has
	(
    Diagnosis_ID 	INT unsigned,
    Patient_ID  	INT unsigned,
    primary key (Diagnosis_ID, Patient_ID),
    foreign key (Patient_ID) references Patient (Patient_ID),
	foreign key (Diagnosis_ID) references Diagnosis (Diagnosis_ID)
    );

create table Users
(	Username varchar(140) NOT NULL UNIQUE,
	Pass VARCHAR(255) NOT NULL,
	Typ varchar(140) NOT NULL
);
