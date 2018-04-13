import os
cwd = os.getcwd()
# a = '{0}/javatests/com/williamfiset/algorithms'.format(os.getcwd())
# os.chdir(a)
# s = 'java -classpath "{0}/randoop-4.0.3/randoop-all-4.0.3.jar":"{0}/build/classes/main/" randoop.main.Main gentests --testclass=com.williamfiset.algorithms.strings.RabinKarp --output-limit=100'.format(os.getcwd())
s = 'java -classpath "{0}/randoop-4.0.3/randoop-all-4.0.3.jar":"{0}/build/classes/main/" randoop.main.Main gentests --classlist={0}/classes.txt --output-limit=100'.format(cwd)
os.system(s)

