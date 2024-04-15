USE mflg;

CREATE TABLE IF NOT EXISTS Employees (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  dob DATE NOT NULL,
  email VARCHAR(50) NOT NULL,
  gender ENUM('M', 'F') NOT NULL,
  primary_role ENUM('Manager', 'Service', 'Kitchen'),
  secondary_role ENUM('Manager', 'Service', 'Kitchen'),
  wage DECIMAL(10,2), 
  status ENUM('Part time', 'Full time'),
  address VARCHAR(256)
);


CREATE TABLE IF NOT EXISTS Availability (
  emp_id INT REFERENCES Employees(emp_id),
  week DATE NOT NULL,
  mon ENUM('None','Morning', 'Night', 'Full'),  -- Values: 0 (Unavailable), 1 (Shift 1), 2 (Shift 2), 3 (Both)
  tues ENUM('None','Morning', 'Night', 'Full'),
  wed ENUM('None','Morning', 'Night', 'Full'),
  thur ENUM('None','Morning', 'Night', 'Full'),
  fri ENUM('None','Morning', 'Night', 'Full'),
  sat ENUM('None','Morning', 'Night', 'Full'),
  sun ENUM('None','Morning', 'Night', 'Full'),
  CONSTRAINT unique_availability UNIQUE (emp_id, week)
);

CREATE TABLE IF NOT EXISTS Schedules (
  scheduleId INT PRIMARY KEY AUTO_INCREMENT,
  emp_id INT,
  week DATE NOT NULL,
  day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  shift ENUM('Morning', 'Night', 'Full') NOT NULL,
  role ENUM('Kitchen', 'Service', 'Manager') NOT NULL,
  CONSTRAINT unique_schedule UNIQUE (emp_id, week, day),
  starttime TIME NOT NULL,
  endtime TIME NOT NULL,
  FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);


CREATE TABLE IF NOT EXISTS Events (
  event_id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  event_type ENUM('Wings of Time', 'Others'),
  event_name VARCHAR(50) NOT NULL,
  event_period ENUM('Morning', 'Night', 'Full') NOT NULL,
  num_pax INT,
  staffReq INT,
  remark VARCHAR(255)  
);

CREATE TABLE IF NOT EXISTS DemandForecast (
  Date DATE,
  Day  VARCHAR(50),
  Time TIME,
  expectedCustomers INT
);

CREATE TABLE IF NOT EXISTS PastDemand (
  Date DATE,
  Day  VARCHAR(50),
  Time TIME,
  actualCustomers INT
);

CREATE TABLE IF NOT EXISTS SummaryStats (
  date DATE PRIMARY KEY,
  shift VARCHAR(50) NOT NULL,
  totalCost DECIMAL(10,2) NOT NULL,
  totalWorkers INT NOT NULL,
  avgHours DECIMAL(5,2),
  CONSTRAINT unique_summary_stats UNIQUE (date, shift)
);

CREATE TABLE IF NOT EXISTS Wage (
    day ENUM('Weekday', 'Weekend', 'Public Holiday'),
    role ENUM('Service', 'Kitchen'),
    wage DECIMAL(10,2) NOT NULL
);