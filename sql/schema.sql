CREATE TABLE IF NOT EXISTS Employees (
  emp_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  age INT NOT NULL,
  email VARCHAR(50) NOT NULL,
  number VARCHAR(50) NOT NULL,
  gender ENUM('M', 'F') NOT NULL,
  primary_role ENUM('Manager', 'Server', 'Cook', 'Dishwasher'),
  secondary_role ENUM('Manager', 'Server', 'Cook', 'Dishwasher'),
  wage DECIMAL(10,2), 
  status ENUM('Part time', 'Full time'),
  address VARCHAR(256)
);

CREATE TABLE IF NOT EXISTS Schedules (
  scheduleId INT PRIMARY KEY AUTO_INCREMENT,
  emp_id INT FOREIGN KEY REFERENCES Employees(emp_id),
  week DATE NOT NULL,
  day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  shift ENUM('Unavailable', 'Shift 1', 'Shift 2', 'Both') NOT NULL,
  CONSTRAINT unique_schedule UNIQUE (employeeId, week, day)
);

CREATE TABLE IF NOT EXISTS Availability (
  emp_id INT PRIMARY KEY REFERENCES Employees(emp_id),
  week DATE NOT NULL,
  mon TINYINT NOT NULL CHECK (mon >= 0 AND mon <= 3),  -- Values: 0 (Unavailable), 1 (Shift 1), 2 (Shift 2), 3 (Both)
  tues TINYINT NOT NULL CHECK (tues >= 0 AND mon <= 3),
  wed TINYINT NOT NULL CHECK (wed >= 0 AND mon <= 3),
  thur TINYINT NOT NULL CHECK (thur >= 0 AND mon <= 3),
  fri TINYINT NOT NULL CHECK (fri >= 0 AND mon <= 3),
  sat TINYINT NOT NULL CHECK (sat >= 0 AND mon <= 3),
  sun TINYINT NOT NULL CHECK (sun >= 0 AND mon <= 3),
  CONSTRAINT unique_availability UNIQUE (employeeId, week)
);


CREATE TABLE IF NOT EXISTS Events (
  event_id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE NOT NULL,
  event_type VARCHAR(50),
  eventName VARCHAR(50) NOT NULL,
  numPax INT,
  time TIME NOT NULL,
  duration DECIMAL(5,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS DemandForecast (
  date DATE PRIMARY KEY,
  expectedCustomers INT NOT NULL,
  peakHours VARCHAR(50),
  weather ENUM('Rain', 'Sun', 'Storm')
);

CREATE TABLE IF NOT EXISTS SummaryStats (
  date DATE PRIMARY KEY,
  shift VARCHAR(50) NOT NULL,
  totalCost DECIMAL(10,2) NOT NULL,
  totalWorkers INT NOT NULL,
  avgHours DECIMAL(5,2),
  CONSTRAINT unique_summary_stats UNIQUE (date, shift)
);

CREATE TABLE IF NOT EXISTS Wage {
    day ENUM('Weekday', 'Weekend', 'Public Holiday'),
    role ENUM('Server', 'Cook', 'Dishwasher'),
    wage DECIMAL(10,2) NOT NULL
};