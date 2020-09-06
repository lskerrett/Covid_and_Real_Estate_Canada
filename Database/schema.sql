-- Create table
CREATE TABLE inventory (
	REF_DATE DATE not null,
    City VARCHAR(25) not null,
    Province VARCHAR(25) not null,
	Completed_units VARCHAR (25) not null,
    Dwelling_Type VARCHAR (25) not null,
    UNIT_VALUE int not null
	);