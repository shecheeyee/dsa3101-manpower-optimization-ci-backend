USE mflg;

CREATE TABLE IF NOT EXISTS Employees (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
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
  mon TINYINT NOT NULL CHECK (mon >= 0 AND mon <= 3),  -- Values: 0 (Unavailable), 1 (Shift 1), 2 (Shift 2), 3 (Both)
  tues TINYINT NOT NULL CHECK (tues >= 0 AND tues <= 3),
  wed TINYINT NOT NULL CHECK (wed >= 0 AND wed <= 3),
  thur TINYINT NOT NULL CHECK (thur >= 0 AND thur <= 3),
  fri TINYINT NOT NULL CHECK (fri >= 0 AND fri <= 3),
  sat TINYINT NOT NULL CHECK (sat >= 0 AND sat <= 3),
  sun TINYINT NOT NULL CHECK (sun >= 0 AND sun <= 3),
  CONSTRAINT unique_availability UNIQUE (emp_id, week)
);

CREATE TABLE IF NOT EXISTS Schedules (
  scheduleId INT PRIMARY KEY AUTO_INCREMENT,
  emp_id INT,
  week DATE NOT NULL,
  day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  shift ENUM('Unavailable', 'Shift 1', 'Shift 2', 'Both') NOT NULL,
  CONSTRAINT unique_schedule UNIQUE (emp_id, week, day),
  FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);


CREATE TABLE IF NOT EXISTS Events (
  event_id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  event_type ENUM('Wings of Time', 'Others'),
  event_name VARCHAR(50) NOT NULL,
  num_pax INT,
  time TIME NOT NULL,
  duration DECIMAL(5,2) NOT NULL
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
    role ENUM('Server', 'Cook', 'Dishwasher'),
    wage DECIMAL(10,2) NOT NULL
);