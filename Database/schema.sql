-- Create table
CREATE TABLE inventory (
	REF_DATE DATE not null,
    City VARCHAR(35) not null,
    Province VARCHAR(30) not null,
	Completed_units VARCHAR (25) not null,
    Dwelling_Type VARCHAR (25) not null,
    UNIT_VALUE int not null
	);

    CREATE TABLE price_index (
	REF_DATE DATE not null,
    GEO VARCHAR(60) not null,
    Housing_Type VARCHAR(10) not null,
	PRICE_INDEX DOUBLE not null
	);