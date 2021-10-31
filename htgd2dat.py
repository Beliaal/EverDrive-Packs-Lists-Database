#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use a HTGD database and convert it to Logiqx - DTD ROM Management Datafile format. "http://www.logiqx.com/Dats/datafile.dtd"
"""
import datetime

def create_DB(path_2_file):
	fx = open(path_2_file, "w")
	fi = open("./venv/include/num.txt", "w")
	fx.close()
	fi.close()

def writeftr(path_2_file):
	frw = open(path_2_file, "a")
	frw.write("</datafile>")
	frw.close()

def writehdr(towrite, path_2_file):
	frw = open(path_2_file, "a")
	for _val in towrite:
		frw.write(_val + "\n")
	frw.close()

def writelns(towrite, path_2_file):
	frw = open(path_2_file, "a")
	for _val in towrite:
		frw.write(_val + "\n")
	frw.close()

def readlns(path_2_db):
	databucket = dict()
	dic_rot = 0					# How many rotations have we spun the dict...

	fro = open(path_2_db, "r")
	for _line in fro:
		_line = _line.replace('&', '&amp;')
		temp = _line.rstrip().split("\t")

		_sha256 = temp[0]
		_sha1 = temp[2]
		_md5 = temp[3]
		_crc32 = temp[4]
		_fsize = temp[5]  # File Size
		_fpath = temp[1]

		temp = temp[1].split("/", 1)
		_dbnme = temp[0]  # Database Name
		temp = temp[-1].rsplit("/", 1)
		_rname = temp[1]
		_gname = _rname.rsplit(".", 1)
		_gname = _gname[0]

		if dic_rot == 0:
			temp = ['<?xml version="1.0"?>']
			temp.append('<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">')
			temp.append('<datafile>')
			temp.append('\t<header>')
			temp.append('\t\t<name>HTGDB:{0} database conversion</name>'.format(_dbnme))
			temp.append('\t\t<description>Converted from HTGDB to datxml</description>')
			temp.append('\t\t<version>{0}</version>'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M")))
			temp.append('\t\t<author>nedala</author>')
			temp.append('\t\t<homepage>A Winrar is you!</homepage>')
			temp.append('\t\t<url>https://www.winrar.com</url>')
			temp.append('\t</header>')
			writehdr(temp, "./venv/include/out.dat")

		temp.clear()

		# Construct a game container...
		temp.append('\t<game name="{0}">'.format(_gname))
		temp.append('\t\t<comment>Part of DB: "{0}" | Filepath: "{1}"</comment>'.format(_dbnme, _fpath))
		temp.append('\t\t<description>{0}</description>'.format(_gname))
		temp.append('\t\t<rom name="{0}" size="{1}" crc="{2}" md5="{3}" sha1="{4}"/>'.format(_rname, _fsize, _crc32, _md5, _sha1))
		temp.append('\t</game>')

		databucket.update({dic_rot: {"dat": temp}})
		dic_rot += 1
		fi = open("./venv/include/num.txt", "a")
		fi.write(str(dic_rot) + "  " + _gname + "\n")
		fi.close()

	fro.close()
	return databucket



def main():
	outfile_n_path = "./venv/include/out.dat"
	#conversionDB = "./venv/include/indata.mini.dat"
	conversionDB = "./venv/include/indata.dat"
	create_DB(outfile_n_path)				# Make sure we create a new file from start.

	datdb = dict()
	datdb = readlns(conversionDB)
	#writehdr(outfile_path + outfile_name)
	for gid in datdb.values():
		#print(gid.get("dat"))
		#testlist = gid.get("dat")
		writelns(gid.get("dat"), outfile_n_path)
	writeftr(outfile_n_path)


if __name__ == "__main__":
	main()
