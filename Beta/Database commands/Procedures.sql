USE examination;
DELIMITER $$

CREATE PROCEDURE q_p_create(IN qid INT)
BEGIN
  DECLARE table_name VARCHAR(32);
  SET table_name = CONCAT('Q', qid);
  SET @sql = CONCAT('CREATE TABLE IF NOT EXISTS questions.', table_name, ' (qid INT PRIMARY KEY AUTO_INCREMENT, question_text TEXT, option_a TEXT(1), option_b TEXT(), option_c TEXT(), option_d TEXT(), correct CHAR(2))');

  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END$$

DELIMITER ;
