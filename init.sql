-- Create table
CREATE TABLE mytable (
  Datetime TIMESTAMP,
  Sirta_GHI FLOAT,
  Sat_GHI_0 FLOAT,
  Clearsky_GHI FLOAT,
  Arpege_GHI FLOAT,
  SZA FLOAT,
  Kc_Sat_mean FLOAT,
  Kc_Sat_std FLOAT,
  Kc_obs FLOAT,
  Wreg FLOAT,
  Sat_GHI_15 FLOAT,
  Sat_GHI_30 FLOAT,
  Sat_GHI_45 FLOAT,
  Sat_GHI_60 FLOAT,
  Sat_GHI_75 FLOAT,
  Sat_GHI_90 FLOAT,
  Sat_GHI_105 FLOAT,
  Sat_GHI_120 FLOAT,
  Sat_GHI_135 FLOAT,
  Sat_GHI_150 FLOAT,
  Sat_GHI_165 FLOAT,
  Sat_GHI_180 FLOAT,
  Sat_GHI_195 FLOAT,
  Sat_GHI_210 FLOAT,
  Sat_GHI_225 FLOAT,
  Sat_GHI_240 FLOAT,
  Sat_GHI_255 FLOAT,
  Sat_GHI_270 FLOAT,
  Sat_GHI_285 FLOAT,
  Sat_GHI_300 FLOAT,
  Sat_GHI_315 FLOAT,
  Sat_GHI_330 FLOAT,
  Sat_GHI_345 FLOAT,
  Sat_GHI_360 FLOAT,
  year INT,
  month INT,
  hour INT,
  dayofweek INT,
  quarter INT,
  dayofyear INT
);

-- Import data from CSV file
COPY mytable FROM '/app/data.csv' DELIMITER ',' CSV HEADER;

