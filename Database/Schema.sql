-- Create table Inventory
CREATE TABLE inventory (
	inventory_index int not null,
	Ref_Year int not null,
	REf_Month int not null, 
    City VARCHAR(35) not null,
    Province VARCHAR(30) not null,
	Completed_units VARCHAR (25) not null,
    Dwelling_Type VARCHAR (25) not null,
    UNIT_VALUE int not null,
	PRIMARY KEY (inventory_index)
	);

-- Create table Price index
CREATE TABLE price (
	housingprice_index int not null, 
	Ref_Year int not null,
	Ref_Month int not null, 
    City VARCHAR(35) not null,
    Province VARCHAR(30) not null,
    Housing_Type VARCHAR(10) not null,
	PRICE_INDEX int not null,
	PRIMARY KEY (price_index)
	);
