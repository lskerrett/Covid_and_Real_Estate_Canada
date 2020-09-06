-- Create table Inventory
CREATE TABLE inventory (
	REF_DATE DATE not null,
    City VARCHAR(35) not null,
    Province VARCHAR(30) not null,
	Completed_units VARCHAR (25) not null,
    Dwelling_Type VARCHAR (25) not null,
    UNIT_VALUE int not null,
	PRIMARY KEY (City)
	);

-- Create table Price index
    CREATE TABLE price_index (
	REF_DATE DATE not null,
    City VARCHAR(35) not null,
    Province VARCHAR(30) not null,
    Housing_Type VARCHAR(10) not null,
	PRICE_INDEX Int not null,
	PRIMARY KEY (City)
	);
	  
-- -- Create table Canadian population
CREATE TABLE canadian_population (
     city_name VARCHAR(4) NOT NULL,
     city_size_type VARCHAR(40) NOT NULL,
	 city_type VARCHAR(40) NOT NULL,
	 province VARCHAR(40) NOT NULL,
	 pop_2011 Int NOT NULL,
	 pop_density Int NOT NULL,
     PRIMARY KEY (city_name)
);