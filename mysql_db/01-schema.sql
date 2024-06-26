USE mflg;

CREATE TABLE IF NOT EXISTS Employees (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL UNIQUE,
  primary_role ENUM('Manager', 'Service', 'Kitchen'),
  secondary_role ENUM('Manager', 'Service', 'Kitchen'),
  wage DECIMAL(10,2), 
  status ENUM('Part Time', 'Full Time')
);


CREATE TABLE IF NOT EXISTS Availability (
  emp_id INT REFERENCES Employees(emp_id),
  week DATE NOT NULL,
  Monday ENUM('None','Morning', 'Night', 'Full'), 
  Tuesday ENUM('None','Morning', 'Night', 'Full'),
  Wednesday ENUM('None','Morning', 'Night', 'Full'),
  Thursday ENUM('None','Morning', 'Night', 'Full'),
  Friday ENUM('None','Morning', 'Night', 'Full'),
  Saturday ENUM('None','Morning', 'Night', 'Full'),
  Sunday ENUM('None','Morning', 'Night', 'Full'),
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
  event_name VARCHAR(50) NOT NULL,
  event_period ENUM('Morning', 'Night', 'Full') NOT NULL,
  staffReq INT,
  num_pax INT,
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