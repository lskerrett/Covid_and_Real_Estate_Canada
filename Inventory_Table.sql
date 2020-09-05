-- Creating tables for housing inventory
CREATE TABLE housing_inventory (
     Ref_Date DATE NOT NULL,
     Geo_Area VARCHAR(100) NOT NULL,
	 Completed_Dwelling BOOL NOT NULL,
	 Type_Dwelling BOOL NOT NULL,
	 Coordinates VARCHAR (8) NOT NULL, 
	 Unit_value MONEY NOT NULL,
     PRIMARY KEY (Geo_Area)
     );