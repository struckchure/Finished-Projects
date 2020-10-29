import sqlite3 as sql


database_name = 'DiamondRubyQuiz'
connections = sql.connect(f'{database_name}.db')

'''
	Quiz Master Database Functions
'''


def create_quiz_master():
    connections.execute(
        '''
		CREATE TABLE IF NOT EXISTS QuizMasterAuth (
			id INT PRIMARY KEY NOT NULL,
			first_name VARCHAR NOT NULL,
			last_name VARCHAR NOT NULL,
			email VARCHAR NOT NULL,
			username VARCHAR NOT NULL,
			password VARCHAR NOT NULL
			)
		'''
    )
    connections.commit()


def get_quiz_master_column(column):
    selection = connections.execute(
        f'''
        SELECT {column} FROM QuizMasterAuth
        '''
    )
    values = []
    for i in selection:
        values.append(i[0])
    return values


def insert_quiz_master(first_name, last_name, email, username, password):
    if get_quiz_master_column('id'):
        id_ = get_quiz_master_column('id')[-1] + 1
    else:
        id_ = 0
    connections.execute(
        '''
		INSERT INTO QuizMasterAuth(id, first_name, last_name, email, username, password)
			VALUES (?, ?, ?, ?, ?, ?)
		''', (str(id_), first_name, last_name, email, username, password)
    )
    connections.commit()


def get_quiz_master_all():
    selection = connections.execute(
        '''
		SELECT * FROM QuizMasterAuth
		'''
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False


def get_quiz_master_by_id(id_):
    selection = connections.execute(
        '''
		SELECT * FROM QuizMasterAuth WHERE id = ?
		''', (str(id_))
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False


def delete_quiz_master(id_):
    connections.execute(
        '''
		DELETE FROM QuizMasterAuth WHERE id = ?
		''', (str(id_))
    )
    connections.commit()



'''
    Create Quiz Results
'''


def create_quiz_results(quiz_topic):
    quiz_topic = quiz_topic.replace(' ', '_')
    quiz_topic = f'{quiz_topic}_result'
    connections.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {quiz_topic} (
            id INT PRIMARY KEY NOT NULL,
            quiz_topic VARCHAR NOT NULL,
            candidate VARCHAR NOT NULL,
            score VARCHAR NOT NULL
            )
        '''
    )
    connections.commit()


def insert_quiz_results(quiz_topic, id_, candidate, score):
    quiz_topic = f'{quiz_topic}_result'
    try:
        connections.execute(
            f'''
            INSERT INTO {quiz_topic}(id, quiz_topic, candidate, score)
                VALUES (?, ?, ?, ?)
            ''', (str(id_), quiz_topic, candidate, score)
        )
        connections.commit()
    except sql.IntegrityError:
        connections.execute(
            f'''
            UPDATE {quiz_topic}
                SET quiz_topic = ?,
                    candidate = ?,
                    score = ?
            WHERE id = ?
            ''', (quiz_topic, candidate, score, str(id_))
        )
        connections.commit()
    except Exception as e:
        raise e


def get_quiz_results_all(quiz_topic):
    quiz_topic = f'{quiz_topic}_result'
    selection = connections.execute(
        f'''
        SELECT * FROM {quiz_topic}
        '''
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False


def delete_quiz_results(quiz_topic):
    quiz_topic = f'{quiz_topic}_result'
    connections.execute(
        f'''
        DROP TABLE {quiz_topic}
        '''
    )
    connections.commit()


def delete_quiz_results_by_id(quiz_topic, id_):
    quiz_topic = quiz_topic.replace(' ', '_')
    table_name = f'{quiz_topic}_result'
    connections.execute(
        f'''
        DELETE FROM {table_name} WHERE id = ?
        ''', (str(id_))
    )
    connections.commit()


'''
    Create Quiz
'''


def create_quiz(quiz_topic):
    quiz_topic = quiz_topic.replace(' ', '_')
    connections.execute(
        f'''
        CREATE TABLE IF NOT EXISTS {quiz_topic} (
            id INT PRIMARY KEY NOT NULL,
            question VARCHAR NOT NULL,
            option_a VARCHAR NOT NULL,
            option_b VARCHAR NOT NULL,
            option_c VARCHAR NOT NULL,
            option_d VARCHAR NOT NULL,
            answer VARCHAR NOT NULL
            )
        '''
    )
    create_quiz_results(quiz_topic)
    connections.commit()


def insert_quiz(quiz_topic, id_, question, option_a, option_b, option_c, option_d, answer):
    quiz_topic = quiz_topic.replace(' ', '_')
    connections.execute(
        f'''
        INSERT INTO {quiz_topic}(id, question, option_a, option_b, option_c, option_d, answer)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (str(id_), question, option_a, option_b, option_c, option_d, answer)
    )
    connections.commit()


def get_quiz_all(quiz_topic):
    quiz_topic = quiz_topic.replace(' ', '_')
    selection = connections.execute(
        f'''
        SELECT * FROM {quiz_topic}
        '''
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False


def delete_quiz_by_id(quiz_topic, id_):
    table_name = quiz_topic.replace(' ', '_')
    connections.execute(
        f'''
        DELETE FROM {table_name} WHERE id = ?
        ''', (str(id_))
    )
    connections.commit()


def delete_quiz(quiz_topic):
    delete_quiz_results(quiz_topic)
    connections.execute(
        f'''
        DROP TABLE {quiz_topic}
        '''
    )
    connections.commit()


'''
    Create Quiz Check
'''


def create_quiz_check():
    connections.execute(
        '''
        CREATE TABLE IF NOT EXISTS QuizCheck (
            id INT PRIMARY KEY NOT NULL,
            quiz_topic VARCHAR NOT NULL,
            quiz_day VARCHAR NOT NULL,
            quiz_master VARCHAR NOT NULL,
            time_allocated VARCHAR NOT NULL,
            allow_status VARCHAR NOT NULL
            )
        '''
    )
    connections.commit()


def get_quiz_check_by_column(column):
    selection = connections.execute(
        f'''
        SELECT {column} FROM QuizCheck
        '''
    )
    values = []
    for i in selection:
        values.append(i[0])

    return values


def insert_quiz_check(quiz_topic, quiz_day, quiz_master, time_allocated, allow_status):
    all_id = get_quiz_check_by_column('id')
    if len(all_id) != 0:
        id_ = all_id[-1] + 1
    else:
        id_ = 0
    connections.execute(
        f'''
        INSERT INTO QuizCheck(id, quiz_topic, quiz_day, quiz_master, time_allocated, allow_status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (str(id_), quiz_topic, quiz_day, quiz_master, time_allocated, allow_status)
    )
    connections.commit()


def get_quiz_check_all():
    selection = connections.execute(
        f'''
        SELECT * FROM QuizCheck
        '''
    )
    values = []
    for i in selection:
        values.append(i)

    return values


def get_quiz_check_by_id(id_):
    selection = connections.execute(
        '''
        SELECT * FROM QuizCheck WHERE id = ?
        ''', (str(id_))
    )
    values = []
    for i in selection:
        values.append(i)

    return values


def update_quiz_check_status(id_, status):
    connections.execute(
        '''
        UPDATE QuizCheck 
            SET allow_status = ?
        WHERE id = ?
        ''', (status, str(id_))
    )
    connections.commit()


def delete_quiz_check(id_):
    table_name = get_quiz_check_by_id(str(id_))[0][1]
    delete_quiz(table_name)
    connections.execute(
        '''
        DELETE FROM QuizCheck WHERE id = ?
        ''', (str(id_))
    )
    connections.commit()


'''
    Create Quiz Candidates
'''


def create_quiz_candidates():
    connections.execute(
        '''
        CREATE TABLE IF NOT EXISTS QuizCandidates(
            id INT PRIMARY KEY NOT NULL,
            first_name VARCHAR NOT NULL,
            middle_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            mail VARCHAR NOT NULL,
            username VARCHAR NOT NULL,
            password VARCHAR NOT NULL
        )
        '''
    )
    connections.commit()


def get_quiz_candidate_by_column(column):
    selection = connections.execute(
        f'''
        SELECT {column} FROM QuizCandidates
        '''
    )
    values = []
    for i in selection:
        values.append(i[0])

    return values


def insert_quiz_candidate(first_name, middle_name, last_name, mail, username, password):
    all_ids = get_quiz_candidate_by_column('id')
    if len(all_ids) != 0:
        id_ = all_ids[-1] + 1
    else:
        id_ = 0
    print(id_)
    connections.execute(
        '''
        INSERT INTO QuizCandidates(
            id,
            first_name,
            middle_name,
            last_name,
            mail,
            username,
            password
            )
            VALUES(?, ?, ?, ?, ?, ?, ?)
        ''', (id_, first_name, middle_name, last_name, mail, username, password)
    )
    connections.commit()


def get_quiz_candidate_all():
    selection = connections.execute(
        '''
        SELECT * FROM QuizCandidates
        '''
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False
        

def get_quiz_candidate_by_id(id_):
    selection = connections.execute(
        '''
        SELECT * FROM QuizCandidates WHERE id = ?
        ''', (str(id_))
    )
    values = []
    for i in selection:
        values.append(i)
    if values:
        return values
    else:
        return False


def delete_quiz_candidate(id_):
    connections.execute(
        '''
        DELETE FROM QuizCandidates WHERE id = ?
        ''', (str(id_))
    )
    connections.commit()


'''
	Create All Database Tables
'''


def run_all_table_creations():
    create_quiz_master()
    create_quiz_candidates()
    create_quiz_check()


run_all_table_creations()
