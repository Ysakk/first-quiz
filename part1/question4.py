import pets_db
import sqlite3
################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

conn = sqlite3.connect('quiz_pets')
cursor = conn.cursor()

sql_pets_owned_by_nobody = """

SELECT animals.name, animals.species, animals.age
FROM animals
LEFT JOIN people_animals ON animals.animal_id = people_animals.pet_id
WHERE people_animals.owner_id IS NULL

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(*) AS num_pets_older_than_owners
FROM animals AS A
JOIN people_animals AS PA ON A.animal_id = PA.pet_id
JOIN people AS P ON PA.owner_id = P.person_id
WHERE A.age > P.age;

"""

#result = conn.execute(sql_pets_older_than_owner).fetchone()
#sql_pets_older_than_owner = result[0]

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT P.name AS person_name, A.name AS pet_name, A.species
FROM animals AS A
JOIN people_animals AS PA ON A.animal_id = PA.pet_id
JOIN people AS P ON PA.owner_id = P.person_id
WHERE P.name = 'bessie'
AND NOT EXISTS (
    SELECT 1
    FROM people_animals AS PA2
    WHERE PA2.pet_id = PA.pet_id
    AND PA2.owner_id <> PA.owner_id
);

"""