-- Create MySQL server user user_0d_1, then create user if it does not  exist
-- Set the password and grant privilegs to user
    CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
     GRANT ALL PRIVILEGES
        ON *.*
        TO user_0d_1@localhost;
