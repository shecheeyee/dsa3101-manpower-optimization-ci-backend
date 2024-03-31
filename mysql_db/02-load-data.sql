USE mflg;  -- Switch to your database

-- LOAD DATA LOCAL INFILE '/data/csv/mock_availabilty.csv'
-- INTO TABLE Availability
-- FIELDS TERMINATED BY ','  
-- LINES TERMINATED BY '\n'  
-- IGNORE 1 LINES;  

-- LOAD DATA LOCAL INFILE '/data/csv/mock_emp_details.csv'
-- INTO TABLE Employees
-- FIELDS TERMINATED BY ','  
-- LINES TERMINATED BY '\n'  
-- IGNORE 1 LINES;  

-- LOAD DATA LOCAL INFILE '/data/csv/mock_events.csv'
-- INTO TABLE Events
-- FIELDS TERMINATED BY ','
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES;

-- LOAD DATA LOCAL INFILE '/data/csv/mock_wage.csv'
-- INTO TABLE Wage
-- FIELDS TERMINATED BY ','
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES;

INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('1', 'Charin', 'Sneller', '49', 'csneller0@ox.ac.uk', 'M', 'Manager', 'Cook', '4818.28', 'Full time', '3 Prentice Point');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('2', 'Karna', 'Topping', '31', 'ktopping1@si.edu', 'M', 'Dishwasher', 'Dishwasher', '3910.96', 'Full time', '9 Summerview Park');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('3', 'Lindon', 'Kyncl', '44', 'lkyncl2@mysql.com', 'M', 'Server', 'Cook', '0', 'Part time', '9063 American Street');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('4', 'Ruben', 'Blasoni', '46', 'rblasoni3@salon.com', 'F', 'Cook', 'Dishwasher', '2278.67', 'Full time', '212 Gateway Pass');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('5', 'Barret', 'OFielly', '27', 'bofielly4@artisteer.com', 'M', 'Cook', 'Dishwasher', '0', 'Part time', '7482 Namekagon Point');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('6', 'Devan', 'Maddinon', '33', 'dmaddinon5@networksolutions.com', 'F', 'Manager', 'Server', '4553.48', 'Full time', '16780 Sachtjen Hill');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('7', 'Aurea', 'Lademann', '25', 'alademann6@woothemes.com', 'M', 'Cook', 'Server', '0', 'Part time', '0 Spaight Point');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('8', 'Isaiah', 'Hair', '36', 'ihair7@eventbrite.com', 'M', 'Server', 'Server', '0', 'Part time', '40 Cascade Road');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('9', 'Sile', 'Coppins', '59', 'scoppins8@newyorker.com', 'F', 'Server', 'Cook', '0', 'Part time', '1 Nancy Park');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('10', 'Casey', 'Feige', '36', 'cfeige9@instagram.com', 'F', 'Manager', 'Cook', '0', 'Part time', '31 Fuller Parkway');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('11', 'Marybeth', 'Molohan', '55', 'mmolohana@kickstarter.com', 'F', 'Cook', 'Dishwasher', '0', 'Part time', '0027 Logan Junction');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('12', 'Maximilian', 'Perford', '58', 'mperfordb@nationalgeographic.com', 'F', 'Cook', 'Cook', '3806.25', 'Full time', '4 Heath Street');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('13', 'Nanette', 'Braidon', '58', 'nbraidonc@rakuten.co.jp', 'M', 'Dishwasher', 'Server', '0', 'Part time', '871 Bluejay Crossing');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('14', 'Alexandra', 'Dix', '62', 'adixd@goodreads.com', 'M', 'Dishwasher', 'Dishwasher', '4167.84', 'Full time', '66635 2nd Pass');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('15', 'Abram', 'Lamputt', '56', 'alamputte@barnesandnoble.com', 'F', 'Server', 'Dishwasher', '0', 'Part time', '60454 Sloan Place');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('16', 'Ailene', 'Winsper', '38', 'awinsperf@tripadvisor.com', 'F', 'Server', 'Cook', '0', 'Part time', '357 Shoshone Court');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('17', 'Ingamar', 'Warstall', '55', 'iwarstallg@newsvine.com', 'M', 'Dishwasher', 'Cook', '0', 'Part time', '89528 Gateway Center');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('18', 'Oralee', 'Scruby', '42', 'oscrubyh@youtu.be', 'M', 'Server', 'Cook', '3652.23', 'Full time', '25 Center Road');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('19', 'Malory', 'Cruft', '19', 'mcrufti@nbcnews.com', 'F', 'Dishwasher', 'Dishwasher', '3517.18', 'Full time', '5 Eggendart Circle');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('20', 'Prentiss', 'Guppy', '30', 'pguppyj@wired.com', 'F', 'Server', 'Cook', '0', 'Part time', '109 Cambridge Junction');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('21', 'Lev', 'Glasscott', '61', 'lglasscottk@economist.com', 'M', 'Server', 'Dishwasher', '0', 'Part time', '5 Swallow Road');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('22', 'Reggie', 'Showler', '49', 'rshowlerl@mlb.com', 'F', 'Cook', 'Dishwasher', '0', 'Part time', '039 Caliangt Place');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('23', 'Tamqrah', 'Bogue', '61', 'tboguem@netscape.com', 'M', 'Cook', 'Server', '0', 'Part time', '3 Anniversary Point');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('24', 'Gabi', 'Jirzik', '30', 'gjirzikn@unc.edu', 'M', 'Dishwasher', 'Server', '0', 'Part time', '48126 Rutledge Park');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('25', 'Towny', 'Seage', '34', 'tseageo@umn.edu', 'M', 'Manager', 'Server', '4797.83', 'Full time', '73 American Street');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('26', 'Janeen', 'Dinsey', '63', 'jdinseyp@ycombinator.com', 'M', 'Dishwasher', 'Dishwasher', '2126.78', 'Full time', '3 Cardinal Court');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('27', 'Elston', 'Hardway', '64', 'ehardwayq@mail.ru', 'F', 'Cook', 'Server', '3790.72', 'Full time', '8873 Toban Park');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('28', 'Uriah', 'Stanes', '21', 'ustanesr@illinois.edu', 'M', 'Manager', 'Server', '4801.86', 'Full time', '04 Luster Terrace');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('29', 'Katya', 'OBrogan', '61', 'kobrogans@seattletimes.com', 'M', 'Dishwasher', 'Dishwasher', '0', 'Part time', '55 Holy Cross Drive');
INSERT INTO Employees (emp_id, first_name, last_name, age, email, gender, primary_role, secondary_role, wage, status, address) VALUES ('30', 'Cicily', 'Polsin', '40', 'cpolsint@acquirethisname.com', 'M', 'Cook', 'Cook', '3097.49', 'Full time', '0 Monument Junction');

INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('3', '31/12/23', '2', '1', '0', '3', '3', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('5', '31/12/23', '1', '2', '2', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('7', '31/12/23', '2', '2', '0', '3', '3', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('8', '31/12/23', '2', '3', '0', '1', '1', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('9', '31/12/23', '1', '0', '0', '1', '1', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('10', '31/12/23', '2', '2', '2', '2', '1', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('11', '31/12/23', '2', '2', '2', '1', '3', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('13', '31/12/23', '0', '0', '1', '3', '0', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('15', '31/12/23', '3', '3', '1', '0', '1', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('16', '31/12/23', '1', '2', '2', '3', '0', '1', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('17', '31/12/23', '0', '2', '1', '2', '3', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('20', '31/12/23', '2', '2', '3', '3', '3', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('21', '31/12/23', '1', '2', '0', '1', '0', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('22', '31/12/23', '1', '2', '2', '1', '2', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('23', '31/12/23', '1', '3', '1', '1', '1', '1', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('24', '31/12/23', '2', '3', '0', '1', '2', '1', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('29', '31/12/23', '1', '2', '3', '3', '0', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('3', '7/1/24', '1', '0', '0', '3', '1', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('5', '7/1/24', '0', '1', '2', '1', '3', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('7', '7/1/24', '3', '1', '1', '1', '2', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('8', '7/1/24', '1', '2', '2', '0', '0', '2', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('9', '7/1/24', '0', '3', '2', '2', '0', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('10', '7/1/24', '3', '0', '0', '0', '3', '0', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('11', '7/1/24', '2', '1', '2', '3', '0', '1', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('13', '7/1/24', '3', '2', '3', '2', '3', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('15', '7/1/24', '0', '1', '0', '2', '0', '0', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('16', '7/1/24', '1', '1', '2', '1', '1', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('17', '7/1/24', '2', '0', '1', '3', '1', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('20', '7/1/24', '3', '3', '1', '0', '2', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('21', '7/1/24', '1', '0', '0', '2', '2', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('22', '7/1/24', '0', '3', '3', '2', '2', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('23', '7/1/24', '1', '2', '2', '0', '2', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('24', '7/1/24', '2', '1', '1', '0', '0', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('29', '7/1/24', '0', '0', '0', '1', '2', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('3', '14/1/24', '2', '3', '1', '3', '0', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('5', '14/1/24', '1', '3', '0', '2', '0', '3', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('7', '14/1/24', '2', '3', '0', '1', '3', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('8', '14/1/24', '1', '1', '2', '2', '1', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('9', '14/1/24', '0', '2', '1', '0', '2', '2', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('10', '14/1/24', '0', '2', '1', '0', '1', '2', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('11', '14/1/24', '3', '0', '1', '0', '0', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('13', '14/1/24', '1', '3', '1', '2', '1', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('15', '14/1/24', '2', '0', '2', '2', '1', '0', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('16', '14/1/24', '3', '1', '0', '0', '2', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('17', '14/1/24', '3', '2', '0', '3', '0', '0', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('20', '14/1/24', '0', '2', '2', '1', '1', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('21', '14/1/24', '0', '3', '2', '0', '3', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('22', '14/1/24', '1', '3', '2', '0', '3', '0', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('23', '14/1/24', '0', '1', '2', '3', '2', '0', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('24', '14/1/24', '3', '2', '2', '1', '0', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('29', '14/1/24', '2', '0', '1', '1', '1', '0', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('3', '21/1/24', '1', '3', '2', '1', '1', '2', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('5', '21/1/24', '2', '3', '1', '2', '3', '2', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('7', '21/1/24', '2', '3', '2', '0', '1', '2', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('8', '21/1/24', '0', '3', '2', '2', '1', '2', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('9', '21/1/24', '0', '1', '2', '0', '1', '1', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('10', '21/1/24', '1', '1', '2', '2', '3', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('11', '21/1/24', '2', '1', '3', '2', '0', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('13', '21/1/24', '2', '1', '0', '1', '0', '2', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('15', '21/1/24', '2', '2', '0', '3', '3', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('16', '21/1/24', '0', '3', '0', '3', '1', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('17', '21/1/24', '1', '0', '2', '0', '3', '2', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('20', '21/1/24', '3', '1', '0', '3', '0', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('21', '21/1/24', '0', '2', '2', '1', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('22', '21/1/24', '3', '0', '1', '2', '1', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('23', '21/1/24', '2', '1', '3', '2', '1', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('24', '21/1/24', '0', '0', '1', '3', '2', '3', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('29', '21/1/24', '0', '3', '1', '0', '2', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('3', '28/1/24', '0', '0', '0', '0', '1', '0', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('5', '28/1/24', '1', '0', '3', '3', '3', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('7', '28/1/24', '0', '1', '3', '1', '0', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('8', '28/1/24', '2', '3', '1', '1', '0', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('9', '28/1/24', '2', '2', '2', '3', '1', '2', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('10', '28/1/24', '1', '1', '1', '2', '1', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('11', '28/1/24', '2', '1', '2', '1', '2', '1', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('13', '28/1/24', '3', '1', '0', '1', '0', '2', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('15', '28/1/24', '1', '0', '3', '3', '2', '2', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('16', '28/1/24', '0', '1', '3', '1', '3', '2', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('17', '28/1/24', '1', '2', '3', '1', '3', '0', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('20', '28/1/24', '2', '2', '1', '3', '1', '1', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('21', '28/1/24', '1', '1', '0', '0', '2', '1', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('22', '28/1/24', '2', '0', '2', '1', '3', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('23', '28/1/24', '3', '2', '3', '0', '0', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('24', '28/1/24', '3', '3', '3', '0', '3', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('29', '28/1/24', '3', '3', '3', '2', '1', '1', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('1', '31/12/23', '0', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('2', '31/12/23', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('4', '31/12/23', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('6', '31/12/23', '1', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('12', '31/12/23', '3', '0', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('14', '31/12/23', '3', '3', '3', '3', '0', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('18', '31/12/23', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('19', '31/12/23', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('25', '31/12/23', '3', '3', '3', '3', '3', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('26', '31/12/23', '0', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('27', '31/12/23', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('28', '31/12/23', '3', '3', '3', '0', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('30', '31/12/23', '3', '3', '3', '0', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('1', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('2', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('4', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('6', '7/1/24', '1', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('12', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('14', '7/1/24', '3', '3', '3', '3', '3', '0', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('18', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('19', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('25', '7/1/24', '3', '0', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('26', '7/1/24', '3', '3', '0', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('27', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('28', '7/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('30', '7/1/24', '3', '1', '3', '1', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('1', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('2', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('4', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('6', '14/1/24', '1', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('12', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('14', '14/1/24', '3', '0', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('18', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('19', '14/1/24', '3', '3', '3', '3', '0', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('25', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('26', '14/1/24', '3', '3', '0', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('27', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('28', '14/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('30', '14/1/24', '3', '1', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('1', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('2', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('4', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('6', '21/1/24', '1', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('12', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('14', '21/1/24', '3', '3', '3', '3', '3', '3', '2');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('18', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('19', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('25', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('26', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('27', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('28', '21/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('30', '21/1/24', '3', '1', '3', '3', '3', '3', '1');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('1', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('2', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('4', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('6', '28/1/24', '1', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('12', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('14', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('18', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('19', '28/1/24', '3', '3', '3', '0', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('25', '28/1/24', '3', '3', '0', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('26', '28/1/24', '3', '3', '3', '3', '3', '3', '0');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('27', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('28', '28/1/24', '3', '3', '3', '3', '3', '3', '3');
INSERT INTO Availability (emp_id, week, mon, tues, wed, thur, fri, sat, sun) VALUES ('30', '28/1/24', '3', '3', '3', '3', '3', '3', '3');



INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('1', '2024-01-23', 'Random', 'Annual Sandwort', '52', '15:24', '1');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('2', '2024-01-26', 'Wings of time', 'Dot Lichen', '61', '13:37', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('3', '2024-01-10', 'Random', 'Ravens Milkvetch', '25', '20:26', '1');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('4', '2024-01-19', 'Tour', 'Hairy Townsend Daisy', '57', '18:15', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('5', '2024-01-15', 'Random', 'Cypress Spurge', '31', '19:55', '3');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('6', '2024-01-04', 'Company', 'Sesbania', '63', '12:10', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('7', '2024-01-25', 'Company', 'Woodland Flax', '23', '12:42', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('8', '2024-01-30', 'Wings of time', 'Nutmeg Hickory', '96', '18:24', '1');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('9', '2024-01-03', 'Random', 'Desert Pussypaws', '29', '12:06', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('10', '2024-01-30', 'Random', 'Cup Lichen', '85', '20:28', '1');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('11', '2024-01-24', 'Wings of time', 'Trypelthelium Lichen', '89', '13:12', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('12', '2024-01-07', 'Wings of time', 'Geyers Milkvetch', '70', '19:19', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('13', '2024-01-21', 'Company', 'Yellow Avalanche-lily', '84', '15:02', '1');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('14', '2024-01-07', 'Random', 'Smiths Buckthorn', '76', '19:48', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('15', '2024-01-06', 'Company', 'Catillaria Lichen', '66', '17:20', '2');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('16', '2024-01-23', 'Random', 'Woolly Maidenhair', '55', '18:06', '3');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('17', '2024-01-27', 'Company', 'Longbeak Arrowhead', '25', '14:45', '3');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('18', '2024-01-06', 'Company', 'Zigzag Larkspur', '79', '20:17', '3');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('19', '2024-01-21', 'Tour', 'Pricklypear', '63', '20:44', '3');
INSERT INTO Events (event_id, date, event_type, event_name, num_pax, time, duration) VALUES ('20', '2024-01-10', 'Random', 'Quinine', '37', '16:58', '1');

INSERT INTO Wage (day, role, wage) VALUES ('Weekday', 'Server', '13');
INSERT INTO Wage (day, role, wage) VALUES ('Weekday', 'Dishwasher', '13');
INSERT INTO Wage (day, role, wage) VALUES ('Weekday', 'Cook', '15');
INSERT INTO Wage (day, role, wage) VALUES ('Weekend', 'Server', '14');
INSERT INTO Wage (day, role, wage) VALUES ('Weekend', 'Dishwasher', '14');
INSERT INTO Wage (day, role, wage) VALUES ('Weekend', 'Cook', '16');
INSERT INTO Wage (day, role, wage) VALUES ('Public Holiday', 'Server', '15');
INSERT INTO Wage (day, role, wage) VALUES ('Public Holiday', 'Dishwasher', '15');
INSERT INTO Wage (day, role, wage) VALUES ('Public Holiday', 'Cook', '17');
