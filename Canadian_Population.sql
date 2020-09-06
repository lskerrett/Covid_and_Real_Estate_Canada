-- Canadian population
CREATE TABLE population (
     city_name VARCHAR(4) NOT NULL,
     city_size_type VARCHAR(40) NOT NULL,
	 city_type VARCHAR(40) NOT NULL,
	 province VARCHAR(40) NOT NULL,
	 pop_2011 Int NOT NULL,
	 pop_density Int NOT NULL,
     PRIMARY KEY (city_name)
);
