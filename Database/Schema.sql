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
	PRICE_INDEX Numeric not null,
	PRIMARY KEY (housingprice_index)
	);

--Create Join 
SELECT inventory.Ref_Year,
	 inventory.REf_Month, 
	 price.City,
	 price.Province,
	 inventory.Completed_units,
     inventory.Dwelling_Type,
     inventory.UNIT_VALUE,
    price.Housing_Type,
   price.PRICE_INDEX	
FROM inventory
INNER JOIN price
ON inventory.Ref_Year = price.Ref_Year and inventory.REf_Month = price.Ref_month and inventory.City = price.City and inventory.Province = price.Province
