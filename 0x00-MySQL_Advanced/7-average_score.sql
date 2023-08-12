-- creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE current_score FLOAT;
    DECLARE average FLOAT;
    DECLARE total_score FLOAT DEFAULT 0.0;
    DECLARE total_count INT DEFAULT 0;

    
    -- Declare a cursor
    DECLARE score_cursor CURSOR FOR SELECT score FROM corrections 
        WHERE corrections.user_id = user_id;

    -- Declare NOT FOUND handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN score_cursor;

    my_loop: LOOP
        FETCH score_cursor INTO current_score;
        IF done THEN
            LEAVE my_loop;
        END IF;
        
        -- total score for a student
        SET total_score = total_score + current_score;
        SET total_count = total_count + 1;
        
    END LOOP my_loop;
    CLOSE score_cursor;

    IF total_count THEN
        SET average = total_score / total_count;
    END IF;

    UPDATE users SET average_score = average WHERE users.id = user_id;
END;
$$
DELIMITER ;
