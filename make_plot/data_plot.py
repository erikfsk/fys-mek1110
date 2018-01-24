# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from data_dict import *



# 1 FILE 
TEST_DICT = data_dict("test.txt")
plot(TEST_DICT["X"],TEST_DICT["Y"])
make_plot("test.pdf","Wealth [$]","Probability [%]")



#MANY FILES
from subprocess import Popen, PIPE
import re
import os
output = Popen(["ls"], stdout=PIPE).communicate()[0]
txtfiles = re.findall(".*\.txt",output,re.IGNORECASE)

for txtfile in txtfiles:
	TEST_DICT = data_dict(txtfile)
	plot(TEST_DICT["X"],TEST_DICT["Y"])
	make_plot("test2.pdf","Wealth [$]","Probability [%]")

print txtfiles


