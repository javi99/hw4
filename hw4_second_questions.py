############################################
#
# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#

list_of_dictionaries = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
                        {'user': 'jane', 'jobs': ['finance', 'software']},
                         { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}]


#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cvs, job_title):
    persons = []
    for cv in cvs:
        if job_title in cv['jobs']:
            persons.append(cv['user'])
    return persons
print(has_experience_as(list_of_dictionaries,'analyst'))

#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.


def job_counts(cvs):
    job_counts_dict = dict()

    for cv in cvs:
        for job in cv["jobs"]:
            if job_counts_dict.get(job) != None:
                job_counts_dict[job] += 1
            else:
                job_counts_dict[job] = 1

    return job_counts_dict

print(job_counts(list_of_dictionaries))


#
# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.

from operator import itemgetter
def most_popular_job(cvs):
    
    job_dictionary = job_counts(list_of_dictionaries)
    job_counts_list = job_dictionary.items()  ##dictionary.items() returns the dictionary as a list of tuples with (key, value) as tuples
    
    for job in job_counts_list:
        if job[1] > 0:
            job_name=max(job_counts_list,key=itemgetter(1))[0] ## del valor màxim de lo que hi ha a la posició 1 dels tuples, agafam el que hi ha a la posició 0
            maxworkers= max(job_counts_list,key=itemgetter(1))[1] ## del valor màxim de lo que hi ha a la posició 1 dels tuples, agafam el que hi ha a la posició 1
    return (job_name, maxworkers)

print(most_popular_job(list_of_dictionaries))
