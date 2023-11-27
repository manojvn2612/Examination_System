use examination;
DELIMITER $$
CREATE FUNCTION last_q()
RETURNS int
deterministic
BEGIN
DECLARE lastValue int;
SET lastValue = (SELECT qid FROM question_paper ORDER BY qid DESC LIMIT 1);
RETURN lastValue;
END $$
DELIMITER ;

SELECT last_q();
