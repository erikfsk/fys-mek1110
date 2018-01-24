# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import *

def data_dict(txtfile):
	with open(txtfile,"r") as infile:
		data = {}
		identifiers = infile.readline().split()
		for identifier in identifiers:
			data[identifier] = []

		lines = infile.readlines()
		for line in lines: 
			values = line.split()
			for identifier,value in zip(identifiers,values):
				data[identifier].append(float(value))
		for identifier in identifiers:
			data[identifier] = array(data[identifier])
	return data

def make_plot(savefile="test.pdf",xlabel="Wealth [$]",ylabel="Probability [%]"):
	plt.xlabel(xlabel,fontsize=20)
	plt.ylabel(ylabel,fontsize=20)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.xlim(0,10)
	plt.grid("on")
	plt.tight_layout()
	plt.legend(loc="best",fontsize=20)
	plt.savefig(savefile ,bbox_inches="tight")
	plt.clf()