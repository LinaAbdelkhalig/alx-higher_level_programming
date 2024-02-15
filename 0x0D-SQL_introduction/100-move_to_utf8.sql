-- convert the htn_0c_0 databse to utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- convert the table first_table to utf-8
ALTER TABLE first_table CONVERT TO CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
-- convert the field name in first_table to utf-8
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

