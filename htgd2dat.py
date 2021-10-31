#!/usr/bin/python3
import datetime
import argparse

def create_DB(path_2_file):
	fx = open(path_2_file, "w")
	fx.close()

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


def readlns(input, output):
	dataset = dict()
	dic_rot = 0  								# How many rotations have we spun the dict...

	fro = open(input, "r")
	for _line in fro:
		_line = _line.replace('&', '&amp;')		# XML needs &amp;, not &...
		temp = _line.rstrip().split("\t")

		_sha256 = temp[0]						# sha256 | Not in use...
		_sha1 = temp[2]							# sha1
		_md5 = temp[3]							# md5
		_crc32 = temp[4]						# crc32
		_fsize = temp[5] 						# File Size
		_fpath = temp[1]						# Filepath in database

		temp = temp[1].split("/", 1)
		_dbnme = temp[0]  						# Database Name
		temp = temp[-1].rsplit("/", 1)
		_rname = temp[1]						# ROM name
		_gname = _rname.rsplit(".", 1)
		_gname = _gname[0]						# Game's name

		if dic_rot == 0:
			temp = ['<?xml version="1.0"?>', '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">', '<datafile>', '\t<header>',
				'\t\t<name>HTGDB:{0} database conversion</name>'.format(_dbnme), '\t\t<description>Converted from HTGDB to datxml</description>', '\t\t<version>{0}</version>'.format(datetime.datetime.now().strftime("%Y%m%d-%H%M")),
				'\t\t<author>nedala</author>', '\t\t<homepage>A Winrar is you!</homepage>', '\t\t<url>https://www.winrar.com</url>', '\t</header>']
			writehdr(temp, output)

		temp.clear()

												# Construct a game dictionary/container in logicqX format...
		temp.append('\t<game name="{0}">'.format(_gname))
		temp.append('\t\t<comment>Part of DB: "{0}" | Filepath: "{1}"</comment>'.format(_dbnme, _fpath))
		temp.append('\t\t<description>{0}</description>'.format(_gname))
		temp.append('\t\t<rom name="{0}" size="{1}" crc="{2}" md5="{3}" sha1="{4}"/>'.format(_rname, _fsize, _crc32, _md5, _sha1))
		temp.append('\t</game>')

		dataset.update({dic_rot: {"dat": temp}})
		dic_rot += 1

	fro.close()
	return dataset

def main():
	parser = argparse.ArgumentParser(prog='htgd2dat', description = 'Convert htgd databases to logicqX XML datfiles for use in standard rom managers...')
	parser.add_argument('-i', '--input', help='The filename of the databaste that is to be converted', required = True)
	parser.add_argument('-o', '--output', nargs = '?', help='The name of the converted file...', required = True)
	args = parser.parse_args()

	datdb = dict()
	datdb = readlns(str(args.input), args.output)
	for gid in datdb.values():
		writelns(gid.get("dat"), args.output)
	writeftr(args.output)

if __name__ == "__main__":
	main()
