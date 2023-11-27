use examination;
-- create a procedure to create a question paper
delimiter $$
CREATE PROCEDURE q_p_create(IN qid INT)
BEGIN
  DECLARE table_name VARCHAR(32);
  SET table_name = CONCAT('Q', qid);

  SET @sql = CONCAT('CREATE TABLE IF NOT EXISTS questions.', table_name, ' (id INT PRIMARY KEY AUTO_INCREMENT, question_text TEXT)');

  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END$$
delimiter ;