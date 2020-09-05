-- Create table
CREATE TABLE inventory (
	REF_DATE DATE not null,
	GEO varchar(45) not null,
    Completed VARCHAR (25) not null,
    Type_of_dwelling varchar (25) not null,
    Inventory int not null
	);